year = int(input("Year: "))

if year % 4 == 0:
    if year % 100:
        if year % 400:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is a not leap year.")
    else:
        print(f"{year} is a not leap year.")
else:
    print(f"{year} is not a leap year.")
