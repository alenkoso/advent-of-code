#!/usr/bin/env python3


def main():
    with open('../inputs/day4.txt') as input:
        print(part1(input))
    with open('../inputs/day4.txt') as input2:
        print(part2(input2))


def part1(input):
    randNums = []
    boards = []
    boardNum = 0
    boardData = {}
    boardLength = None

    for line in input:
        if len(randNums) == 0:
            for num in line.strip().split(','):
                randNums.append(int(num))
        else:
            if len(boards) == 0 and len(line.strip()) == 0:
                continue
            if len(line.strip()) == 0:
                boardNum += 1
                continue
            if boardLength is None:
                boardLength = len([i for i in line.split()])

            if boardNum == len(boards):
                boards.append([])

            boards[boardNum].append([[int(num), 0] for num in line.split()])

    bingo = False
    bingoSum = 0
    for num in randNums:
        for board in boards:
            board = mark_numbers(board, num)
            if check_board(board):
                bingo = True
                for row in board:
                    for x in row:
                        bingoSum += x[0] if x[1] == 0 else 0
                return bingoSum * num


def mark_numbers(board, n):
    for row in board:
        for num in row:
            if num[0] == n:
                num[1] = 1

    return board


def check_board(board):
    for row in board:
        sum = 0
        for num in row:
            sum += num[1]
        if sum == len(row):
            return True

    for i in range(len(board[0])):
        sum = 0
        for row in board:
            sum += row[i][1]
        if sum == len(board[0]):
            return True


def part2(input2):
    random_numbers = []
    boards = []
    board_numbers = 0
    board_data = {}
    board_length = None

    for line in input2:
        if len(random_numbers) == 0:
            for number in line.strip().split(','):
                random_numbers.append(int(number))
        else:
            if len(boards) == 0 and len(line.strip()) == 0:
                continue
            if len(line.strip()) == 0:
                board_numbers += 1
                continue
            if board_length is None:
                board_length = len([i for i in line.split()])

            if board_numbers == len(boards):
                boards.append([])

            boards[board_numbers].append([[int(num), 0] for num in line.split()])

    bingo = False
    bingo_num = 0
    bingo_sum = 0
    for number in random_numbers:
        for i in range(len(boards) - 1, -1, -1):
            board = boards[i]
            board = mark_numbers(board, number)
            if check_board(board):
                if len(boards) != 1:
                    boards.remove(board)
                else:
                    bingo_num = number
                    bingo = True
                    break
        if bingo:
            break

    for row in boards[0]:
        for number in row:
            bingo_sum += number[0] if number[1] == 0 else 0
    return bingo_sum * bingo_num


if __name__ == '__main__':
    main()
