#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: assignment8.py."""


import time
import argparse
import random
random.seed(0)


class Dice(object):
    """A dice object class definition."""

    def __init__(self):
        """Constructor for the dice() class."""
        self.result = 0

    def roll_dice(self):
        """Assigns a random number to the dice() object."""
        self.result = random.randint(1, 6)
        print "You have rolled a: ", str(self.result)
        return self.result

    def reset(self):
        """Assigns a zero to the result attribute of the dice() object."""
        self.result = 0


class Player(object):
    """A Player class definition."""

    def __init__(self, num):
        """Constructor for the Player() class."""
        self.id = str(1 + int(num))
        self.totalscore = 0

    def reset(self):
        """Resets the totalscore attribute to zero."""
        self.totalscore = 0

    def get_id(self):
        """Returns the id attribute."""
        return self.id

    def get_label(self):
        """Returns the id attribute."""
        return self.label

    def get_totalscore(self):
        """Returns the totalscore attribute."""
        return self.totalscore

    def print_totalscore(self):
        """Prints the totalscore attribute."""
        print "*Your Score is:", str(self.totalscore)
        return

    def getTempTotal(self, tempscore):
        """Calculates a temporary total score for the round."""
        return (self.totalscore + tempscore)

    def add_round_score(self, roundscore):
        """Updates the totalscore with the roundscore."""
        self.totalscore = self.totalscore + roundscore
        return


class ComputerPlayer(Player):
    """A Player class definition."""

    def __init__(self, num):
        """Constructor for the Player() class."""
        self.label = "computer"
        Player.__init__(self, num)

    def computer_test(self, roundscore):
        """Decides to hold or roll again."""
        x = self.totalscore
        y = roundscore
        limit = 100 - x
        if (y >= 25) or (y >= limit):
            return True
        else:
            return False

    def get_label(self):
        """Returns the id attribute."""
        return self.label


class HumanPlayer(Player):
    """A Player class definition."""

    def __init__(self, num):
        """Constructor for the Player() class."""
        self.label = "human"
        Player.__init__(self, num)

    def get_label(self):
        """Returns the attribute."""
        return self.label


class PlayerFactory(object):
    """A PlayerFactory class definition."""

    def __init__(self):
        """Constructor for the PlayerFactory() class."""
        self.confirm = "yes"

    def getPlayer(self, num, choice):
        """Determines assignment to Player() class."""
        if choice.lower() == "human":
            return HumanPlayer(num)
        if choice.lower() == "computer":
            return ComputerPlayer(num)


