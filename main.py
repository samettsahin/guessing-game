import random


class Number:
    def __init__(self):
        self.value = random.randint(1, 99)

    def is_even(self):
        return self.value % 2 == 0

    def check_guess(self, user_number):
        return self.value == user_number


class Score:
    def __init__(self):
        self.value = 10

    def decrease(self):
        self.value -= 1

    def show(self):
        print(f"Your score {self.value}")

    def is_zero(self):
        return self.value == 0


class User:
    def get_input(self):
        return input("guess the number please: ")


class Game:
    def __init__(self):
        self.number = Number()
        self.score = Score()
        self.user = User()

    def start(self):
        print("the game is started")

        while True:
            user_input = self.user.get_input()

            if user_input == "exit":
                break

            elif user_input == "is the number even":
                if self.number.is_even():
                    print("The number is even")
                else:
                    print("The number is odd")

            else:
                user_number = int(user_input)

                if self.number.check_guess(user_number):
                    print("You won nice")
                    self.score.show()
                    break
                else:
                    print("You lose,try next time")
                    print("-1")
                    self.score.decrease()

                    if self.score.is_zero():
                        print("Game over")
                        print(f"The correct number was {self.number.value}")
                        break


if __name__ == "__main__":
    game = Game()
    game.start()