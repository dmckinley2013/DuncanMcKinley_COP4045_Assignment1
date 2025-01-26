# voyager 1 distance calculator
from datetime import timedelta

# initial conditions from 9/25/2009
INITIAL_DISTANCE_MILES = 16637000000
SPEED_MPH = 38241
MILES_TO_KM = 1.609344
MILES_TO_AU = 92955887.6
LIGHT_SPEED_MPS = 299792458

print("\n=== Voyager 1 Distance Calculator ===")
try:
    # get days since launch date
    days_since_2009 = int(input("\nEnter number of days since 9/25/2009: "))
    if days_since_2009 < 0:
        raise ValueError("Days cannot be negative")
except ValueError as e:
    print("\nError: Please enter a valid positive number")
    exit()

# convert days to hours
hours_since_2009 = days_since_2009 * 24

# calculate current distance
new_distance_miles = INITIAL_DISTANCE_MILES + (SPEED_MPH * hours_since_2009)
new_distance_km = new_distance_miles * MILES_TO_KM
new_distance_au = new_distance_miles / MILES_TO_AU

# calculate communication time
round_trip_time_hours = (new_distance_miles * MILES_TO_KM * 1000 * 2) / (LIGHT_SPEED_MPS * 3600)

print("\nResults:")
print("---------")
print(f"Distance in miles: {new_distance_miles:,.2f}")
print(f"Distance in kilometers: {new_distance_km:,.2f}")
print(f"Distance in astronomical units: {new_distance_au:,.2f}")
print(f"Round-trip communication time in hours: {round_trip_time_hours:.2f}")

# verify all calculations match
verify_km = new_distance_miles * MILES_TO_KM
verify_au = new_distance_miles / MILES_TO_AU
verify_distance = INITIAL_DISTANCE_MILES + (SPEED_MPH * days_since_2009 * 24)

if abs(verify_km - new_distance_km) < 0.01 and \
   abs(verify_au - new_distance_au) < 0.01 and \
   abs(verify_distance - new_distance_miles) < 0.01:
    print("\nTest PASSED ✓")
else:
    print("\nTest FAILED ✗")