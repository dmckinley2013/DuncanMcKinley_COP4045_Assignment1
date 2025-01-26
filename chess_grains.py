# calculate total grains on chessboard (doubles each square)
SQUARES_ON_CHESSBOARD = 64
GRAIN_WEIGHT_MG = 50

print("\n=== Chess Board Grain Calculator ===")

# calculate total grains using geometric series
total_grains = (2 ** SQUARES_ON_CHESSBOARD) - 1
total_weight_kg = (total_grains * GRAIN_WEIGHT_MG) / 1e6

print("\nResults:")
print("--------")
print(f"Total grains on the chessboard: {total_grains:,}")
print(f"Total weight of the grains: {total_weight_kg:,.2f} kg")

print("\nDepth Calculator")
print("--------------")
# calculate depth for given area
area_m2 = float(input("Enter area to cover (in square meters): "))
depth_m = (total_grains * GRAIN_WEIGHT_MG / 1e6) / area_m2
print(f"Depth of wheat covering {area_m2:,} m²: {depth_m:.6f} meters")

# verify total grains calculation
if total_grains == 18446744073709551615:
    print("\nTest PASSED ✓")
else:
    print("\nTest FAILED ✗")