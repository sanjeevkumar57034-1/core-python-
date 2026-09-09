#task 1

name=input("enter your name:")
favorite_food=input("enter your favorite food:")
print("hello",name,"," ,"your favorite food is",favorite_food+"!")

#task 2
number1=int(input("enter your first number"))
number2=int(input("enter your second number"))
print("sum:",number1+number2)
print("difference:",number1-number2)
print("product:",number1*number2)
print("quotient:",number1/number2)

#task_3 zomato-style bill calculator

price=float(input("enter food price :"))
quantity=int(input("enter quantity "))
total=price *quantity
print(f"your total bill is₹[total:.2f] ")

#task_4

followers=int(input("enter yuor instagram followers"))
print("\n\tyou have",followers,"followers")
like=1200
followers=1500
print("\n\tyou have",like,"likes")
print("\n\tyou have",followers,"followers")

#task_5

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -,): ")

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)
else:
    print("Error: Invalid operator")







