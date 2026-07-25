Total_Homework = 4
Original_Count = Total_Homework
print("You have {} homework tasks to complete today!\n".format(Original_Count))

Completed_Count = 0
Task_num = 1

while Task_num <= Total_Homework:
    if Task_num == 1:
        Next_Task = "Math Worksheet"
    elif Task_num == 2:
        Next_Task = "English Essay writing"
    elif Task_num == 3:
        Next_Task = "SST Reading"
    elif Task_num == 4:
        Next_Task = "Science Lab Report"

    user_input = input("Have you completed {}? (Y/N): ".format(Next_Task)).lower()

    if user_input == "y":
        Completed_Count += 1
        Task_num += 1
        print("Great job! You have completed {} out of {} homework tasks.\n".format(Completed_Count, Original_Count))
    else:
        print("No worries! You still have {} homework tasks to complete.\n".format(Original_Count - Completed_Count))

print("================== ALL HOMEWORK'S COMPLETED! ==================")
print("You have completed {} out of {} homework tasks. Well done!\n".format(Completed_Count, Original_Count))

print("Now let's safely peek at a infinite Loop.....")
test_val = 0
safety_val = 0

while test_val <= 0:
    print("This is an infinite loop! Be careful!")
    safety_val += 1
    if safety_val > 5:
        print("Safety break activated! Exiting the loop....")
        break