import csv
import os
from datetime import datetime
from collections import defaultdict

try:
    from tabulate import tabulate
except:
    tabulate = None

try:
    import matplotlib.pyplot as plt
except:
    plt = None


FILE_NAME = "expenses.csv"


# ---------------- CREATE FILE ----------------

def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Amount",
                    "Category",
                    "Description",
                    "Date"
                ]
            )



# ---------------- ADD EXPENSE ----------------


def add_expense():

    try:

        amount = float(input("Enter amount: "))


        if amount <= 0:

            print("Amount must be positive")
            return



        category = input("Enter category: ")

        description = input("Enter description: ")



        date = input(
            "Enter date (YYYY-MM-DD): "
        )


        datetime.strptime(
            date,
            "%Y-%m-%d"
        )



        with open(FILE_NAME,"a",newline="") as file:


            writer = csv.writer(file)


            writer.writerow(
                [
                    amount,
                    category,
                    description,
                    date
                ]
            )


        print("Expense Added Successfully")



    except ValueError:

        print("Invalid Input")





# ---------------- LOAD DATA ----------------


def load_expenses():

    expenses=[]


    with open(FILE_NAME,"r") as file:


        reader = csv.DictReader(file)


        for row in reader:

            expenses.append(row)



    return expenses






# ---------------- VIEW EXPENSES ----------------


def view_expenses():


    expenses = load_expenses()


    if not expenses:

        print("No expenses found")
        return



    table=[]


    for e in expenses:


        table.append(
            [
                e["Amount"],
                e["Category"],
                e["Description"],
                e["Date"]
            ]
        )


    headers=[
        "Amount",
        "Category",
        "Description",
        "Date"
    ]



    if tabulate:


        print(
            tabulate(
                table,
                headers=headers,
                tablefmt="grid"
            )
        )


    else:

        print(headers)

        for row in table:

            print(row)






# ---------------- FILTER CATEGORY ----------------


def filter_by_category():


    category=input(
        "Enter category: "
    )


    expenses=load_expenses()


    found=False


    for e in expenses:


        if e["Category"].lower()==category.lower():


            print(e)

            found=True



    if not found:

        print("No record found")






# ---------------- FILTER DATE ----------------


def filter_by_date_range():


    start=input(
        "Start date YYYY-MM-DD: "
    )


    end=input(
        "End date YYYY-MM-DD: "
    )


    expenses=load_expenses()



    for e in expenses:


        if start <= e["Date"] <= end:


            print(e)







# ---------------- MONTHLY SUMMARY ----------------


def monthly_summary():


    month=input(
        "Enter month YYYY-MM: "
    )


    data=defaultdict(float)


    expenses=load_expenses()


    total=0



    for e in expenses:


        if e["Date"].startswith(month):


            amount=float(
                e["Amount"]
            )


            data[e["Category"]] += amount


            total += amount





    if total==0:


        print("No data found")

        return





    print("\nMONTHLY SUMMARY")

    print("----------------------")



    for category,amount in data.items():


        percentage=(amount/total)*100



        print(
            f"{category} : ₹{amount} ({percentage:.2f}%)"
        )



    print(
        "\nTotal Spending : ₹",
        total
    )


    create_chart(data)






# ---------------- PIE CHART ----------------


def create_chart(data):


    if plt:


        plt.pie(
            data.values(),
            labels=data.keys(),
            autopct="%1.1f%%"
        )


        plt.title(
            "Expense Distribution"
        )


        plt.show()






# ---------------- CLEAR DATA ----------------


def clear_data():


    confirm=input(
        "Are you sure? (yes/no): "
    )


    if confirm.lower()=="yes":


        with open(FILE_NAME,"w",newline="") as file:


            writer=csv.writer(file)


            writer.writerow(
                [
                    "Amount",
                    "Category",
                    "Description",
                    "Date"
                ]
            )


        print("All expenses deleted")


    else:

        print("Delete cancelled")







# ---------------- MENU ----------------


def menu():


    create_file()


    while True:


        print(
"""
========= EXPENSE TRACKER =========

1. Add Expense

2. View Expenses

3. Filter By Category

4. Filter By Date Range

5. Monthly Summary

6. Clear All Data

7. Exit

===================================
"""
        )



        choice=input(
            "Enter choice: "
        )



        if choice=="1":

            add_expense()



        elif choice=="2":

            view_expenses()



        elif choice=="3":

            filter_by_category()



        elif choice=="4":

            filter_by_date_range()



        elif choice=="5":

            monthly_summary()



        elif choice=="6":

            clear_data()



        elif choice=="7":

            print("Good Bye")

            break



        else:

            print("Invalid Choice")
# RUN PROGRAM

menu()