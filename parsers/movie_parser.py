from bs4 import BeautifulSoup
from locators.movie_details_locators import MovieDetailsLocators


class MovieParser:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def __repr__(self):
        return f'\nTitle: {self.title}\n' \
               f'Year: {self.year}\n' \
               f'Duration: {self.duration}\n' \
               f'Genres: {self.genres}\n' \
               f'Actors: {self.actors}\n' \
               f'Description: {self.description}\n'

    @property
    def title(self):
        locator = MovieDetailsLocators.TITLE
        title = self.soup.select_one(locator).contents[0].strip()
        return title

    @property
    def year(self):
        locator = MovieDetailsLocators.YEAR
        year = self.soup.select_one(locator).string
        return int(year)

    @property
    def duration(self):
        locator = MovieDetailsLocators.DURATION
        duration = self.soup.select_one(locator).string.strip()
        return duration

    @property
    def genres(self):
        locator = MovieDetailsLocators.GENRES
        genres = self.soup.select(locator)
        return [g.string for g in genres[:-1]]  # without last a tag

    @property
    def actors(self):
        locator = MovieDetailsLocators.ACTORS
        actors = self.soup.select(locator)
        return [a.string for a in actors[:-1]]

    @property
    def description(self):
        locator = MovieDetailsLocators.DESCRIPTION
        description = self.soup.select_one(locator).string.strip()
        return description

    @property
    def movie_parser_as_dict(self):
        return {'Title': self.title,
                'Year': self.year,
                'Duration': self.duration,
                'Genres': self.genres,
                'Actors': self.actors,
                'Description': self.description}
