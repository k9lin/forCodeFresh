class Microclass1:
    msg = None
    def __init__(self, msgIn):
        self.msg = msgIn

    def sayIt(self):
        print(Microclass1.__name__ + u" says: " + self.msg)