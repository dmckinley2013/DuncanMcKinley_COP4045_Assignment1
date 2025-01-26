# calculate depth if great lakes water spread across US
GREAT_LAKES_VOLUME_KM3 = 22810
CONTIGUOUS_US_AREA_KM2 = 8080464

# calculate average depth
depth_km = GREAT_LAKES_VOLUME_KM3 / CONTIGUOUS_US_AREA_KM2

print(f"The average depth of the Great Lakes water spread across the contiguous U.S. is {depth_km:.6f} km.")

print("\nTest Case:")
print(f"Input:")
print(f"- Great Lakes Volume: {GREAT_LAKES_VOLUME_KM3} km³")
print(f"- Contiguous US Area: {CONTIGUOUS_US_AREA_KM2} km²")
print(f"Expected Output: ~0.002822 km depth")
print(f"Actual Output: {depth_km:.6f} km depth")

# verify calculation matches expected value
print(f"Test Result: {'PASSED' if abs(depth_km - 0.002822) < 1e-6 else 'FAILED'}")