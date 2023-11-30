# Advent of Code Automation Script 

## Overview
This Python script (setup.py) automates the setup for the Advent of Code (AoC) challenges. It creates a directory structure for each day's challenge, fetches and saves the puzzle input and instructions, allowing participants to focus on solving the puzzles.

## Features
- **Automatic Directory Creation**: For each day of the challenge, creates directories under `./src/[Year]/Day_[Day]`.
- **Input Fetching**: Downloads the puzzle input for the day and saves it as `input.txt`.
- **Instruction Fetching**: Retrieves the puzzle instructions and saves them as `instructions.txt`.

## Prerequisites
- Python 3.6 or later.
- `requests` and `beautifulsoup4` libraries. Install them using:
  ```bash
  pip install requests beautifulsoup4

## Configuration

1. Session Cookie: Store your AoC session cookie in config.ini (same directory as the script):

    ```bash
    [DEFAULT]
    SessionCookie = your_session_cookie_here

Keep your session cookie secure and do not share this file.

2. .gitignore: Ensure config.ini is listed in .gitignore to prevent it from being pushed to public repositories.

## Usage

Run the script from the terminal:

```bash
python3 setup.py
```

### The script will automatically:

- Determine the current day and year.
- Create necessary directories under ./src/[Year]/Day_[Day].
- Fetch and save the day's puzzle input to input.txt.
- Fetch and save the day's instructions to instructions.txt.

## Directory structure

```
./src/
│
└───2023/
    │
    ├───Day_1/
    │   ├─── input.txt
    │   └─── instructions.txt
    │
    ├───Day_2/
    │   ├─── input.txt
    │   └─── instructions.txt
    │
    ... (and so on)
```