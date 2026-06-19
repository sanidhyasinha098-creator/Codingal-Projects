while True:
    user_input = input("Please enter the Temperature Outside (or type 'exit'): ")

    if user_input.lower() == "exit":
        exit()

    Weather_Input = int(user_input)

    if Weather_Input < 10:
        print("Wear Jacket, It's Cold Outside\n") 
    elif Weather_Input >= 10 and Weather_Input < 16:
        print("Wear a Light Jacket, It's Cool Outside\n")
    else:
        print("No Jacket is Required\n")

