height = float(input("What's your Height in meters? "))
weight =  float (input("What's your weight in Kg? "))

bmi = ((weight)/height**2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underwheight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
