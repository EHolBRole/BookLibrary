class Book:  # Realisation of Book entity
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "stocked"
        self.id = None

