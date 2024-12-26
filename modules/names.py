from random import choice
import os

# prep file names to read list of names
cur_path = os.path.dirname(os.path.abspath(__file__))
FIRST_NAMES_PATH = os.path.join(cur_path, '..', 'data', 'first_names.txt')
LAST_NAMES_PATH = os.path.join(cur_path, '..', 'data', 'last_names.txt')

# return a random first name
def rng_first_name():
    random_name = choice(open(FIRST_NAMES_PATH).readlines()).rstrip()
    return random_name

# return a random last name
def rng_last_name():
    random_name = choice(open(LAST_NAMES_PATH).readlines()).rstrip()
    return random_name

# return a random first, last name pair
def player_name():
    return [rng_first_name(), rng_last_name()]
