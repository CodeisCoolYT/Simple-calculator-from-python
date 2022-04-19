print("Choose your operator:")
print("1) plus")
print("2) minus")
print("3) times")
print("4) divide")
option=int(input("Enter your option (by number)\n: "))

while True:
    if option == 1:
        num1=int(input("Enter your first number: "))
        numm1=int(input("Enter your second number: "))
        ansplus=num1 + numm1
        print(ansplus)
        option=int(input("Enter your option (by number)\n: "))
    if option == 2:
        num2=int(input("Enter your first number: "))
        numm2=int(input("Enter your second number: "))
        ansminus=num2 - numm2
        print(ansminus)
        option=int(input("Enter your option (by number)\n: "))
    if option == 3:
        num3=int(input("Enter your first number: "))
        numm3=int(input("Enter your second number: "))
        anstimes=num3 * numm3
        print(anstimes)
        option=int(input("Enter your option (by number)\n: "))
    if option == 4:
        num4=int(input("Enter your first number: "))
        numm4=int(input("Enter your second number: "))
        ansdivide=num4 / numm4
        print(ansdivide)
        option=int(input("Enter your option (by number)\n: "))
    else:
        print("Invalid option!")
        option=int(input("Enter your option (by number)\n: "))
