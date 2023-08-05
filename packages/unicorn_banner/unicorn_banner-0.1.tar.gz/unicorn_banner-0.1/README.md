# RaspberryPi UnicornHat banner

A class can display text as a banner on a Unicorn Hat device.

## Unicorn Hat

https://shop.pimoroni.com/products/unicorn-hat


## Usage

Create a UnicornBanner object and put a Queue and initial text in it:

    from Queue import Queue
    from time import sleep
    from unicorn_banner import UnicornBanner    
   
    text_q = Queue()
   
    ubanner = UnicornBanner(self.text_q, "Hello World!")
    
Start it:

    ubanner.start()
    sleep(10)
    
Admire the result

![Hello World banner](doc/hello_world.jpg)
    
Change the text and colour

    text_q.put({'text': "Hello Python!", 'colour': [0, 255, 0]})
    sleep(10)
    
![Hello Python banner](doc/hello_python.jpg)
    
And stop

    ubanner.stop()
    
      
    
      
      