# Program 1(e): Library Management using class and objects

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

book1 = Book("Python Programming", "John", 450)
book2 = Book("Machine Learning", "David", 600)

book1.display()
book2.display()
