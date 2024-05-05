print("Welcome to the py pizza order!")

size = input("What is th e size of the required pizza (S, M or L)? ")
price = 0

if size == 'S':
    price = 15

    print(f"Small Pizzas cost ${price}.")
    add_pep = input("Do you want peperoni added (Y/N)?").lower()
    add_echeese = input("Do you want extra cheeze added (Y/N)?").lower()

    if  add_pep == 'y':
        price +=2
    if add_echeese == 'y':
        price += 1

    print(f"Your final bill is ${price}.")

elif size == 'M':
    price = 20
    print(f"Medium Pizzas cost ${price}.")
    add_pep = input("Do you want peperoni added (Y/N)?").lower()
    add_echeese = input("Do you want extra cheeze added (Y/N)?").lower()

    if  add_pep == 'y':
        price +=3
    if add_echeese == 'y':
        price += 1

    print(f"Your final bill is ${price}.")
else:
    price = 20
    print(f"Large Pizzas cost ${price}.")
    add_pep = input("Do you want peperoni added (Y/N)?").lower()
    add_echeese = input("Do you want extra cheeze added (Y/N)?").lower()

    if  add_pep == 'y':
        price +=3
    if add_echeese == 'y':
        price += 1
    print(f"Your final bill is ${price}.")






