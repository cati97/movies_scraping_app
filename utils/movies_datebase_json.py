import json
import requests

from parsers.movie_parser import MovieParser
from utils.shortcuts import shorts_search_by
from utils.user_options import OPTIONS_SEARCH_BY


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

    def prompt_add_movie(self):
        link = input("\nEnter a IMDb movie link: ")
        page_content = requests.get(link).content
        movie = MovieParser(page_content)
        movie_dict = movie.movie_parser_as_dict
        print(movie)
        self.add_movie(movie_dict)

    def search_movie_by_title_or_year(self, short, title_year):
        for movie in self.get_all_movies:
            if movie[shorts_search_by[short]] == title_year:
                print(f'\nTitle: {movie["Title"]}'
                      f'\nYear: {movie["Year"]}'
                      f'\nDuration: {movie["Duration"]}'
                      f'\nGenres: {movie["Genres"]}'
                      f'\nActors: {movie["Actors"]}'
                      f'\nDescription: {movie["Description"]}')

    def search_movie_by_actor_or_genre(self, short, actor_genre):
        for movie in self.get_all_movies:
            for match in movie[shorts_search_by[short]]:
                if match == actor_genre:
                    print(f'\nTitle: {movie["Title"]}'
                          f'\nYear: {movie["Year"]}'
                          f'\nDuration: {movie["Duration"]}'
                          f'\nGenres: {movie["Genres"]}'
                          f'\nActors: {movie["Actors"]}'
                          f'\nDescription: {movie["Description"]}')

    def prompt_remove_movie(self):
        title = input("Enter the title of a movie you want to remove: ")
        self.search_movie_by_title_or_year('t', title)
        decision = input("\nAre you sure you want to remove this movie? y/n : ")
        if decision == 'y':
            self.delete_movie(title)
            print("Movie deleted properly")

    def prompt_search_for_movie(self):
        search_by = input(OPTIONS_SEARCH_BY)
        while search_by != 'q':
            if search_by == 't':
                title = input("Enter movie title to see all its' features: ")
                self.search_movie_by_title_or_year(search_by, title)
            elif search_by == 'y':
                year = input("Enter a year to see all the movies released then: ")
                self.search_movie_by_title_or_year(search_by, int(year))
            elif search_by == 'g':
                genre = input("Enter a genre to see all the movies with that category: ")
                self.search_movie_by_actor_or_genre(search_by, genre)
            elif search_by == 'a':
                actor = input(
                    "Enter first name and last name of an actor to see all the movies starred by this person: ")
                self.search_movie_by_actor_or_genre(search_by, actor)
            else:
                print("I don't understand, please try again. ")
            search_by = input(OPTIONS_SEARCH_BY)
