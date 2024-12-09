Part 1 deals with moving individual blocks from right to left to make space contiguous. 
The key insight here was that we want to move blocks to the leftmost available space - but
scanning from left each time would be inefficient. Instead, we track free spaces in a queue,
making it O(1) to find the next available space.

Part 2 changes the rules - now we move whole files at once, and in a specific order (highest ID first).
Here we need to find contiguous free spaces big enough for each file. A file only moves if there's 
enough continuous free space to its left.

Implementation approach:
1. Parse the input into blocks with file IDs and track free spaces ('.')
2. For Part 1: Use a deque to track free spaces for quick access and updates
3. For Part 2: Keep track of file starting positions and lengths to move whole files at once
4. Calculate checksum by multiplying position by file ID

The main optimization was avoiding repeated scans over the blocks array by maintaining the
free space queue in Part 1, and doing file moves efficiently in Part 2.

Example:
Input: "12345" -> One-block file, two spaces, three-block file, four spaces, five-block file
Part 1: Move blocks individually left
Part 2: Move whole files in reverse ID order