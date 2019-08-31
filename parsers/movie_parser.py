import re
from bs4 import BeautifulSoup
from locators.movie_details_locators import MovieDetailsLocators


class MovieParser:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def __repr__(self):
        return f'\nTitle: {self.title}\n' \
               f'Year: {self.year}\n' \
               f'Description: {self.description}\n' \
               f'Genres: {self.genres}\n' \
               f'Actors: {self.actors}\n'

    @property
    def title(self):
        locator = MovieDetailsLocators.TITLE
        title = self.soup.select_one(locator).string
        return title

    @property
    def year(self):
        locator = MovieDetailsLocators.YEAR
        year = self.soup.select_one(locator).string  # (2010)
        pattern = '\(([0-9]*)\)'
        match = re.search(pattern, year)
        return int(match.group(1))

    @property
    def description(self):
        locator = MovieDetailsLocators.DESCRIPTION
        description = self.soup.select_one(locator).string
        return description

    @property
    def genres(self):
        locator = MovieDetailsLocators.GENRES
        genres = self.soup.select(locator)
        return [g.string for g in genres]

    @property
    def actors(self):
        locator = MovieDetailsLocators.ACTORS
        actors = self.soup.select(locator)
        return [a.string for a in actors]
