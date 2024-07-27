"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        """Initialization string for class"""
        self.start = start
        self.initial = start
    def generate(self):
        """Increases number by 1 and returns new value"""
        self.start += 1
        return self.start
    def reset(self):
        """Resets to our default start value, 100"""
        self.start = self.initial
        return self.start
    
