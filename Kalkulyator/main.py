print("\tKALKULYATOR")
num1 = int(input("Son kiriting: "))
oper = input("Amal kiriting: ")
num2 = int(input("Son kiriting: "))
if oper == '+':
    print(f"Natija: {num1+num2}")
elif oper == '-':
    print(f"Natija: {num1-num2}")
elif oper == '*':
    print(f"Natija: {num1*num2}")
elif oper == '/':
    print(f"Natija: {num1//num2}")
elif oper == '**':
    print(f"Natija: {num1**num2}")
else:
    print("Bunday amal mavjud emas!")