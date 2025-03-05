from datetime import datetime
import re
import sys
import os

expenses = []

try:
    file_path = sys.argv[1]
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                if line.startswith("Expense"):
                    # Initialize a dictionary to store the current expense
                    expense = {}
                elif line.startswith("- Amount:"):
                    expense["Amount"] = int(line.split(":")[1].strip())
                elif line.startswith("- Category:"):
                    expense["Category"] = line.split(":")[1].strip()
                elif line.startswith("- Date:"):
                    expense["Date"] = line.split(":")[1].strip()
                    # Add the expense to the list
                    expenses.append(expense)
    else:
        create_file = input("File not found. Would you like to create one? (Y/N): ").upper()
        if create_file == "Y":
            with open(file_path, "w"):
                print("File created.")
        else:
            sys.exit("Exiting...")
except Exception as e:
    print(f"Error: {e}")
    sys.exit("File not found.")


while True:
    try:
        option = int(input("""
                            Choose a task from the list below:
                            1. Add expense
                            2. View expenses
                            3. View summary
                            4. Exit
                            """))
        match option:
            case 1:
                while True:
                    while True:
                        try:
                            amount = int(input("Enter the amount: "))
                            if amount <= 0:
                                print("Amount cannot be negative or zero")
                                continue
                            break
                        except ValueError:
                            print("Invalid input. Try a positive number...")

                    category = input("Enter the category: ")

                    while True:
                        try:
                            date = input("Enter the date (YYYY-MM-DD): ")
                            match = re.match(r"(\d{4}).?(\d{2}).?(\d{2})", date)
                            year, month, day = match.group(1), match.group(2), match.group(3)
                            if int(month) > 12 or int(day) > 31:
                                print("Invalid input. Try values within valid ranges")
                                continue
                            break
                        except Exception as e:
                            print(f"Error is: {e}")

                    expenses.append({"Amount":amount, "Category":category, "Date":date})
                    add_another = input("Press 'Y' to add another expense or any key to return to main menu: ").upper()
                    if add_another == "Y":
                        continue
                    break
                    
            case 2:
                filter = input("Enter the filter name: ")

                def func(count, dic):
                    print(f"Expense {count+1}")
                    print(f"- Amount: ${dic['Amount']}")
                    print(f"- Category: {dic['Category']}")
                    print(f"- Date: {dic['Date']}")

                if filter:
                    for i, item in enumerate(expenses):
                        if filter not in item.values():
                            continue
                        func(i, item)
                else:
                   for i, item in enumerate(expenses):
                       func(i, item)

            case 3:
                total = 0
                for item in expenses:
                    total += item["Amount"]
                print(f"Total Spending: {total}")
                for item in expenses:
                    print(f"- {item['Category']}: ${item['Amount']}")
            case 4:
                with open(file_path, "w") as file:
                    for i, item in enumerate(expenses):
                        file.write(f"Expense {i+1}" + "\n")
                        for key in item.keys():
                            file.write(f"- {str(key)}:{str(item[key])}" + "\n")
                sys.exit("Exiting...")
         
    except ValueError:
        print("Invalid choice. Choose from the list...")
        continue
    








