class MicroClass1:
  msg = None
  def __init__(self, msgIn):
    self.msg = msgIn
    
  def sayIt():
    print(MicroClass1.__name__ + " says: " + self.msg)
