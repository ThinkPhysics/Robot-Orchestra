from threading import Timer
from time import sleep


class RepeatedTimer(object):
    """Simple timer class, from StackExchange (obviously)."""
    def __init__(self, interval, function, *args, **kwargs):
        """Initialize the timer object."""
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        """Timer has been triggered: execute callback function."""
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        """Start the timer, if it's not already running."""
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        """Stop the timer."""
        self._timer.cancel()
        self.is_running = False


def hello(name):
    print "Hello %s!" % name


output = "World"
print "starting..."
rt = RepeatedTimer(0.01, hello, output)
try:
    sleep(5)
    output = "Jonathan"
    # Have to stop and restart for data to update
    rt.stop()
    rt = RepeatedTimer(0.1, hello, output)
    sleep(5)
    # more code here
finally:
    rt.stop()
