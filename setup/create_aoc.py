#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
from pathlib import Path
from datetime import datetime

def create_aoc_project(year, day, packages=None):
    # Create AoC project structure for specific day.
    if packages is None:
        packages = ['numpy', 'pandas']
        
    # Get the root project directory (2 levels up from setup/)
    root_dir = Path(__file__).parent.parent
    src_dir = root_dir / 'src'
    
    # Create project structure
    project_name = f"{year}/Day_{day:02d}"
    project_path = src_dir / project_name
    project_path.mkdir(parents=True, exist_ok=True)
    
    # Create virtual environment if it doesn't exist
    venv_path = root_dir / 'venv'
    if not venv_path.exists():
        print(f"Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', str(venv_path)])
        
        # Install packages in the venv
        if os.name == 'nt':  # Windows
            pip_path = venv_path / 'Scripts' / 'pip'
        else:  # Unix/macOS
            pip_path = venv_path / 'bin' / 'pip'
            
        subprocess.run([str(pip_path), 'install', '--upgrade', 'pip'])
        if packages:
            subprocess.run([str(pip_path), 'install'] + packages)
            subprocess.run([str(pip_path), 'freeze', '>', str(root_dir / 'requirements.txt')], shell=True)
    
    # Create day's files
    template = f'''def parse_input(filename="input.txt"):
    with open(filename) as f:
        return f.read().strip()

def part1(data):
    # TODO: Implement part 1
    pass

def part2(data):
    # TODO: Implement part 2
    pass

def main():
    data = parse_input()
    print(f"Part 1: {{part1(data)}}")
    print(f"Part 2: {{part2(data)}}")

if __name__ == "__main__":
    main()
'''
    
    # Create files
    (project_path / f'{day:02d}.py').write_text(template)
    (project_path / 'input.txt').touch()
    (project_path / 'test_input.txt').touch()
    
    print(f"\nCreated AoC {year} Day {day} project!")
    print(f"Project structure:")
    print(f"src/")
    print(f"└── {year}/")
    print(f"    └── Day_{day:02d}/")
    print(f"        ├── {day:02d}.py")
    print("        ├── input.txt")
    print("        └── test_input.txt")

    # Print commands for user to run
    print("\nTo navigate to project directory and activate venv, run these commands:")
    print(f"cd {project_path}")
    if os.name == 'nt':  # Windows
        print(f"{venv_path}/Scripts/activate")
    else:  # Unix/macOS
        print(f"source {venv_path}/bin/activate")

def main():
    parser = argparse.ArgumentParser(description='Create AoC project structure')
    parser.add_argument('--year', type=int, default=datetime.now().year)
    parser.add_argument('--day', type=int, required=True)
    parser.add_argument('--packages', nargs='+', help='Additional packages to install')
    args = parser.parse_args()
    
    create_aoc_project(args.year, args.day, args.packages)

if __name__ == '__main__':
    main()