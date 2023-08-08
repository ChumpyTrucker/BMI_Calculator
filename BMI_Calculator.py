# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)

#If statement
if bmi < 18.5:
    print('\033[1m' +  f"Your BMI is {bmi}, you are underweight. " + '\033[0m' )
elif bmi >= 18.5 and bmi <= 25:
    print('\033[1m' + f"Your BMI is {bmi}, you have a normal weight." + '\033[0m')
elif bmi >= 25 and bmi <= 30:
    print('\033[1m' + f"Your BMI is {bmi}, you are slightly overweight." + '\033[0m')
elif bmi >= 30 and bmi <= 35:
    print('\033[1m' + f"Your BMI is {bmi}, you are obese." + '\033[0m')
else:
    print('\033[1m' + f"Your BMI is {bmi}, you are clinically obese." + '\033[0m')
