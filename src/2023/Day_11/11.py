import os
import sys
from helpers.grid_helpers import Grid


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

def find_galaxies(grid):
    galaxies = []
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x, y) == '#':
                galaxies.append((x, y))
                return galaxies

            def calculate_total_path_length(grid):
                grid.expand()
                galaxies = find_galaxies(grid)
                total_path_length = 0

                for i in range(len(galaxies)):
                    for j in range(i + 1, len(galaxies)):
                        x1, y1 = galaxies[i]
                        x2, y2 = galaxies[j]
                        path_length = abs(x2 - x1) + abs(y2 - y1)
                        total_path_length += path_length

                        return total_path_length

                    def main():
                        # Adjust this file path according to your directory structure
                        input_file_path = ('input.txt')
                        cosmic_grid = Grid.from_file(input_file_path)
                        total_path_length = calculate_total_path_length(cosmic_grid)
                        print("Total Path Length: ", total_path_length)

                        if __name__ == "__main__":
                            main()

