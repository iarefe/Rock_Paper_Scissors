#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def __init__(self):
        self.score = 0
        self.my_move_ = random.choice(moves)
        self.their_move_ = random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move_ = my_move
        self.their_move_ = their_move
        return


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move_


class CyclePlayer(Player):
    def move(self):
        if self.my_move_ == 'rock':
            return 'paper'
        elif self.my_move_ == 'paper':
            return 'scissors'
        else:
            return 'rock'


class HumanPlayer(Player):
    def move(self):
        userinput = input('how u will be playing? rock or paper or'
                          + ' scissors? please make sure u write a'
                          + ' full word:  ').lower()
        if userinput == 'q':
            exit()
        elif userinput in moves:
            return userinput
        else:
            print('your input is wrong please rewrite it')
            return self.move()  # re callimg the function agien


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"you: {move1}  computer: {move2}")
        if beats(move1, move2):
            self.p1.score = self.p1.score + 1
            print(' you won X)')
        elif beats(move2, move1):
            self.p2.score = self.p2.score + 1
            print('Nooooo, you lose :(, Please win in the next game')
        else:
            print('Tied game')
        print(f"scores: you: {self.p1.score}  computer: {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("\nGame over! , now i well announce the winner: ")
        print(f"scores: you: {self.p1.score}  computer: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("you are the winner!!!!")
        elif self.p1.score < self.p2.score:
            print("you lose :( ")
        else:
            print('no winners')


def How_computer_will_be_play():
    typeOfGame = input('How would you like to make a computer play ?'
                       + ' random or reflect or cycler ?'
                       + 'please make sure u write a full word:  ').lower()
    if typeOfGame == 'random':
        return Game(HumanPlayer(), RandomPlayer())
    elif typeOfGame == 'reflect':
        return Game(HumanPlayer(), ReflectPlayer())
    elif typeOfGame == 'cycler':
        return Game(HumanPlayer(), CyclePlayer())
    else:
        print('your input is wrong please rewrite it')
        return How_computer_will_be_play()


if __name__ == '__main__':
    game = How_computer_will_be_play()
    game.play_game()
