'''
imagine you are a recuitment specialist and you need
to hire canfifates based on 5 factors, from which
at least 3 should be satisfied

factors are:

age> 21
experience > 4
telugu = True
nationality = Indian
nightShift = True
'''

noOfFactors = 0

age = int(input("Enter your age as well: \n"))
experience = int(input("Enter your experience as well: \n"))
isLanguageTelugu = input("Is you language Telugu: \n")
nationality = input("Enter your nationality: \n")
areYouAvailableForNightShift = input("Enter your avaibility: \n")


if age > 21:
    noOfFactors = noOfFactors + 1
if experience>4:
    noOfFactors = noOfFactors + 1
if bool(isLanguageTelugu) == True:
    noOfFactors = noOfFactors + 1
if nationality == "Indian":
    noOfFactors = noOfFactors + 1
if bool(areYouAvailableForNightShift) == True:
    noOfFactors = noOfFactors + 1
print("----------------------------------------------------------")
print("After evaluation")
print("----------------------------------------------------------")
if noOfFactors>=3:
    print("candidate is eligible")
else:
    print("Not eligible")