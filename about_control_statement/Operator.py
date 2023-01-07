

num = 10
num1 = 3
result = num + num1
result1 = num - num1
result2 = num * num1
result3 = num / num1
re = float(result3)
result4 = num % num1
result5 = num // num1
result6 = num ** num1

print(result)
print(result1)
print(result2)
print(re)
print(result4)
print(result5)
print(result6)
print("-------------------------------------")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
choice = int(input("Enter choice: "))
if choice >= 1 and choice <= 4:
    print("enter two number!!")
    number1 = int(input("enter number1: "))
    number2 = int(input("enter number2: "))
    if choice == 1:
        result_number = number1 + number2
        print(number1, " + ", number2, "=", result_number)
    elif choice == 2:
        result_number = number1 - number2
        print(number1, "-", number2, "=", result_number)
    elif choice == 3:
        result_number = number1 * number2
        print(number1, "*", number2, "=", result_number)
    elif choice == 4:

        result_number = number1 / number2
        re = float(result_number)
        print(number1, "/", number2, "=", re)
    elif choice == 5:
        exit()
    else:
        print("Wrong input!!!")

