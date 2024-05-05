print("Welcome to the rollercoaster!")
bill = 0
height = int(input("What is your height? "))

if height >= 120:
    print("You can ride the rollerCoaster!")
    
    age = int(input("What is your age?"))
    
    if age < 12:
        print("Child's tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("You can ride for free!")
    else:
        print("Adult tickets are $12.")
        bill = 12
    
    photo = input("Do you want a photo taken? (Y/N)").lower()
    if photo == 'y':
        bill += 3
    
    print(f"Your final bill is {bill}.")    
else:
    print("You cannot ride the rollerCoaster.")
