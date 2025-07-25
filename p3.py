import json
try:
    with open("expenses.json","r") as f:
        expenses = json.load(f)
except FileNotFoundError:
    expenses = [
  {"amount": 250, "category": "Food", "note": "Lunch"},
  {"amount": 1200, "category": "Transport", "note": "Cab to airport"},
]
def save_data():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=2)   

menu = ["Add Expense","View Expense","View Summary","Delete Expense","Exit"]
print("------ Welecome to Expense Tracker ------")
print()
for i,option in enumerate(menu):
    print(f'{i + 1}. {option}')
def view_expense():
    if not expenses:
        print("No expenses added yet.")
    else:
        for i,expense in enumerate(expenses):
            print(f'{i+1}. ₹{expense["amount"]} | {expense["category"]} | {expense["note"]}')
while True:
    option = input("Enter Option No (1-5): ")
    try:
        option = int(option)
        if option <= 0 or option >= 6:
            print("Out of range!, Try again.")
        else:
            if option == 1:
                flag= False
                print("You chose: Add Expense")
                while True:
                    amount = input("Enter the amount: ")
                    try:
                        amount = float(amount)
                        cate = input("Enter the Category: ")
                        note = input("Note(Optional) :")
                        expense = {"amount": amount, "category": cate,"note":note}
                        expenses.append(expense)
                        print(expenses)
                        print("Added Successfully!")
                        save_data()
                        again = input("Enter again ?(Y/N): ").lower()
                        if again == 'y':
                            continue
                        else:
                            break
                    except:
                        print("Don't enter strings!")
            elif option == 2:
                print("You chose: View Expense")
                print("-------- All Expenses -------")
                view_expense()
            elif option == 3:
                print("You chose: View Summary")
                print("-------- Expenses Summary -------")
                if not expenses:
                    print("No expenses to summarize.")
                else:
                    total = sum(exp["amount"] for exp in expenses)
                    print(f"Total Expenses: {total}")
                    cat_summary={}
                    for exp in expenses:
                        cat =exp["category"]
                        amt =exp["amount"]
                        if cat in cat_summary:
                            cat_summary[cat] += amt
                        else:
                            cat_summary[cat] = amt
                    for cat,amt in cat_summary.items():
                        print(f'-{cat}: ₹{amt}')
            elif option == 4:
                print("You chose: Delete Expense")
                print("-------- Delete Expense -------")
                view_expense()
                del_number = input("Enter a number to delete: ")
                try:
                    del_number = int(del_number)-1
                    if del_number <0 or del_number > len(expenses):
                        print("Out of Range!")
                    else:
                        deleted_exp = expenses[del_number]
                        del expenses[del_number]
                        print(f'Deleted: {deleted_exp["amount"]} | {deleted_exp["category"]} |{deleted_exp["note"]}')
                        save_data()
                except:
                    print("Enter a number to Delete, Not as string!")
            elif option == 5:
                print("You chose: Exit")
                print("Exit Successfuly!")
                break
            else:
                print("Error !, try again")
    except:
        print("Don't Enter Strings or float")

