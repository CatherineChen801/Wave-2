print("Full name of the month and capitalization of the first letter is required.\n")
print("Please make sure the spelling is correct.\n")
month = input('Enter the name of the month: ')
if month == "February":
    print("There are 28 or 29 days in this month.")
elif month in ("April", 'June', 'September', 'November'):
    print('There are 30 days in this month.')
else:
    print('There are 31 days in this month.')