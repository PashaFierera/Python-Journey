print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Children ticket are $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket aare $7.")
    else:
        bill = 12
        print("Adult ticket are $12.")

        wants_photo = input ("Do you want to have the photo take? type Y for Yes and N for No")
        if wants_photo == "y":
            bill += 3
    print(f"Your final bill is${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
