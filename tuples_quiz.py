# if statements to check for conditions
cars= ['audi', 'toyota', 'subaru', 'mercedes', 'bmw', 'hyundai']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
name = 'ahmed' # one = sign sets the value for a variable
name == 'ahmed'  # 2 == signs checks if its true or false, it asks a question if its true or false and is case sensitive
# to ignore case sensitivity run the test as below
name= 'Ahmed'
name== 'ahmed'
#false

name='Ahmed'
name.lower()== 'ahmed'
#true

#inequality operator to check if the value is not equal to (!=) like the example below
pizza_topping = 'mushrom'
if pizza_topping != 'anchovies': #if pizza topping not equal to
    print("hold the anchovies\n")


answer = 17
if answer != 42:
    print("this is not a correct answer. please try again \n")

# age = 19
# age < 21
# true
# age<= 21 #age less than or equal to
# age> 21 # Each mathematical comparison can be used as part of an if statement which can help you detect the exact conditions of interest.

# checking for multiple conditions using (and) , (or)

# age_0 = 22
# age_1 = 18
# age_0 >= 21 and age_1 >= 21
# false

# age_1 = 22
# age_0 >= 21 and age_1 >= 21
#true
# we can use parentheses to improve readability but it doesnt affect the result like below
# (age_0 >= 21) and (age_1 >= 21)

# we can use (or) to check for more than 1 condition but both of them must e true as below

# age_0 = 22
# age_1 = 18
# age_0 >= 21 or age_1 >= 21
#true

# age_0 = 18
# age_0 >= 21 or age_1 >= 21
# false

# cheking whether a certain value is in a list with (in)
# requested_toppins= ['onion','tomato','cheese',' olives', 'mushrooms']
# 'mushrooms' in requested_toppins
# true
# 'pepperoni' in requested_toppins
# false

# checking if a value is not in a list by using (not)
banned_user = ['andrew','maria','john']
user= 'sara'
if user not in banned_user:
    print(f"{user.title()},you can post a response if you wish.")

# boolean expression test if (True or False)

car = 'subaru'
print("is car== 'subaru', i predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print( car== 'audi')
