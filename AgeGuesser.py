#Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

#Here are a few instructions that you must have to follow:

#Do not use any type of module like DateTime or date utils. (-5 points)
#Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
#Provide user with their age after 100 years      (2points)
#Your code should handle all sorts of errors like :            (2 points)
# 1)You are not yet born
# 2)You seem to be the oldest person alive
# 3)You can also handle any other errors, if possible!


yearAge = int(input("What is your Age/Year of birth\n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if(yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()

if(yearAge>2022):
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2022 - yearAge

print(f"Your Current AGE Is {2022 - yearAge}")

print(f"You will be 100 years old in {yearAge + 100}")

InterestedYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {InterestedYear - yearAge} years old in {InterestedYear}")