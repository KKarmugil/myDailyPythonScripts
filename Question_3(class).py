# Return the Next Number from the Integer Passed
class Next:
  def __init__(self,n):
    self.n=n

  def number(self,n):
    n = n + 1
    print(n)

n = int(input('Enter the number'))
obj = Next(n)   # making object for class
obj. number(n)

