# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# Bmi = weight/ height squared.

height = input("Input height in m: ")
weight = input("input weight in kg: ")

num1 = float(height)
num2 = float(weight)
bmi = num2/(num1*num1)
# or bmi = num2/num1 ** 2
# result = int(bmi)
# print(result)
print(int(bmi))