#Activity 1
w = 1
h = 9
s = 6
m = 2
c = 6
d = 3
t = 4

z = (w+5) * (h / s)
print ("The Answer of w+5 x h/s is: ", z)


name = "Sanidhya"
age = 9

if name == "Sanidhya" or name == "Romit" and age >= 9:
    print("Hello, Welcome")
else:
    print("Sorry, You are not allowed to enter")

numn = int(input("Enter a number (Numerator): "))
numd = int(input("Enter a number (Denominator): "))

if numn % numd == 0:
    print("The number is divisible")
else:
    print("The number is not divisible")


#Activity 2
mean1 = 36
wrong_num = 68
correct_num = 58
total_num = 100

sum = mean1 * total_num
num2 = sum - ((wrong_num - correct_num))
print("sum - ((wrong_num - correct_num)): ", num2)


#Activity 3
A = int(input("Enter a value: "))
B = int(input("Enter value 1: "))
C = int(input("Enter value 2: "))

avg = (A + B + C) / 3

if avg > A and avg > B and avg > C:
    print("Avg is greater than A, B and C")
elif avg > A and avg > B:
    print("Avg is greater than A and B")
elif avg > A and avg > C:
    print("Avg is greater than A and C")
elif avg > B and avg > C:
    print("Avg is greater than B and C")
else:
    print("Avg is not grater than any of the values 'A, B, C'")
