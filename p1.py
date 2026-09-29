name=input("enter student name:")
m1=float(input("enter marks subject 1:"))
m2=float(input("enter marks subject 2:"))
m3=float(input("enter marks subject 3:"))
m4=float(input("enter marks subject 4:"))
m5=float(input("enter marks subject 5:"))

total=m1+m2+m3+m4+m5

percentage=total/5

print("\n  result  .")

print("name:",name)
print("total",total)
print("percentage",percentage)

if m1<35 or m2<35 or m3<35 or m4<35 or m5<35:
    print("status:fail")
else:
    print("status:pass")

if percentage>=90:
    print("Grade:O")

elif percentage>=80:
    print("Grade : A+")

elif percentage>=70:
    print("Grade : A")

elif percentage>=60:
    print("Grade : B")

elif percentage>=50:
    print("Grade : C")

else:
    print("Grade : D")


