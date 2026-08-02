import time
import sys

def slow_print(text, delay=0.025):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
#-------------------------------------------------------------------------------------------------------        
def Total_Bill(Bill_Amount, Tip_Percentage):
    TTL_Bill = Bill_Amount * (1 + 0.01 * Tip_Percentage)
    TTL_Bill = round(TTL_Bill, 2)
    slow_print(f"Total Bill Amount (including tip): ${TTL_Bill}\n")
    return TTL_Bill

Total_Bill(150, 20)
#-------------------------------------------------------------------------------------------------------
def Seating_Arrangement(Guests):
    '''The function "Seating_Arrangement" takes a list of guests and returns a seating arrangement.\n'''
    if Guests == 0 or Guests == 1:
        return 1

    else:
        return Guests * Seating_Arrangement(Guests - 1)
    
slow_print(Seating_Arrangement.__doc__)

slow_print("\n")
slow_print("Seating Arrangement for 1 Guest: ")
slow_print(str(Seating_Arrangement(1)))
slow_print("\n")
slow_print("Seating Arrangement for 2 Guests: ")
slow_print(str(Seating_Arrangement(2)))
slow_print("\n")
slow_print("Seating Arrangement for 3 Guests: ")
slow_print(str(Seating_Arrangement(3)))
slow_print("\n")
slow_print("Seating Arrangement for 5 Guests: ")
slow_print(str(Seating_Arrangement(5)))