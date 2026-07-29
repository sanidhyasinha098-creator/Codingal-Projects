print("Welcome to the Genuine Grocery Store.")

Low_Price = 0
Med_Price = 0
High_Price = 0

Customers_Served = 0
Total_Sales = 0

Billing = True

while Billing:
    Name = input("Please enter your name: ")
    Items = int(input("Hello {}! How many grocery items have you purchased? ".format(Name)))
    
    if Items <= 0:
        print("Invalid item count. Please enter a positive number...")
        continue

    purchased_items = []  # store all items first
    Customer_Subtotal = 0
    Customer_Tax = 0

    for i in range(Items):
        Item_Name = input("Enter item name: ")
        Item_Price = float(input("Enter item price: "))
        Item_Qty = int(input("Enter item Quantity: \n"))

        if Item_Price <= 0 or Item_Qty <= 0:
            print("Invalid price or quantity. Please re-enter...")
            continue

        SubTotal = Item_Price * Item_Qty
        Tax = SubTotal * 0.05

        purchased_items.append((Item_Name, Item_Qty, Item_Price, SubTotal, Tax))

        Customer_Subtotal += SubTotal
        Customer_Tax += Tax

        if Item_Price < 50:
            Low_Price += Item_Qty
        elif Item_Price <= 100:
            Med_Price += Item_Qty
        else:
            High_Price += Item_Qty

    Customer_Total = Customer_Subtotal + Customer_Tax
    Customers_Served += 1
    Total_Sales += Customer_Total

    # Now print the full receipt AFTER collecting items
    print("\n" + "=" * 76)
    print("       Genuine Grocery Store")
    print("=" * 76)
    print("Customer: {}".format(Name))
    print("-" * 76)

    for item in purchased_items:
        Item_Name, Item_Qty, Item_Price, SubTotal, Tax = item
        print("Item: {}    Qty: {}    Price: {:.2f}    Subtotal: {:.2f}    Tax: {:.2f}".format(
            Item_Name, Item_Qty, Item_Price, SubTotal, Tax))

    print("-" * 76)
    print("Subtotal : {:.2f}".format(Customer_Subtotal))
    print("Tax      : {:.2f}".format(Customer_Tax))
    print("Total    : {:.2f}".format(Customer_Total))
    print("-" * 76)

    thank_you = "Thank you for shopping with us!"
    print(thank_you.center(76))

    print("=" * 76 + "\n")

    again = input("Next customer? (yes/no): ").strip().lower()
    if again != "yes":
        Billing = False

# Final report
print("\n=== Grocery Category Report ===")
print("Low price items   : {} {}".format(Low_Price, "*" * Low_Price))
print("Medium price items: {} {}".format(Med_Price, "*" * Med_Price))
print("High price items  : {} {}".format(High_Price, "*" * High_Price))

print("\nCustomers served : {}".format(Customers_Served))
print("Total sales      : {:.2f}".format(Total_Sales))
print("Grocery billing closed. Goodbye!")