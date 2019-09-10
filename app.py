from utils.user_options import *
from utils.movies_datebase_json import MoviesDatabaseJson
from utils.shortcuts import *


def menu_inside_file(file_short):
    file_path = file_paths[file_short]
    print(f"\nWelcome to your {list_names[file_short]}!")
    action = input(OPTIONS_INSIDE_FILE)
    f = MoviesDatabaseJson(file_path)
    while action != 'q':
        if action == 'd':
            f.print_nicely_all_movies()
        elif action == 'a':
            f.prompt_add_movie()
            print(f"Movie successfully added to {list_names[file_short]} :D")
        elif action == 's':
            f.prompt_search_for_movie()
        elif action == 'r':
            f.prompt_remove_movie()
        else:
            print("I don't understand, please try again. ")
        action = input(OPTIONS_INSIDE_FILE)


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
