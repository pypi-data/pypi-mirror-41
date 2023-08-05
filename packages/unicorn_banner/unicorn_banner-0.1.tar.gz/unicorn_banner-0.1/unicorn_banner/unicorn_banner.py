from time import sleep
import threading
import Queue

try:
    import unicornhat as unicorn
except ImportError:
    exit("This class requires the unicornhat module")

try:
    from pyfiglet import figlet_format
except ImportError:
    exit("This class requires the pyfiglet module\nInstall with: sudo pip install pyfiglet")

# TODO: add some way of signalling thread to stop
class UnicornBanner(threading.Thread):

    # Init to 2 dim array
    matrix = None
    width = None
    height = None
    i = -1
    on = False
    delay = 0.1

    """ Create a UnicornBanner object
    
    Arguments: 
      - a Queue.Queue object. This can be used to update text and colour when the banner
        is running.
      - The text that will be initially displayed
      - The colour that the initial text will be displayed in.
      
    Start the banner by calling the start() method (from Thread parent class).
    
    Update text by putting a new item in to the text queue. 
    The item should be a dict with 'text' and 'colour'. Text contains the new
    text to be displayed, colour contains the colour as a list
    of [r, g, b] values (unsigned bytes)
    """
    def __init__(self, text_q, text, colour=[255, 0, 0]):
        super(UnicornBanner, self).__init__()
        self.text_q = text_q
        self._prepare_unicornhat()
        self._build_matrix(text)
        self.colour = colour
        self._stop_request = threading.Event()

    def _prepare_unicornhat(self):
        unicorn.set_layout(unicorn.AUTO)
        unicorn.rotation(0)
        unicorn.brightness(0.5)
        self.width, self.height = unicorn.get_shape()

    def _build_matrix(self, text):
        figlet_text = figlet_format(text + ' ', "banner", width=1000)  # banner font generates text with heigth 7
        self.matrix = figlet_text.split("\n")[:self.width]  # width should be 8 on both HAT and pHAT!

    def run(self):
        while not self._stop_request.isSet():
            self._step()
            try:
                # Check the queue for new text, if none present
                # wait the timeout value
                item = self.text_q.get(True, 0.05)
                self._build_matrix(item['text'])
                if item['colour'] is not None:
                    self.colour = item['colour']
            except Queue.Empty:
                continue

    def stop(self, timeout=None):
        self._stop_request.set()
        self.join(timeout)

    def _step(self):
        text_width = len(self.matrix[0])  # the total length of the result from figlet
        self.i = 0 if self.i >= 1000 * text_width else self.i + 1  # avoid overflow
        for h in range(self.height):
            for w in range(self.width):
                h_pos = (self.i + h) % text_width
                chr = self.matrix[w][h_pos]
                if chr == ' ':
                    unicorn.set_pixel(self.width - w - 1, h, 0, 0, 0)
                else:
                    unicorn.set_pixel(self.width - w - 1, h, self.colour[0], self.colour[1], self.colour[2])
        unicorn.show()
        sleep(self.delay)

