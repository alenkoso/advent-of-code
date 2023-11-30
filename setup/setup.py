import os
import requests
from BeautifulSoup import bs4
from datetime import datetime
import configparser

def get_session_cookie():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT']['SessionCookie']
    
def create_directory(year, day):
    ### Create directories for the given year and day under './src/' if they don't exist. ###
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Path to the setup directory
    base_dir = os.path.join(script_dir, "../src")  # Adjusted to point to the parent directory's 'src' folder
    year_dir = os.path.join(base_dir, str(year))
    day_dir = os.path.join(year_dir, f"Day_{day}")
    
    # Create base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Create year directory if it doesn't exist
    if not os.path.exists(year_dir):
        os.makedirs(year_dir)

    # Create day directory if it doesn't exist
    if not os.path.exists(day_dir):
        os.makedirs(day_dir)

    return day_dir

def generate_aoc_url(year, day, is_input=False):
    ### Generate the URL for the given day and year for Advent of Code. ###
    base_url = f"https://adventofcode.com/{year}/day/{day}"
    return f"{base_url}/input" if is_input else base_url

def make_request(url, session_cookie=None):
    ### Make an HTTP request to the given URL. ###
    headers = {'Cookie': f'session={session_cookie}'} if session_cookie else {}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response

def fetch_input(day, year, session_cookie):
    ### Fetch the puzzle input for the given day and year using the session cookie. ###
    url = generate_aoc_url(year, day, is_input=True)
    response = make_request(url, session_cookie)
    return response.text

def save_input(input_data, dir_name):
    ### Save the fetched input data to a text file. ###
    with open(os.path.join(dir_name, "input.txt"), 'w') as file:
        file.write(input_data)

def fetch_instructions(day, year):
    ### Fetch the puzzle instructions for the given day and year. ###
    url = generate_aoc_url(year, day)
    response = make_request(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('article')
    return article.get_text(strip=True) if article else "Instructions not found."

def save_instructions(instructions, dir_name):
    ### Save the instructions to a text file. ###
    with open(os.path.join(dir_name, "instructions.txt"), 'w') as file:
        file.write(instructions)

def create_base_python_file(day, dir_name):
    ### Create a base Python file for the given day with links to input, instructions, and helper imports. ###
    file_path = os.path.join(dir_name, f"{day}.py")
    with open(file_path, 'w') as file:
        file.write("# Advent of Code\n")
        file.write(f"# Day {day}\n")
        file.write(f"# See instructions: {os.path.join('..', '..', 'instructions.txt')}\n")
        file.write(f"# See input data: {os.path.join('..', '..', 'input.txt')}\n\n")
        file.write("import sys\n")
        file.write("import os\n")
        file.write("sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))\n\n")
        file.write("from helpers.grid_helpers import *\n")
        file.write("from helpers.data_structures import *\n")
        file.write("from helpers.parsing_utils import *\n\n")
        file.write("def main():\n")
        file.write("    # Your code here\n\n")
        file.write("if __name__ == '__main__':\n")
        file.write("    main()\n")

def setup_day_challenge(current_day, current_year, session_cookie):
    ### Set up the directory and files for the current day's challenge. ###
    day_dir = create_directory(current_year, current_day)

    try:
        # Fetch and save inputs
        input_data = fetch_input(22, 2022, session_cookie)
        save_input(input_data, day_dir)
        print(f"Input for Day {current_day}, Year {current_year} saved to {day_dir}/input.txt")

        # Fetch and save instructions
        instructions = fetch_instructions(current_day, current_year)
        save_instructions(instructions, day_dir)
        print(f"Instructions for Day {current_day}, Year {current_year} saved to {day_dir}/instructions.txt")

        # Create base Python file
        create_base_python_file(current_day, day_dir)
        print(f"Base Python file for Day {current_day} created at {day_dir}/{current_day}.py")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    session_cookie = get_session_cookie()
    current_day = datetime.now().day
    current_year = datetime.now().year

    print(f"Setting up for Day {current_day} of the year {current_year}...")
    setup_day_challenge(current_day, current_year, session_cookie)

if __name__ == "__main__":
    main()
