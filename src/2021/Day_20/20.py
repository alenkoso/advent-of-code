def parse_input(filename="input.txt"):
    with open(filename) as f:
        data = f.read().strip().split('\n\n')
        algorithm = data[0]
        image = data[1]
        
    # Convert algorithm to a lookup list where '#' is 1 and '.' is 0
    algorithm = [1 if c == '#' else 0 for c in algorithm]
    
    # Convert image to a set of coordinates where '#' exists
    lit_pixels = set()
    for y, line in enumerate(image.split('\n')):
        for x, c in enumerate(line):
            if c == '#':
                lit_pixels.add((x, y))
                
    return algorithm, lit_pixels

def get_bounds(image):
    if not image:
        return 0, 0, 0, 0
    min_x = min(x for x, y in image)
    max_x = max(x for x, y in image)
    min_y = min(y for x, y in image)
    max_y = max(y for x, y in image)
    return min_x, max_x, min_y, max_y

def enhance(image, algorithm, background):
    min_x, max_x, min_y, max_y = get_bounds(image)
    new_image = set()
    
    # Consider a slightly larger area than the current image
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            # Build 9-bit binary number from 3x3 grid
            idx = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    idx <<= 1
                    nx, ny = x + dx, y + dy
                    # If point is in bounds, use its value
                    # Otherwise use background value
                    if min_x <= nx <= max_x and min_y <= ny <= max_y:
                        idx |= 1 if (nx, ny) in image else 0
                    else:
                        idx |= background
            
            # Add point to new image if algorithm says it should be lit
            if algorithm[idx]:
                new_image.add((x, y))
                
    return new_image

def solve(algorithm, image, steps):
    # Handle the infinite background pixels
    # If algorithm[0] is 1 and algorithm[511] is 0, the infinite background will flash
    background = 0
    
    for step in range(steps):
        image = enhance(image, algorithm, background)
        # Update background for next iteration
        if algorithm[0] == 1 and background == 0:
            background = 1
        elif algorithm[511] == 0 and background == 1:
            background = 0
    
    return len(image)

def main():
    algorithm, image = parse_input()
    print(f"Part 1: {solve(algorithm, image, 2)}")
    print(f"Part 2: {solve(algorithm, image, 50)}")

if __name__ == "__main__":
    main()

