class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "stocked"


class Request:
    def __init__(self, command, args: list):
        self.command = command
        self.args = args
        pass
