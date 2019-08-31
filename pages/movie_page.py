from bs4 import BeautifulSoup
from parsers.movie_parser import MovieParser


class MoviePage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def movie(self):
        return MovieParser(self.soup)
