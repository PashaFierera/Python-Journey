weight = 67
height = 1.61

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi <= 18.5:
    print("underweight")  # Use lowercase
elif 18.5 <= bmi < 25:
    print("normal weight")  # Use lowercase
else:
    print("overweight")  # Use lowercase
