#program to calculate the love between two people:
# use the count method

print("Welcome to the love calculator!")

fst_partner = input("Enter the first person's name: ").lower()
scnd_partner = input("Enter the second person's name:").lower()
name = fst_partner + scnd_partner

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e') 

oc_true = t + r + u + e

oc_love = l + o + v + e

total = str(oc_true) + str(oc_love)
score = int(total)

if score < 10 or score > 90:
    print(f"Your love score is {score}%. \nYou Go together like Coke and Mentos.")
elif score >= 40 and score <=50:
    print(f"Your love score is {score}%. \nYou are alright together!")
else:
    print(f"Your love score is {score}%.")
