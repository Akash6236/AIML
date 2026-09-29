class student:
    def __init__(self,name,regno,marks):
        self.name=name
        self.regno=regno
        self.marks=marks



    def display(self):
        print("\n  name:", self.name)
        print("\n  regno:", self.regno)
        print("\n  marks:", self.marks)

m1=student("Abhiram","101","80")
m2=student("Amrutha","102","90")

m1.display()
m2.display()