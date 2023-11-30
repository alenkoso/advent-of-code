import os
import requests
from datetime import datetime
import configparser

def get_session_cookie():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT']['SessionCookie']

def create_directory(year, day):
    """Create directories for the given year and day under './src/' if they don't exist."""
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

def fetch_input(day, year, session_cookie):
    """Fetch the puzzle input for the given day and year using the session cookie."""
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {'session': session_cookie}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()  # This will raise an error if the fetch fails
    return response.text

def save_input(input_data, dir_name):
    """Save the fetched input data to a text file."""
    with open(os.path.join(dir_name, "input.txt"), 'w') as file:
        file.write(input_data)

def main():
    SESSION_COOKIE = get_session_cookie()
    
    current_day = datetime.now().day
    current_year = datetime.now().year
    print(f"Setting up for Day {current_day} of the year {current_year}...")

    day_dir = create_directory(current_year, current_day)
    input_data = fetch_input(current_day, current_year, SESSION_COOKIE)
    save_input(input_data, day_dir)
    print(f"Day {current_day} for year {current_year} setup complete. Input saved to src/{day_dir}/input.txt")

if __name__ == "__main__":
    main()
