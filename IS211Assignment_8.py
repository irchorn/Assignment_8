import random
import argparse


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def __str__(self):
        return f"{self.name} has {self.total}points"

    def play(self):
        turn_total = 0
        while True:
            turn_input = input(f'{self.name}, do you want to roll or hold? ')
            if turn_input == 'r':
                die_value = random.randint(1, 6)
                if die_value == 1:
                    print(f"{self.name} you roll a 1. Your score for this round is 0")
                    print("----------------------------------------------------------------")
                    return
                else:
                    print(f"{self.name} you roll a {die_value}.")
                    turn_total += die_value
                    if turn_total + self.total >= 100:
                        self.total += turn_total
                        return

                    print(f"Your turn score is {turn_total}")
                    print(f"Your possible score if you hold is {turn_total + self.total}")
            elif turn_input == 'h':
                self.total += turn_total
                print(f"Your score is {self.total}. Turn is over")
                print("----------------------------------------------------------------")
                return


class ComputerPlayer(Player):

    def play(self):
        turn_total = 0
        while True:
            if turn_total > min(25, 100 - self.total):
                # Hold
                self.total += turn_total
                print(f"Your score is {self.total}. Turn is over")
                print("----------------------------------------------------------------")
                return
            else:
                die_value = random.randint(1, 6)
                if die_value == 1:
                    print(f"{self.name} you roll a 1. Your score for this round is 0")
                    print("----------------------------------------------------------------")
                    return
                else:
                    print(f"{self.name} you roll a {die_value}.")
                    turn_total += die_value
                    if turn_total + self.total >= 100:
                        self.total += turn_total
                        return
                    print(f"Your turn score is {turn_total}")
                    print(f"Your possible score if you hold is {turn_total + self.total}")


def factory(player_type):
    if player_type == 'computer':
        return ComputerPlayer("")
    else:
        return Player("")


class Game:
    def __init__(self, name1, name2):
        self.players = [ComputerPlayer(name1), ComputerPlayer(name2)]
        self.turn_total = 0
        self.total = 0
        self.current_player = 0

    def next_player(self):
        if self.current_player + 1 == len(self.players):
            self.current_player = 0
        else:
            self.current_player += 1

    def play(self):
        turn_total = 0
        while self.players[0].total < 100 and self.players[1].total < 100:
            self.players[self.current_player].play()
            if self.players[self.current_player].total >= 100:
                print(f"{self.players[self.current_player].name} you are the WINNER.")
                print(f"Your winning score is {self.players[self.current_player].total}")
                return
            else:
                self.next_player()

class TimedGameProxy(Game):
    def __init__(self, name1, name2, timed):
        self.timed = timed
        self.players = [ComputerPlayer(name1), ComputerPlayer(name2)]
        self.turn_total = 0
        self.total = 0
        self.current_player = 0

    def next_player(self):
        if self.current_player + 1 == len(self.players):
           self.current_player = 0
        else:
           self.current_player += 1

    def play(self):
        turn_total = 0
        while self.players[0].total < 100 and self.players[1].total < 100 and self.timed < 60:
            self.players[self.current_player].play()
            if self.players[self.current_player].total >= 100:
                print(f"{self.players[self.current_player].name} you are the WINNER.")
                print(f"Your winning score is {self.players[self.current_player].total}")
            else:
                self.next_player()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Play game")
    parser.add_argument('--Player', action='store_true',
                        help='specifying the player')
    args = parser.parse_args()
    if args.Player:
        Player()
    else:
        ComputerPlayer(Player)

    my_game = Game(factory(player_type='computer'), 'John')
    my_game.play()

    timed_proxy = TimedGameProxy("John", "Michael", 0)
    timed_proxy.play()

main()
