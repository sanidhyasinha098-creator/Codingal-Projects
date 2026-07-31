print("=========== Star Pyramid ===========")
rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
    print()

#Activity 2
print("=========== Floyd's Triangle ===========")
rows_2 = int(input("Enter the numbers of rows: "))
number = 1

for i in range(1, rows_2):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()

#Activity 3
print("=========== Diamond number pattern ===========")
rows_3 = int(input("Enter the numbers of Diamond row size: "))

if rows_3 % 2 == 0:
    half_rows = rows_3 // 2
else:
    half_rows = rows_3 // 2 + 1

space = half_rows - 1

for i in range(1, half_rows + 1):
    for j in range(1, space + 1):
        print(" ", end="")
 
    space -= 1
    number = 1
 
    for j in range(2 * i - 1):
        print(number, end="")
        number += 1
 
    print()
 
space = 1
 
for i in range(1, half_rows):
    for j in range(1, space + 1):
        print(" ", end="")
 
    space += 1
    number = 1
 
    for j in range(1, 2 * (half_rows - i)):
        print(number, end="")
        number += 1
 
    print()

print("" \
"=========== LOOP ART DESIGN COMPLETE ===========")
print("You created Star, Triangle, and Diamond pattern using nested loops!")    


    