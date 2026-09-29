balance = 25000

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Deposit amount: "))
        balance += amount
        print("Amount deposited successfully.")
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Withdraw amount: "))

        if amount <= balance:
            balance -= amount
            print("Collect Cash")
            print("Balance:", balance)
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")