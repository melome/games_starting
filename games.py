import random

money = 1000


# Write your game of chance functions here
def coin_flip(guess, bet):
    if(bet <= money):
        while(guess == 'head') or (guess == 'tail'):
            coin = random.randint(1, 2)
            if coin == 1:
                coin = "head"
            else:
                coin = "tail"
            if coin == guess:
                print("Congrats! the coin lands on " + coin + " you won " + str(
                    bet) + " pesos. You now have a total money of " + str(money + bet))
                return bet
            else:
                print("Better luck next time.. the coin lands on " + coin + ", you lost " + str(
                    bet) + " pesos. Your total money is " + str(money - bet))
                return bet * -1
        else:
            print('TIP: When guessing, choose only "head" or "tail".')
            return 0
    else:
        print("You do not have enough money")
        return 0

def cho_han(guess, bet):
    if(bet <= money):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        if (total % 2) == 0:
            dice = "even"
        else:
            dice = "odd"
        if dice == guess:
            print("Congrats! the dice is " + dice + " you won " + str(
                bet) + " pesos. You now have a total money of " + str(money + bet))
            return bet
        else:
            print("Better luck next time.. the dice is " + dice + ", you lost " + str(
                bet) + ". Your total money is " + str(money - bet))
            return bet * -1
    else:
        print("You do not have enough money")
        return 0


def highest_card(bet):
    plyr2_bet = random.randint(1, 100)
    if(bet <= money):
        drawn_cards = []
        plyr1_card = random.randint(1, 13)
        plyr2_card = random.randint(1, 13)
        while (drawn_cards.count(plyr1_card) != 1) and (drawn_cards.count(plyr2_card) != 1):
            drawn_cards.append(plyr1_card)
            drawn_cards.append(plyr2_card)

        if (plyr1_card > plyr2_card):
            print("You won with number " + str(plyr1_card) + " card." + " You will go home with " + (bet+plyr2_bet))
            return bet + plyr2_bet
        elif (plyr1_card < plyr2_card):
            print("Player2 won! with " + str(plyr2_card) + " card." + " You will go home with " + (bet+plyr2_bet))
            return plyr2_bet + bet
        else:
            print("Draw!")
            return bet
    else:
        print("You do not have enough money")
        return 0

def roulette(guess, bet):
    if(bet <= money):
        number = random.randint(1, 10)
        if number == guess:
            if number % 2 == 0:
                print("You won! " + str(bet * 2) + ". Total money is equal to " + str(money + bet))
                money_won = bet * 2
                return money_won
            else:
                print("You won! " + str(bet) + ". Total money is equal to " + str(money + bet))
                return bet
        else:
            print("Try again next time. You lost " + str(bet) + " pesos. " + "your remaining money is " + str(
                money - bet) + " pesos")
            return bet * -1
    else:
        print("You do not have enough money")
        return 0



# Call your game of chance functions here
money += (coin_flip("head", 240))
money += (roulette(4, 100))
