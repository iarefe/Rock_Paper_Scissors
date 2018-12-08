#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
choicefst=input("Choose how you want to play"" [ A-randomPlayer B-RepeatPlayer C-ReflectPlayer D- CyclerPlayer] ").lower()
moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""

class Player:
    def move(self):
        return 'rock'
    def __init__(self):
        self.scores=0
    def learn(self, my_move, their_move):



class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class RepeatPlayer(Player):
    def __init__(self):
        self.my_move=random.choice(moves)
    def move(self):
        return self.my_move


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move=random.choice(moves)
    def move(self):
        return self.their_move

class CyclerPlayer(Player):
    def move(self):
        pass

class HumanPlayer(Player):
    #move=input("what is your game:\n1-Rock\n2-paper\n3-scissors\n?"")
    #usermove.self
    def Humanuser(arg):
        pass
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
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    mode=input("select your mode:\n 1-RandomPlayer\n2-CyclerPlayer\n3-ReflectPlayer\n4-RepeatPlayer\n4-Player ").lower()
    game = Game(RandomPlayer(),mode)
    game.play_game()

"""
عندك خمس ألعاب وهي :
روك
دخل وحرد عليك راندوم
دخل والاولى حرد راندوم ثم بقعد أقلدك
دخل وحرد عليك بعشوائي واستمر ارد عليك به لنهاية اللوب
دخل وانا حرد بالترتيب بداية من الروك اى السكيوبمنت

لازم في البداية الهيومن يدخل نوع اللعبة

واذا دخل الهيومن نوع اللعبة لازم يدخل الان اداته

بالنسبة للعبة الأولى بطلب منك تدخل خيار وبرد عليك روك ودخل ثاني وارد عليك روك إلى نهاية الراندوم
بالنسبة للعبة الثانية بطلب منك تدخل خيار وبرد عليك بخيار من مخي وحتدخل انت وحدخل أنا من مخي الى نهاية الراندوم
بالنسبة للعبة الثالثة بطلب منك تدخل خيار وبرد عليك نفس ردك  وتدخل الثاني وادخل مثلك وهكذا (اشوف وش كتبت انت في اللعبة الاخيرة واكتب مثله)ا
بالنسبة للعبة الرابعة بطلب منك تدحل خبار وبرد عليك بالخيار الاول ثم دخل اي خيار وبرد عليك بالخيار الثاني وهكذا بالترتيب ارد عليك ( اشوف وش اخر شي انا نزلته وانزل غيره ) ا
جمع النقاط
احظ وش اخر لعبة لك
"""
