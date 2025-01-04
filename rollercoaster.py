# Welcome words
print("Welcome to the rollercoaster!")
# Height input
height = int(input("How tall are you in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
    
    # Age input    
    age = int(input("How old are you? "))

    if age <= 12:
        print("You have to pay $7")
    elif age <= 18:
        print("You have to pay $5")
    else:
        print("You have to pay $12")
else: 
    print("Sorry, we cannot let you ride the rollercoaster")
