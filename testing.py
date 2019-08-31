class Test:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __repr__(self):
        return f'Title: {self.title}\n' \
               f'Year: {self.year}\n'


movie = Test('Titanic', '1997')
print(movie)
