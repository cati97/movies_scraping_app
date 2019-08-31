import requests
import json
from parsers.movie_parser import MovieParser

USER_CHOICE = '''
Choose one of the options below:
a -> add a movie to a particular collection
g -> go into a collection to find some info
q -> quit

Your choice: '''


def prompt_add_movie_to_file():
    link = input("Enter a filmweb link to the movie you want to add: ")
    page_content = requests.get(link).content
    page = MovieParser(page_content)
    print(page)


def add_movie_to_file(movie_link, filename):
    pass


def prompt_go_into_a_file():
    pass


def go_into_a_file(filename):
    pass


choices = {
    'a': prompt_add_movie_to_file,
    'g': prompt_go_into_a_file,

}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ['a', 'g']:
            choices[user_input]()
        else:
            print("I don't understand, please try again. ")
        user_input = input(USER_CHOICE)
    else:
        print('Sorry to see you go! Bye')


menu()
