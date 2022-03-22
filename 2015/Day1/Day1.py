with open("input.txt") as input:
    # stevec za nadstropja
    # sprehod cez vrstice input, nato skozi znake v vrsticah
    # za vsak ( prišteješ floor, za vsak ) odšteješ floor
    floor = 0
    basement_index_position = 0
    # Part 1:
    for row in input:
        for character in row:
            if character == '(':
                floor += 1
            else:
                floor -= 1
            basement_index_position += 1
            if floor == -1:  # Part 2
                print("The position of the character that causes Santa to first enter the basement: ",
                      basement_index_position)
    print("Floor: ", floor)

# TODO: stop the printing of basement position after the first catch

