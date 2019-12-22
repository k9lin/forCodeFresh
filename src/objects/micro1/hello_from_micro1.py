#!/usr/bin/env python
'''module doc string'''
class Microclass1:
    '''Class doc string'''
    msg = None
    def __init__(self, msgIn):
        '''docstring for constructor.'''
        self.set_messge(msgIn)
    def say_it(self):
        '''docstring for say_it.'''
        print(self.__name__ + u" says: " + self.msg)
    def set_message(self, msgIn):
        '''docstring for set_message.'''
        self.msg = msgIn
