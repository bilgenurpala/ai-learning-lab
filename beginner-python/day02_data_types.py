# BMI Calculator

# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it: 
## bmi is equal to the person's weight divided by the person's height squared. 
## Convert this sentence into code on line 6.

heigth = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / (float(heigth) ** 2)
print(int(bmi))