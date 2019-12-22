#!/usr/bin/env python
'''module doc string'''
class Microclass1:
    '''Class doc string'''
    msg = None
    def __init__(self, msg_in):
        '''docstring for constructor.'''
        self.set_message(msg_in)
    def say_it(self):
        '''docstring for say_it.'''
        print(Microclass1.__name__ + u" says: " + self.msg)
    def set_message(self, msg_in):
        '''docstring for set_message.'''
        self.msg = msg_in
