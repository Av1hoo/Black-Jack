#  ♠ ♡ ♢ ♣ ♤
import random

cards = []
for i in range(2, 11):
    cards.append(str(i) + "♠")
    cards.append(str(i) + "♡")
    cards.append(str(i) + "♣")
    cards.append(str(i) + "♢")

for i in ["J", "Q", "K", "A"]:
    cards.append(str(i) + "♠")
    cards.append(str(i) + "♡")
    cards.append(str(i) + "♣")
    cards.append(str(i) + "♢")

reset_deck = cards

def welcome():
    print(""""
    Welcome to black jack!
    The goal is to get a value of 21 or close of possible,
    2-10 value is as their number
    J,Q,K equal to 10
    A is 1 or 11 """)


def turn_1():
    global sum_1
    if sum_1 < 21:
        draw = input("Player 1 do you want to draw another card? y/n \n")
        if draw == "y":
            p1 = random.choice(cards)
            player1.append(p1)
            cards.remove(p1)
            if p1[0:2] == "10":
                sum_1 += 10
            elif p1[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                sum_1 += int(p1[0])
            elif p1[0] in ["J", "Q", "K"]:
                sum_1 += 10
            elif p1[0] == "A":
                if sum_1 <= 10:
                    sum_1 += 11
                else: # the sum would be more than 21
                    sum_1 += 1
            table = f"\t \t  Dealer:{sum_d} {dealer} \n \t \t - - - - - - - - - \n " \
                    f"P1:{sum_1} {player1} \t \t P2:{sum_2} {player2}"
            print(table)
            turn_1()
        elif draw == "n":
            pass
        else:
            print("Please etner a valid value.")
            turn_1()


def turn_2():
    global sum_2
    if sum_2 < 21:
        draw = input("Player 2 do you want to draw another card? y/n \n")
        if draw == "y":
            p2 = random.choice(cards)
            player2.append(p2)
            cards.remove(p2)
            if p2[0:2] == "10":
                sum_2 += 10
            elif p2[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                sum_2 += int(p2[0])
            elif p2[0] in ["J", "Q", "K"]:
                sum_2 += 10
            elif p2[0] == "A":
                if sum_2 <= 10:
                    sum_2 += 11
                else:
                    sum_2 += 1
            table = f"\t \t  Dealer:{sum_d} {dealer} \n \t \t - - - - - - - - - \n " \
                    f"P1:{sum_1} {player1} \t \t P2:{sum_2} {player2}"
            print(table)
            turn_2()
        elif draw == "n":
            pass
        else:
            print("Please etner a valid value.")
            turn_2()


print(*cards)

dealt, dealer, player1, player2 = [], [], [], []


def start():
    global dealer, player1, player2
    for a in range(6):
        fround = random.choice(cards)
        dealt.append(fround)
        cards.remove(fround)
    dealer = [dealt[0], dealt[3]]
    player1 = [dealt[1], dealt[4]]
    player2 = [dealt[2], dealt[5]]


sum_d, sum_1, sum_2 = 0, 0, 0


def sums():
    global sum_d, sum_1, sum_2
    for card in dealer:
        if card[0:2] == "10":
            sum_d += 10
        elif card[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
            sum_d += int(card[0])
        elif card[0] in ["J", "Q", "K"]:
            sum_d += 10
        elif card[0] == "A":
            if sum_d <= 10:
                sum_d += 11
            else:
                sum_d += 1
    for card in player1:
        if card[0:2] == "10":
            sum_1 += 10
        elif card[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
            sum_1 += int(card[0])
        elif card[0] in ["J", "Q", "K"]:
            sum_1 += 10
        elif card[0] == "A":
            if sum_1 <= 10:
                sum_1 += 11
            else:
                sum_1 += 1
    for card in player2:
        if card[0:2] == "10":
            sum_2 += 10
        elif card[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
            sum_2 += int(card[0])
        elif card[0] in ["J", "Q", "K"]:
            sum_2 += 10
        elif card[0] == "A":
            if sum_2 <= 10:
                sum_2 += 11
            else:
                sum_2 += 1
    table = f"\t \t  Dealer:{sum_d} {dealer} \n \t \t - - - - - - - - - \n" \
            f" P1:{sum_1} {player1} \t \t P2:{sum_2} {player2} "
    print(table)


def check_win():
    global sum_d, sum_1, sum_2
    if 22 > sum_1 > sum_d:
        print("Player 1 WON !")
    else:
        if sum_d < 22:
            print("Player 1 LOST !")
        elif sum_1 < 22:
            print("Player 1 WON !")
        else:
            print("Player 1 LOST !")
    if 22 > sum_2 > sum_d:
        print("Player 2 WON !")
    else:
        if sum_d < 22:
            print("Player 2 LOST !")
        elif sum_2 < 22:
            print("Player 2 WON !")
        else:
            print("Player 1 LOST !")


def another_d():
    global sum_d
    while sum_d < 18:
        dcard = random.choice(cards)
        dealer.append(dcard)
        cards.remove(dcard)
        if dcard[0:2] == "10":
            sum_d += 10
        elif dcard[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
            sum_d += int(dcard[0])
        elif dcard[0] in ["J", "Q", "K"]:
            sum_d += 10
        elif dcard[0] == "A":
            if sum_d <= 10:
                sum_d += 11
            else:
                sum_d += 1
    table = f"\t \t  Dealer:{sum_d} {dealer} \n \t \t - - - - - - - - - \n" \
            f" P1:{sum_1} {player1} \t \t P2:{sum_2} {player2} "
    print(table)


def reset():
    global sum_1, sum_2, sum_d, dealer, player1, player2, dealt
    sum_d, sum_1, sum_2 = 0, 0, 0
    dealer, player1, player2, dealt = [], [], [], []


def game():
    global cards
    start()
    sums()
    turn_1()
    turn_2()
    another_d()
    check_win()
    again = input("Another game? y/n \n")
    try:
        if again == "y":
            print("\n")
            print(cards)
            reset()
            game()
    except IndexError:
        print("Not enough cards. reshuffle")


game()

# table = f"\t \t  Dealer:{sum_d} {dealer} \n \t \t - - - - - - - - - \n
# P1:{sum_1} {player1} \t \t P2:{sum_2} {player2}"
# print(table)
