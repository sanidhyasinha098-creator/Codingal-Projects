user_input = int(input("Enter a number: "))
power = int(input("Enter the power to raise the number to: "))

for i in range(power):
    result = user_input ** (i + 1)
print("{} raised to the power of {} is: {}".format(user_input, i + 1, result))
