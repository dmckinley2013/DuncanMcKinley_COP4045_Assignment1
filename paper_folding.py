# calculate paper thickness after repeated folding
INITIAL_THICKNESS_MM = 0.1
FOLDS = 30

# calculate final thickness
thickness_mm = INITIAL_THICKNESS_MM * (2 ** FOLDS)

# convert to different units
thickness_m = thickness_mm / 1000
thickness_km = thickness_m / 1000

print(f"Thickness after {FOLDS} folds: {thickness_mm:,.2f} mm")
print(f"Thickness in meters: {thickness_m:,.2f} m")
print(f"Thickness in kilometers: {thickness_km:,.6f} km")

print("\nTest Case:")
print("Input:")
print(f"- Initial thickness: {INITIAL_THICKNESS_MM} mm")
print(f"- Number of folds: {FOLDS}")
print("\nExplanation:")
print("The thickness doubles with each fold:")
print("Fold 1: 0.2 mm")
print("Fold 2: 0.4 mm")
print("Fold 3: 0.8 mm")
print("...")
print(f"Fold {FOLDS}: {thickness_mm:,.2f} mm")
print(f"\nExpected Output: ~107,374,182.40 mm")
print(f"Actual Output: {thickness_mm:,.2f} mm")

# verify calculation matches expected value
print(f"Test Result: {'PASSED' if abs(thickness_mm - 107374182.4) < 1e-1 else 'FAILED'}") 