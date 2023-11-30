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
    # Create directories for the given year and day under './src/' if they don't exist.
    base_dir = "./src"
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
    # Generate the URL for the given day and year for Advent of Code.
    base_url = f"https://adventofcode.com/{year}/day/{day}"
    return f"{base_url}/input" if is_input else base_url

def make_request(url, session_cookie=None):
    # Make an HTTP request to the given URL.
    headers = {'Cookie': f'session={session_cookie}'} if session_cookie else {}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response

def fetch_input(day, year, session_cookie):
    # Fetch the puzzle input for the given day and year using the session cookie.
    url = generate_aoc_url(year, day, is_input=True)
    response = make_request(url, session_cookie)
    return response.text

def save_input(input_data, dir_name):
    # Save the fetched input data to a text file.
    with open(os.path.join(dir_name, "input.txt"), 'w') as file:
        file.write(input_data)

def fetch_instructions(day, year):
    # Fetch the puzzle instructions for the given day and year.
    url = generate_aoc_url(year, day)
    response = make_request(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('article')
    return article.get_text(strip=True) if article else "Instructions not found."

def save_instructions(instructions, dir_name):
    # Save the instructions to a text file.
    with open(os.path.join(dir_name, "instructions.txt"), 'w') as file:
        file.write(instructions)

def main():
    SESSION_COOKIE = get_session_cookie()
    
    current_day = datetime.now().day
    current_year = datetime.now().year
    print(f"Setting up for Day {current_day} of the year {current_year}...")

    # Fetch and save inputs
    day_dir = create_directory(current_year, current_day)
    input_data = fetch_input(current_day, current_year, SESSION_COOKIE)
    save_input(input_data, day_dir)
    print(f"Day {current_day} for year {current_year} setup complete. Input saved to {day_dir}/input.txt")

    # Fetch and save instructions
    instructions = fetch_instructions(current_day, current_year)
    save_instructions(instructions, day_dir)
    print(f"Instructions for Day {current_day} of year {current_year} saved to {day_dir}/instructions.txt")

if __name__ == "__main__":
    main()
