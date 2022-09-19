# Return a String as an Integer
class coversion:
  def __init__(self,string):
      self.string=string


  def type_conversion( self,string):
      print(int(string))
      print(type(int(string)))


string = input("Enter the string")
obj = coversion(string)    # making object for class
obj.type_conversion(string)
