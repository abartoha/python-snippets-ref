'''
118-Threading timer.

By Steve Shambles
Visit my blog for more snippets like this
stevepython.wordpress.com
'''
from threading import Timer

def timer():
    '''Threading timer'''
    # Your code here, It will be executed every 4 seconds.
    print("The seconds goes by quickly here!")

    # Change the 4 seconds to your requirements, 0.01 to infinity.
    t = Timer(4.0, timer)
    t.start()

# Starts the timer.
timer()


# Or maybe you want 2 minutes?
# t = Timer(2*60.0, timer)
