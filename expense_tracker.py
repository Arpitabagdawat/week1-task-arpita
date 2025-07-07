expenses = []

# function to add Expense
def add_expense():
    description = input("Enter item name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expense = {"description": description, "amount": amount, "category": category}

    expenses.append(expense)
    print("Expense added successfully !\n")

#  function to view all expense
def view_expenses():
    if not expenses:
        print("No expenses found yet.\n ")
        return
    print("\n Expense List:")
    
    for idx, exp in enumerate(expenses):
        print(f"{idx+1}.{exp['description']} - Rs. {exp['amount']} ({exp['category']})")
    print() 

# Function for delete an expense
def delete_expense():
    view_expenses()
    if not expenses:
        return
    
    try:
        index = int(input("Enter the number of the expense you want to delete:")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            print(f"Deleted:{removed['description']} - Rs {removed['amount']}")

        else:
            print(" Invalid number. Try again.")
    except ValueError:
        print("Please enter a valid number.")

    print()

# Function to show total category-wise summary
def show_summary():
    if not expenses:
        print("No expenses to summarize.\n")
        return
    total = sum(exp['amount'] for exp in expenses)
    print(f"\n Total Spent: Rs {total}")
    print("Category-wise Summary:")

    category_totals = {}
    for exp in expenses:
        cat = exp['category'] 
        category_totals[cat] =  category_totals.get(cat, 0) + exp['amount']

    for cat, amt in category_totals.items():
        print(f" {cat}: Rs{amt}")
    
    print()

# Main menu to run the tracker
def main():
    while True:
        print("\n Personal Expense Tracker ")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5):")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            print(" Thanks For Using The Expense Tracker \n Goodbye!")

            break
        else:
            print(" Invalid choice. Please try again.\n")

main()


