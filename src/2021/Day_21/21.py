def parse_input(filename="input.txt"):
    with open(filename) as f:
        lines = f.readlines()
        # Extract just the numbers from each line
        p1_start = int(lines[0].strip().split(": ")[1])
        p2_start = int(lines[1].strip().split(": ")[1])
        return p1_start, p2_start

    class DeterministicDie:
        def __init__(self):
            self.value = 0
            self.rolls = 0

            def roll(self):
                self.value = (self.value % 100) + 1
                self.rolls += 1
                return self.value

            class Player:
                def __init__(self, position):
                    self.position = position
                    self.score = 0

                    def move(self, spaces):
                        # Move clockwise, wrapping around after 10
                        self.position = ((self.position + spaces - 1) % 10) + 1
                        self.score += self.position
                        return self.score

                    def play_deterministic_game(p1_start, p2_start):
                        # Initialize game state
                        die = DeterministicDie()
                        player1 = Player(p1_start)
                        player2 = Player(p2_start)

                        while True:
                            # Player 1's turn
                            roll_sum = die.roll() + die.roll() + die.roll()
                            if player1.move(roll_sum) >= 1000:
                                return player2.score * die.rolls

                            # Player 2's turn
                            roll_sum = die.roll() + die.roll() + die.roll()
                            if player2.move(roll_sum) >= 1000:
                                return player1.score * die.rolls

                            def main():
                                # Read starting positions from input.txt
                                p1_start, p2_start = parse_input()

                                # Calculate and print result
                                result = play_deterministic_game(p1_start, p2_start)
                                print(f"Part 1: {result}")

                                if __name__ == "__main__":
                                    main()

