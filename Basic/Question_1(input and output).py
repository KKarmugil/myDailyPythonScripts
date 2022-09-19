hr = int(input("Enter the hours: "))
if (hr>24):
    print("Invalid input")
else:
    sec = hr*60*60
    print(f"In {hr} hours {sec}  seconds are  present")