class PIGSgame(object):
    """A PIGS game class definition."""

    def __init__(self, ch1, ch2, timed=False):
        """Constructor for the PIGSgame() class.

        Args:
            num(integer): The number of players in the game. Default: 2

        Attributes:
            mydice (object): The dice() object.
            endgame (boolean): A boolean to determine if the game continues on.
            player_list (list): A list of Player() objects.
        """
        self.timed = timed
        self.mydice = Dice()
        endgame = False
        self.p_list = []
        player_list = self.p_list

        myfactory = PlayerFactory()
        tempchar1 = str(ch1)
        num1 = 0
        tmp_player1 = myfactory.getPlayer(num1, tempchar1)
        player_list.append(tmp_player1)

        tempchar2 = str(ch2)
        num2 = 1
        tmp_player2 = myfactory.getPlayer(num2, tempchar2)
        player_list.append(tmp_player2)

        while not endgame:
            for b in range(2):
                p_type = player_list[b].get_label()
                if p_type == "computer":
                    endgame = self.play_cmp_round(player_list[b])
                elif p_type == "human":
                    endgame = self.play_round(player_list[b])
                if endgame is True:
                    break

        self.mydice.reset()
        for c in range(2):
            player_list[c].reset()

    def play_cmp_round(self, gameplayer):
        """A function that rolls the dice and prints the round score for a
            computer player.

        Args:
            gameplayer(object): The Player() object.

        Attributes:
            temp_player (string): The id of the Player() object.
            score (integer): The score based on the dice() object.
            round_score (integer): The total round score.
            endgame, endturn (boolean): A boolean to continue the loop.
        """
        temp_player = gameplayer.get_id()
        round_score = 0
        endgame = False
        endturn = False
        print "Computer:", temp_player + "'s turn to roll."

        while not endturn and not endgame:
            gameplayer.print_totalscore()
            print "The Computer chooses to roll the dice."
            score = self.mydice.roll_dice()
            if score == 1:
                print "Sorry, Computer has lost the turn!"
                gameplayer.print_totalscore()
                print "-------------------------"
                round_score = 0
                endturn = True
            else:
                round_score = round_score + score
                print "*Computer Current Round Score is:", str(round_score)
                temp_total = gameplayer.getTempTotal(round_score)
                if temp_total >= 100:
                    gameplayer.add_round_score(round_score)
                    gameplayer.print_totalscore()
                    print "Congratulations! "
                    print "Computer:", temp_player + " is the Winner!"
                    endgame = True
                elif gameplayer.computer_test(round_score):
                    print "The Computer has chosen to hold"
                    gameplayer.add_round_score(round_score)
                    gameplayer.print_totalscore()
                    print "-------------------------"
                    endturn = True
        return endgame

    def play_round(self, gameplayer):
        """A function that rolls the dice and prints the round score.

        Args:
            gameplayer(object): The Player() object.

        Attributes:
            temp_player (string): The id of the Player() object.
            score (integer): The score based on the dice() object.
            round_score (integer): The total round score.
            endgame, endturn (boolean): A boolean to continue the loop.
        """
        temp_player = gameplayer.get_id()
        round_score = 0
        endgame = False
        endturn = False
        print "Player:", temp_player + "'s turn to roll."
        while not endturn and not endgame:
            gameplayer.print_totalscore()
            answer = raw_input("Type R to ROLL the dice or H to HOLD: ")
            if answer.lower() == "r":
                score = self.mydice.roll_dice()
                if score == 1:
                    print "Sorry, You have lost your turn!"
                    gameplayer.print_totalscore()
                    print "-------------------------"
                    round_score = 0
                    endturn = True
                else:
                    round_score = round_score + score
                    print "*Your Current Round Score is:", str(round_score)
                    temp_total = gameplayer.getTempTotal(round_score)
                    if temp_total >= 100:
                        gameplayer.add_round_score(round_score)
                        gameplayer.print_totalscore()
                        print "Congratulations! "
                        print "Player:", temp_player + " is the Winner!"
                        endgame = True
            elif answer.lower() == "h":
                print "You have selected to hold"
                gameplayer.add_round_score(round_score)
                gameplayer.print_totalscore()
                print "-------------------------"
                endturn = True
            else:
                print "Error: Please select R or H."
            if self.timed and not endgame:
                endgame = self.timertest()
        return endgame


class TimedGameProxy(PIGSgame):
    """A PIGS game proxy definition."""

    def __init__(self, ch1, ch2):
        """Constructor for the TimedGameProxy() class."""
        timed = True
        self.start = time.time()
        PIGSgame.__init__(self, ch1, ch2, timed)

    def timertest(self):
        now = time.time()
        if (now-self.start) > 60:
            print "-------------------------"
            print "Sorry, Time Expired!"
            score1 = self.p_list[0].get_totalscore()
            score2 = self.p_list[1].get_totalscore()
            if score1 > score2:
                print "Player: 1 is the Winner!"
            elif score2 > score1:
                print "Player: 2 is the Winner!"
            else:
                print "Tie, No Winner!"
            return True
        else:
            return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Choose Human or Computer:")
    parser.add_argument("-n1", "--player1", help="Choose Human or Computer")
    parser.add_argument("-n2", "--player2", help="Choose Human or Computer")
    parser.add_argument("-t", "--timed", help="Choose to activate time proxy")
    args = parser.parse_args()

    if args.timed:
        p1 = args.player1
        p2 = args.player2
        TimedGameProxy(p1, p2)
    elif args:
        p1 = args.player1
        p2 = args.player2
        PIGSgame(p1, p2)
