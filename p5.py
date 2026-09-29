class student:
    def __init__(self,name,regno,marks):
        self.name = name
        self.regno = regno
        self.marks = marks

    def display(self):
        print("\nName:", self.name)
        print("\nRegno:", self.regno)
        print("\nMarks:", self.marks)


m1 = student("Abhiram", "101", "80")
m2 = student("Amrutha", "102", "90")

m1.display()
m2.display()