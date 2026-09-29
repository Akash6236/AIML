start = int(input("enter Starting Number :"))
end = int(input("enter Ending Number :"))

print("\n Prime numbers are :")
count = 0

for num in range(start,end+1):
    if num>1:
        prime=True
        for i in range(2,int(num ** 0.5)+1):
            if num%i== 0:
                prime=flase
                break

            if prime:
                print(num)
                count+=1

    print("total prime numbers= ",count)
