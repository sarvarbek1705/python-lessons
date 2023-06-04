print("\tKARRA JADVALI")
number = range(int(input("Istalgan raqamingizni kiriting: ")))
for karra in number:
    print("\n")
    for n in list(range(10)):
        print(f"{karra+1}x{n+1}={(karra+1)*(n+1)}")