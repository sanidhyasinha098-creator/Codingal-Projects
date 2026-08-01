import time
import sys

# Helper function for slow typing
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # move to next line after finishing

def Greet_Customer():
    slow_print("\nWelcome to the Art Supplies Billing Tool!\n")
    slow_print("We are here to help you calculate your total bill for art supplies.\n")
    slow_print("Let's get started!\n")

def Thank_Customer():
    slow_print("\nThank you for using the Art Supplies Billing Tool!")
    slow_print("We hope you have a great day and enjoy your art supplies!")

# Call greeting with typing effect
Greet_Customer()

Art_Supplies = ["Art Book", "Paint Set", "Brush Set", "Canvas", "Sketch Pad", "Palette", "Charcoal Pencils", "Watercolor Paper", "Acrylic Paints"]
print("Available Art Supplies: \n",Art_Supplies)

user_input = input("\nPlease enter the name of the art supply you would like to purchase: ")
user_input_2 = float(input("Please enter the price of the art supply: ₹"))
user_input_3 = int(input("Please enter the quantity of the art supply you would like to purchase: "))

def calculate_total(user_input_2, user_input_3):
    Subtotal = user_input_2 * user_input_3
    Tax = Subtotal * 0.18  # 18% Tax
    Grand_Total = Subtotal + Tax
    return Subtotal, Tax, Grand_Total

print("----------------------------------------------------------------")
print("Item: ", user_input)
print("Price:  P₹", user_input_2)
print("Quantity: ", user_input_3)
print("----------------------------------------------------------------")
Subtotal, Tax, Grand_Total = calculate_total(user_input_2, user_input_3)
print("Subtotal:  ₹", f"{Subtotal:.2f}")
print("Tax (18%):  ₹", f"{Tax:.2f}")
print("Grand Total:  ₹", f"{Grand_Total:.2f}")

# Call thank-you with typing effect
Thank_Customer()
