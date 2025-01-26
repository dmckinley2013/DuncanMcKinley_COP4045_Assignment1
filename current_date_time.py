# get current date and time using datetime
from datetime import datetime

# get current time
now = datetime.now()

# format date/time as string
formatted_date_time = now.strftime("%m/%d/%Y %H:%M:%S")

print(f"Current date and time: {formatted_date_time}")

print("\nTest Case:")
print("Input:")
print("- Current system time")
print("Expected Format:")
print("- MM/DD/YYYY HH:MM:SS (e.g., 07/04/2024 12:30:33)")
print(f"Actual Output: {formatted_date_time}")

# verify date format is valid
try:
    datetime.strptime(formatted_date_time, "%m/%d/%Y %H:%M:%S")
    print("Test Result: PASSED - Date format is correct")
except ValueError:
    print("Test Result: FAILED - Date format is incorrect")