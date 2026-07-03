while True:
    num_2 = input("Enter Second Number: ")
    num_1 = input("Enter First Number: ")
    num_3 = input("Enter Third Number: ")
  
    if not num_2.isdigit() or not num_1.isdigit() or not num_3.isdigit():
        print("This is not a number, try again.\n")
        continue

    print("\nBefore Swapping, Check this:")
    print("Second Number:", num_2)
    print("First Number:", num_1)
    print("Third Number:", num_3)

    userinput = input("Is this correct? Press Y to continue or N to type again... :")

    if userinput.upper() == "Y":
        # Do the swap
        num_2, num_1, num_3 = num_1, num_2, num_3

        print("\nAfter Swapping:")
        print("First Number:", num_1)
        print("Second Number:", num_2)
        print("Third Number:", num_3)
        break

    elif userinput.upper() == "N":
        continue
    else:
        print("Invalid input. Please enter Y or N.")
        continue
