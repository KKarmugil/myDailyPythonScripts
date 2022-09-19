# Return the Remainder from Two Numbers
class rem:
  def __init__(self,num,den):
    self.num=num
    self.den=den

  def reminder(self,num,den):
      rem = num % den
      print(rem)

num=10
den=2
obj = rem(num,den)   #  creating object for class
obj.reminder(num,den)
