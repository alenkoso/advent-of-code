# parsing_utils.py

def read_input_file(file_path):
    ### Read a file and return the content as a list of lines. ###
    with open(file_path, 'r') as file:
        return file.readlines()

def split_lines_to_integers(lines):
    ### Split each line by whitespace and convert to integers. ###
    return [list(map(int, line.split())) for line in lines]

def parse_csv_line(line, cast_type=int):
    ### Parse a CSV line to a list of values with a specified type. ###
    return [cast_type(x) for x in line.split(',')]
