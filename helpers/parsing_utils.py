def read_input_file(file_path):
    ### Read a file and return the content as a list of lines.
    with open(file_path, 'r') as file:
        return file.readlines()
    
def read_input_file_strip_lines(file_path):
    ### Read a file and return the content as a list of lines stripped of whitespaces.
    with open(file_path, 'r') as file:
        return file.read().strip().split("\n")

def split_lines_to_integers(lines):
    ### Split each line by whitespace and convert to integers.
    return [list(map(int, line.split())) for line in lines]

def parse_csv_line(line, cast_type=int):
    ### Parse a CSV line to a list of values with a specified type.
    return [cast_type(x) for x in line.split(',')]

def read_input_file_to_grid(file_path):
    ### Reads an input file and converts it into a 2D list (grid).
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

def parse_reactions(lines):
    ### Parse each line to map sources to their destinations, adjusting for types.
    reactions = {}
    typeMapping = {}
    for line in lines:
        source, destinations = line.split('->')
        source = source.strip()
        destinations = [dest.strip() for dest in destinations.split(', ')]
        reactions[source] = destinations
        typeMapping[source[1:]] = source[0]  # Extracting the type from the source
    return reactions, typeMapping

def adjust_types(reactions, typeMapping):
    ### Adjust the types in the reactions mapping based on the typeMapping.
    for src, dests in reactions.items():
        reactions[src] = [typeMapping.get(dest[1:], dest[0]) + dest if dest[1:] in typeMapping else dest for dest in dests]
    return reactions

