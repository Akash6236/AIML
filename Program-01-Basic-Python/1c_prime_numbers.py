# Program 1(c): Generate prime numbers in a given range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)
            count += 1

print("Total prime numbers:", count)
