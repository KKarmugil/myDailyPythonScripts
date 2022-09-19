# Return the Remainder from Two Numbers
def reminder(num,dem):
    rem = num % den
    return rem
num = int(input('Enter the numerator'))
den = int(input('Enter the denominator'))

print(f"Th reminder of {num} and {den} is:",reminder(num,den)) # function call in print statement
