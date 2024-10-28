import calendar
def display_calendar(year, rows, columns):
    if rows * columns < 12:
        print("Error: Rows and columns are not enough to display all 12 months.")
        return
    month_calendars = [calendar.month(year, month) for month in range(1, 13)]
    for i in range(0, len(month_calendars), columns):
        for j in range(6):  
            for k in range(columns):
                month_index = i + k
                if month_index < 12:
                    line = month_calendars[month_index].splitlines()[j]
                    print(line.ljust(20), end=" ")
            print() 
        print()  
year = int(input("Enter the year: "))
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
display_calendar(year, rows, columns)
