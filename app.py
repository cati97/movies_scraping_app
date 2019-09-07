import requests
from parsers.movie_parser import MovieParser
from utils.user_options import *
from utils.movies_datebase_json import MoviesDatabaseJson
from utils.shortcuts import *


def _change_movie_parser_to_movie_dict(movie_parser):
    return {'Title': movie_parser.title,
            'Year': movie_parser.year,
            'Duration': movie_parser.duration,
            'Genres': movie_parser.genres,
            'Actors': movie_parser.actors,
            'Description': movie_parser.description}


def prompt_add_movie(file_obj):
    link = input("\nEnter a IMDb movie link: ")
    page_content = requests.get(link).content
    movie = MovieParser(page_content)
    movie_dict = _change_movie_parser_to_movie_dict(movie)
    print(movie)
    file_obj.add_movie(movie_dict)


def search_movie_by_title_or_year(short, title_year, file_obj):
    for movie in file_obj.get_all_movies:
        if movie[shorts_search_by[short]] == title_year:
            print(f'\nTitle: {movie["Title"]}'
                  f'\nYear: {movie["Year"]}'
                  f'\nDuration: {movie["Duration"]}'
                  f'\nGenres: {movie["Genres"]}'
                  f'\nActors: {movie["Actors"]}'
                  f'\nDescription: {movie["Description"]}')


def search_movie_by_actor_or_genre(short, actor_genre, file_obj):
    for movie in file_obj.get_all_movies:
        for match in movie[shorts_search_by[short]]:
            if match == actor_genre:
                print(f'\nTitle: {movie["Title"]}'
                      f'\nYear: {movie["Year"]}'
                      f'\nDuration: {movie["Duration"]}'
                      f'\nGenres: {movie["Genres"]}'
                      f'\nActors: {movie["Actors"]}'
                      f'\nDescription: {movie["Description"]}')


def prompt_remove_movie(file_obj):
    title = input("Enter the title of a movie you want to remove: ")
    search_movie_by_title_or_year('t', title, file_obj)
    decision = input("\nAre you sure you want to remove this movie? y/n : ")
    if decision == 'y':
        file_obj.delete_movie(title)
        print("Movie deleted properly")


def prompt_search_for_movie(file_obj):
    search_by = input(OPTIONS_SEARCH_BY)
    while search_by != 'q':
        if search_by == 't':
            title = input("Enter movie title to see all its' features: ")
            search_movie_by_title_or_year(search_by, title, file_obj)
        elif search_by == 'y':
            year = input("Enter a year to see all the movies released then: ")
            search_movie_by_title_or_year(search_by, int(year), file_obj)
        elif search_by == 'g':
            genre = input("Enter a genre to see all the movies with that category: ")
            search_movie_by_actor_or_genre(search_by, genre, file_obj)
        elif search_by == 'a':
            actor = input("Enter first name and last name of an actor to see all the movies starred by this person: ")
            search_movie_by_actor_or_genre(search_by, actor, file_obj)
        else:
            print("I don't understand, please try again. ")
        search_by = input(OPTIONS_SEARCH_BY)


def menu_inside_file(file_short):
    file_path = file_paths[file_short]
    print(f"\nWelcome to your {list_names[file_short]}!")
    action = input(OPTIONS_INSIDE_FILE)
    f = MoviesDatabaseJson(file_path)
    while action != 'q':
        if action == 'd':
            f.print_nicely_all_movies()
        elif action == 'a':
            prompt_add_movie(f)
            print(f"Movie successfully added to {list_names[file_short]} :D")
        elif action == 's':
            prompt_search_for_movie(f)
        elif action == 'r':
            prompt_remove_movie(f)
        else:
            print("I don't understand, please try again. ")
        action = input(OPTIONS_INSIDE_FILE)


'''
What would you like to do?

a - add new movie
d - display all movies
s - search for particular movie/s
r - remove a movie
q - quit

>> '''


def main_menu():
    print("\nWelcome to My Movies App. Add, delete, search for movies using IMDb web page.")
    user_file_short = input(FILE_CHOICE)
    while user_file_short != 'q':
        if user_file_short in ['f', 'p', 'w']:
            menu_inside_file(user_file_short)
        else:
            print("I don't understand, please try again. ")
        user_file_short = input(FILE_CHOICE)
    else:
        print('Thanks for using me! :) See you soon!')


main_menu()
