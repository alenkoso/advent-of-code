import os

directories = {}
sub_directories = {}


def parse_input_and_build_directory():
    # DATA = open("test.txt").read()
    DATA = open("input.txt").read()
    lines = [x for x in DATA.split('\n')]

    current_directory = None
    for line in lines:
        if len(line.strip()) == 0:
            continue
        if line[0] == '$':
            c, command, *args = line.split()

            # cd means change directory. This changes which directory is the current directory,
            # but the specific result depends on the argument
            if command == 'cd':
                path, = args
                # cd / switches the current directory to the outermost directory, /.
                if path[0] == '/':
                    current_directory = path
                else:
                    current_directory = os.path.normpath(os.path.join(current_directory, path))
                if current_directory not in directories:
                    directories[current_directory] = 0
                    sub_directories[current_directory] = []
        else:
            size, file_name = line.split()
            if size != 'dir':
                directories[current_directory] += int(size)
            else:
                sub_directories[current_directory].append(os.path.normpath(os.path.join(current_directory, file_name)))


def get_directory_size(directory_name):
    dir_size_result = directories[directory_name]
    for index in sub_directories[directory_name]:
        if index in directories:
            dir_size_result += get_directory_size(index)
    return dir_size_result


def part_one():
    total_size = 0
    for directory in directories:
        current_directory_size = get_directory_size(directory)
        if current_directory_size <= 100000:
            total_size += current_directory_size
    return total_size


def part_two():
    total_size = get_directory_size('/')
    unused_space = 70000000 - total_size
    result_dir_size = None
    for directory in directories:
        current_dir_size = get_directory_size(directory)
        if unused_space + current_dir_size >= 30000000:
            if result_dir_size is None or result_dir_size > current_dir_size:
                result_dir_size = current_dir_size
    return result_dir_size


def main():
    parse_input_and_build_directory()

    print('Part 1: ', part_one())
    print('Part 2: ', part_two())


if __name__ == "__main__":
    main()
