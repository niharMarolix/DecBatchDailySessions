# print(f"name entered is {name} and age entered is {age}")

'''
take input from user:
inputs should be name and age
if age is greater than or equal to 18 print "eligible to vote",
else print "not eligible, sit home eat rice"

+,-,/,*,>,<,>=,<=
'''

name = input("Please enter your name: \n")
age = int(input("Enter your age as well: \n"))

if age<=0:
    print("Enter a valid age")
elif age>=18:
    print(f"{name} eligible to vote")
else:
    print(f"{name} is not eligible, sit home eat rice")