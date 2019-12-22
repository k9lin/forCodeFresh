#!/usr/bin/env python
"""Documentation for this class"""
class Microclass1:
    msg = None
    """Constructor"""
    def __init__(self, msgIn):
        self.msg = msgIn
    """say_it method"""
    def say_it(self):
        print(Microclass1.__name__ + u" says: " + self.msg)
