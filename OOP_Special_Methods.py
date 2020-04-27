class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('deleted')

b = Book("Python", "Jose", 200)
print(b)

print(len(b))
del b