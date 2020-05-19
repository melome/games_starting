import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
   coin = random.randint(1, 2)
   if coin == 1:
       coin = "head"
   else:
       coin = "tail"
   if coin == guess:
     return "Congrats! the coin lands on " + coin + " you won " + str(bet) + " pesos. You now have a total money of " + str(money + bet)
   else:
     return "Better luck next time.. the coin lands on " + coin + " you lost " + str(bet) + ". Your total money is " + str(money - bet)

def cho_han(guess, bet):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    if (total % 2) == 0:
        dice = "even"
    else:
        dice = "odd"
    if dice == guess:
        return "Congrats! the dice is " + dice + " you won " + str(
            bet) + " pesos. You now have a total money of " + str(money + bet)
    else:
        return "Better luck next time.. the dice is " + dice + ", you lost " + str(
            bet) + ". Your total money is " + str(money - bet)

def highest_card(plyr1_bet, plyr2_bet):
    drawn_cards = []
    plyr1_card = random.randint(1, 13)
    plyr2_card = random.randint(1, 13)
    while (drawn_cards.count(plyr1_card) != 1) and (drawn_cards.count(plyr2_card) != 1):
        drawn_cards.append(plyr1_card)
        drawn_cards.append(plyr2_card)

    if(plyr1_card > plyr2_card):
        return "Player1 won! with " + str(plyr1_card)
    else:
        return "Player2 won! with " + str(plyr2_card)

def roulette(guess, bet):
    number = random.randint(1,10)
    if number == guess:
        if number % 2 == 0:
            return "You won! " + str(bet*2) + ". Total money is equal to " + str(money + bet)
        else:
            return "You won! " + str(bet) + ". Total money is equal to " + str(money + bet)
    else:
        return "Try again next time. You lost " + str(bet) + " pesos. " + "your reamaining money is " + str(money-bet) + " pesos"

#Call your game of chance functions here
print(coin_flip('head', 90))
print(coin_flip('tail', 90))
print(cho_han('even', 50))
print(highest_card(50,20))
print(roulette(1, 50))