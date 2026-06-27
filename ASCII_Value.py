while True:
    ASCII_Input = input("Enter a ASCII Character: ")

    if type(ASCII_Input) == str and len(ASCII_Input) == 1:
        print("Valid Input")
    else:
        print("Invalid Input, Please enter a single character")
        continue
    
    ASCII_Value = ord(ASCII_Input)

    type(ASCII_Value)
    
   
    print(f"The ASCII Value of the character '{ASCII_Input}' is {ASCII_Value}")