# Return sum of the two numbers

class add:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def add_number( self,a, b):
          c = a + b
          print(f"The sum of {a} and {b} is {c} ")

a = int(input("Enter the value of first number"))
b = int(input("Enter the value of second number"))
obj = add(a,b) # making object for class
obj. add_number(a,b)
