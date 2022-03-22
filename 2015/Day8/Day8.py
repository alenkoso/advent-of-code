string_literals = 0
in_memory_values = 0

# TODO: rethink how you could redo all this with eval()
# odštej char-e med sabo
with open("input.txt") as input:
    for row in input:
        data = row.strip()
        literal = len(data)
        memory = 0
        # ordinary:     0
        # backslash:    1
        # x:            2
        flag = 0

        for character in data[1:-1]:
            if flag == 0 and character == '\\':
                flag = 1
            elif flag == 1 and character == 'x':
                flag = 2
            elif flag == 2:
                flag = 3
            elif flag == 3:
                flag = 0
                memory += 1
            elif flag == 1:
                flag = 0
                memory += 1
            else:
                memory += 1

        string_literals += literal
        in_memory_values += memory

print("=============================== PART ONE ===============================")
print(
    "Disregarding the whitespace in the file, what is the number of characters of code \nfor string literals minus the number of characters in memory for the values of the strings in total for the entire file?\n")
print("String literals: ", string_literals)
print("In memory values: ", in_memory_values)
print("Difference: ", string_literals - in_memory_values)