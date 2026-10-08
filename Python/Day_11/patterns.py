print("1. Square")
print("2. Rectangle")
print("3. Right Triangle")
print("4. Diamond")
print("5. Circle")

choice = int(input("Enter your choice: "))

if choice == 1:
    n = int(input("Enter size: "))

    for i in range(n):
        print("* " * n)


elif choice == 2:
    rows = int(input("Enter rows: "))
    cols = int(input("Enter columns: "))

    for i in range(rows):
        print("* " * cols)


elif choice == 3:
    n = int(input("Enter size: "))

    for i in range(1, n + 1):
        print("* " * i)


elif choice == 4:
    n = int(input("Enter size: "))

    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


elif choice == 5:
    n = int(input("Enter radius: "))

    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            if i * i + j * j <= n * n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


else:
    print("Invalid choice")