class Second:                                        # class
  def __init__(self,hr):                             #cuns   
    self.hr=hr

  def second(self,hr):
      if (hr > 24):
          print("Invalid input")
      else:
          sec = hr * 60 * 60
          print(f"In {hr} hours {sec}  seconds are  present")

hr=int(input('Enter the hours:'))

obj = Second(hr)  #making object for class
obj. second(hr)

