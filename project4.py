#Jennifer Gonzales
#SP23-CIT-134A-201
#Project 4
SALES_FILE = "monthly_sales.txt"
def read_file(dictionary):
    with open(SALES_FILE, 'r') as f:
        for line in f:
            month, sales = line.split()
            dictionary[month.lower()] = float(sales)
            
def write_file(dictionary):
    with open(SALES_FILE, 'w') as f:
        for month, sales in dictionary.items():
            f.write(month.capitalize() + ' ' + str(sales) + '\n')
            
def view_sales_amount(dictionary):
    month = input('Three-letter month: ').lower()
    if month in dictionary:
        amount= dictionary[month]
        print("Sales amount for {:s} is ${:,.2f}.".format(month.capitalize(), amount))
    else:
        print('Invalid three-letter month. Try again')

def get_highest_amount(dictionary):
    max_month, max_sales = max(dictionary.items(), key=lambda x: x[1])
    print("The highest sales amount is ${:,.2f} in {:s}".format(max_sales, max_month.capitalize()))

def get_lowest_amount(dictionary):
    min_month, min_sales = min(dictionary.items(), key=lambda x: x[1])
    print("The lowest sales amount is ${:,.2f} in {:s}".format(min_sales, min_month.capitalize()))

def edit_sales_amount(dictionary):
    month = input('Three-letter month: ').lower()
    if month in dictionary:
        amount = float(input('Sales amount: '))
        dictionary[month] = amount
        write_file(dictionary)
        print("Sales amount of ${:,.2f} for {:s} has been updated".format(amount, month.capitalize()))
    else:
        print('Invalid three-letter month. Try again')

def get_average(dictionary):
    total_sales = sum(dictionary.values())
    average_sales = total_sales / len(dictionary)
    print("Monthly average is ${:,.2f}".format(average_sales))

def get_range_average(dictionary):
    low = float(input('Low: '))
    high = float(input('Hi: '))
    sales_in_range =[sales for sales in dictionary.values() if low<= sales <= high]
    if not sales_in_range:
        print('No sales in the range')
    else:
        range_average = sum(sales_in_range) / len(sales_in_range)
        print("Sales average of this range is ${:,.2f}".format(range_average))

def get_total(dictionary):
    total = sum(dictionary.values())
    print("Yearly total is ${:,.2f}".format(total))

def terminate_app():
    print('Thank you for using my app!')
    exit(0)

def main():
    dictionary = {}
    read_file(dictionary)
    print('Product Sales Management System\n')
    while True:
        print("Command Menu")
        print("view - View a sales amount for a specified month")
        print("highest - View the highest sales of the year")
        print("lowest - View the lowest sales of the year")
        print("edit - Edit a sales amount for a specified month")
        print("average - View the sales average for the whole year")
        print("range - View the sales average for a specified sales amount range")
        print("total - View the sales total for the whole year")
        print("exit - Exit the program\n")
        command = input("Command: ").lower()
        print()
        if command== "view":
            view_sales_amount(dictionary)
        elif command == "highest":
            get_highest_amount(dictionary)
        elif command == "lowest":
            get_lowest_amount(dictionary)
        elif command == "edit":
            edit_sales_amount(dictionary)
        elif command == "average":
            get_average(dictionary)
        elif command == "range":
            get_range_average(sales)
        elif command == "total":
            get_total(sales)
        elif command == "exit":
            terminate_app()
        else:
            print("Invalid command. Try again.")
 