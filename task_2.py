
print("_____Select operation_______ ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
print("6.Calculate power of a number")

while True:

    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
       print("Addition -> ", num1, "+", num2, "=", num1+num2)
    elif choice == '2':
       print("Substraction -> ", num1, "-", num2, "=", num1-num2)
    elif choice == '3':
       print("Multiplication -> ",num1, "*", num2, "=", num1*num2)

    elif choice == '4':
           print("Dvision -> ",num1, "/", num2, "=", num1/num2)
    elif choice == '5':
           print("modulus -> ",num1, "%", num2, "=", num1%num2)
    elif choice == '6':
          n = int(input('Enter a number : '))
          x = int(input('Enter power--> (2/3/4...) : '))
          print(f'{n} ^ {x} is: {n**x}')
    else:
       print("Invalid Input")
    if choice == '7':
        break