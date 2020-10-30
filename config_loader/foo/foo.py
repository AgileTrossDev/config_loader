def create_foo(config):
    return Foo(config.p1,config.p2,config.p3)

class Foo:
  def __init__(self, i, j, k):
    self.p1 = i
    self.p2 = j
    self.p3 = k



  def disp(self):
      print(f"P1: {self.p1} P2: {self.p2} P3: {self.p3}")  
