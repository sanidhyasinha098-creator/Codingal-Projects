
try:
    Age_Checker = int(input("Please enter your age: "))

    if Age_Checker >= 10 and Age_Checker <= 20:
     print("You are old enough to use this program.")
    elif Age_Checker <= 9:
     print("You are not old enough to use this program.")
    else:
     print("You are too old to use this program.")
    

except ValueError:
    print("Please enter a valid number for your age. Try again.")
    