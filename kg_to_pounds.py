KG_TO_LBS_FACTOR = 2.20462

def kg_to_pounds(kilograms):
    pounds = kilograms * KG_TO_LBS_FACTOR
    return pounds

weight_a_kg = 50
weight_b_kg = 75

weight_a_lbs = kg_to_pounds(weight_a_kg)
weight_b_lbs = kg_to_pounds(weight_b_kg)

total_weight_lbs = weight_a_lbs + weight_b_lbs

print("--- Kilogram to Pounds Converter ---")
print(f"Weight A: {weight_a_kg} kg is {weight_a_lbs:.2f} lbs")
print(f"Weight B: {weight_b_kg} kg is {weight_b_lbs:.2f} lbs")
print("-" * 35)
print(f"Total Combined Weight in Pounds: {total_weight_lbs:.2f} lbs")