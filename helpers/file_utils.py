def read_input_file(file_path: str, mode: str = 'lines', number_type: str = 'int', delimiter: str = None) -> list:
    with open(file_path, 'r') as file:
        if mode == 'full':
            return file.read().strip().split('\n\n')
        elif mode == 'lines_stripped':
            return [line.strip() for line in file]
        elif mode == 'lines_numbers':
            return [float(line.strip()) if number_type == 'float' else int(line.strip()) for line in file]
        elif mode == 'lines_split':
            return [line.strip().split(delimiter) for line in file]
        else:  # default to reading lines (./parsing_utils/read_input_file())
            return file.readlines()

