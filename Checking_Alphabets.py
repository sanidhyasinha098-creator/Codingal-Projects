#-----------------------------------------
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#-----------------------------------------
while True:
    user_input = input("Please enter the Alphabet Letter (or type 'exit'): ")

    if user_input.lower() == "exit":
        exit()
#-----------------------------------------
    elif user_input in Alphabet:
        print("Valid input")
    else:
        print("Invalid input")

#Please check Checking_Alphabets_Output.png for the output of this code.