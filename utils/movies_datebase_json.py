import json


class MoviesDatabaseJson:
    def __init__(self, file_path):
        self.file_path = file_path
        self._create_empty_list_at_first_runtime()

    def _create_empty_list_at_first_runtime(self):
        with open(self.file_path, 'r') as f:
            content = f.read()
        if content == '':  # only if file is completely empty - create an []
            with open(self.file_path, 'w') as file:
                json.dump([], file)

    def add_movie(self, movie_dict):
        movies = self.get_all_movies
        movies.append(movie_dict)
        self._save_all_movies(movies)

    @property
    def get_all_movies(self):
        with open(self.file_path, "r") as content:
            return json.load(content)

    def print_nicely_all_movies(self):
        for movie in self.get_all_movies:
            print(f'\nMovie {self.get_all_movies.index(movie) + 1}\n\n'
                  f'Title: {movie["Title"]}'
                  f'\nYear: {movie["Year"]}'
                  f'\nDuration: {movie["Duration"]}'
                  f'\nGenres: {movie["Genres"]}'
                  f'\nActors: {movie["Actors"]}'
                  f'\nDescription: {movie["Description"]}')

    def _save_all_movies(self, movies):
        with open(self.file_path, 'w') as file:
            json.dump(movies, file)

    def delete_movie(self, title):
        movies = self.get_all_movies
        movies = [movie for movie in movies if title != movie['Title']]
        self._save_all_movies(movies)
