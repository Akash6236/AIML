# Program 1(b): Bank ATM System using branching

balance = 25000

while True:
    print("\n----- ATM MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Amount deposited successfully.")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Please collect your cash.")
        else:
            print("Insufficient balance.")

    elif choice == 3:
        print("Available balance:", balance)

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Try again.")
