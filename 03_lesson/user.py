class User:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def firstName(self):
        print(self.first)

    def lastName(self):
        print(self.last)

    def fullName(self):
        print(f"{self.first} {self.last}")
