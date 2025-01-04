# bill calculator
# Welcome message
print("Welcome to the tip calculator!")

# Input the total bill amount
bill = float(input("What was the total bill? $"))

# Input the percentage tip you'd like to give
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Input the number of people to split the bill
people = int(input("How many people to split the bill? "))

# Calculate the total tip percentage
tip_percentage = tip / 100

# Calculate the total bill including the tip
total_bill = bill + (bill * tip_percentage)

# Calculate the amount each person should pay
amount_per_person = total_bill / people

# Format the result to 2 decimal places
final_amount = "{:.2f}".format(amount_per_person)

# Print the result
print(f"Each person should pay: ${final_amount}")