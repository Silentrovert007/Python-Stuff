# Code repetition solved

print("Welcome to the py pizza order!")

size = input("What is the size of the required pizza (S, M or L)? ").upper()
price = 0

if size == 'S':
    price = 15
    print(f"Small Pizzas cost ${price}.")
elif size == 'M':
    price = 20
    print(f"Medium Pizzas cost ${price}.")
else:
    price = 25
    print(f"Large Pizzas cost ${price}.")

add_pep = input("Do you want pepperoni added (Y/N)? ").lower()
add_echeese = input("Do you want extra cheese added (Y/N)? ").lower()

if add_pep == 'y':
    if size == 'S':
        price += 2
    else:
        price += 3

if add_echeese == 'y':
    price += 1

print(f"Your final bill is ${price}.")
