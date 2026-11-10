# ==========================================
#          BODY MASS INDEX (BMI) CALCULATOR
# ==========================================

print("Welcome to the BMI Calculator!\n")

# Step 1: Prompt user for weight in kilograms
weight = float(input("Enter your weight in kg (e.g., 70): "))

# Step 2: Prompt user for height in meters
height = float(input("Enter your height in meters (e.g., 1.75): "))

# Step 3: Calculate BMI using the formula: weight / [height]^2
bmi = weight / (height ** 2)

# Step 4: Display the calculated BMI and health category
print(f"\n--- Results ---")
print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")