print("Wellcome to the tip calculator\n")

bill = float(input("What was the total bill? $"))
percent_tip = float(input("How much tip you'd like to give? 10, 12 or 15? $\n"))
percent_tip = percent_tip/100
number_of_people = int(input("How many people to split the bill? $\n"))

total_bill = round((bill *(1 + percent_tip) /number_of_people), 2)

print(f"Each person must pay ${total_bill}.")