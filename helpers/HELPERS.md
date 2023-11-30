## Importing modules into your main script

In your main Python script (let's say main_script.py), you can import the modules from the helpers directory like this:

```python
from helpers.grid_helpers import create_grid, print_grid, get_neighbors
from helpers.data_structures import Stack, Queue
from helpers.parsing_utils import read_input_file, split_lines_to_integers, parse_csv_line

# Example usage
grid = create_grid(5, 5, default_value=-1)
print_grid(grid)
# ... rest of your code ...

```