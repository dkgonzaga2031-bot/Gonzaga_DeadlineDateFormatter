#import the library
from datetime import datetime

# contains basic input and output
event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# 2. Create a date object using the datetime module
event_date = datetime(year, month, day)

# 3. Format the outputs
formatted_title = event_title.upper()
readable_date = event_date.strftime("%B %d, %Y").replace(" 0", " ")
month_name = event_date.strftime("%B")
weekday_name = event_date.strftime("%A")

# 4. Display the formatted output
print("\nFormatted Output:")
print(f"Event: {formatted_title}")
print(f"Date: {readable_date}")
print(f"Year: {year}")
print(f"Month: {month_name}")
print(f"Day: {day}")
print(f"Weekday: {weekday_name}")
