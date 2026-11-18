expenses = []
print("welcome to the expense Tracker.")

while True: 
    print("===== Menu: =====")
    print("1. Add Expense:")
    print("2. View All Expense:")
    print("3. View Total Expense:")
    print("4. Exit:")

    choice = int(input("Enter Your choice:"))

    if(choice == 1):

        date=input("Enter The Date Of Expense:")
        category=input("Enter The Category Of Expense:")
        discription=input("Enter The Discription Of Expense:")
        amount=float(input("Enter The Amount Of Expense:"))

        expense = {
            "date":date,
            "category":category,
            "discription":discription,
            "amount":amount
        }

        expenses.append(expense)
        print("\n Expenses is added successfully.")

    elif(choice == 2):
        if(len(expenses)==0):
            print("No Expenses Added.")
        else:
            print(" ===== This Is All Expenses: ===== ")
            count = 1
            for eachkharcha in expenses:
                print(f"Expenses No. {count} -> {eachkharcha["date"]}, {eachkharcha["category"]}, {eachkharcha["discription"]}, {eachkharcha["amount"]} ")
                count = count + 1

    elif(choice == 3):
        total = 0
        for eachkharcha in expenses:
            total = total + eachkharcha["amount"]
        print("\n Total Amount = ", total)

    elif(choice == 4):
        print("Thank you for use this system.")
        break

    else:
        print("Invalid Choice. Try Again")




