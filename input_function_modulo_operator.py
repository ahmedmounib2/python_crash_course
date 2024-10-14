# input function
prompt = 'if you tell us who you are, we can personalize the message you see.'
prompt += "\nwhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}")

age= input('how old are you? ')
age= int(age)
if age >= 18:
    print(f"\nyour age is {age}, you are older than 18, you are allowed to join")
else:
    print("\nsorry you are less than legal age")


height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# The Modulo Operator
# A useful tool for working with numerical information is the modulo operator
# (%), which divides one number by another number and returns the
# remainder:
# >>> 4 % 3
# 1
# >>> 5 % 3
# 2
# >>> 6 % 3
# 0
# >>> 7 % 3
# 1
# The modulo operator doesn’t tell you how many times one number fits
# into another; it just tells you what the remainder is.
# When one number is divisible by another number, the remainder is 0, so
# the modulo operator always returns 0. You can use this fact to determine if a
# number is even or odd:
number= input("Enter a number and i wqill tell you if its evewn or odd: ")
number= int(number)

if number %2 == 0:
    print(f"\n{number} is an even number")
else:
    print(f"\n{number} is an odd number")

# Even numbers are always divisible by two, so if the modulo of a number
# and two is zero (here, if number % 2 == 0) the number is even. Otherwise, it’s
# odd.

