# seconds in 24 hours
SECONDS_IN_A_DAY = 86400

print("\n=== Time Converter ===")
# get user input
total_seconds = int(input("\nEnter a number of seconds between 1 and 86400: "))

# validate input range
if total_seconds < 1 or total_seconds > SECONDS_IN_A_DAY:
    print("\nError: Number must be between 1 and 86400")
    exit()

# convert to hours, mins, secs
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("\nConverted Time:")
print("--------------")
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
print(f"({hours} hours, {minutes} minutes, and {seconds} seconds)")

# verify conversion by calculating back to seconds
calculated_seconds = hours * 3600 + minutes * 60 + seconds
if calculated_seconds == total_seconds:
    print("\nTest PASSED ✓")
else:
    print("\nTest FAILED ✗")
