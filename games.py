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


#Call your game of chance functions here
print(coin_flip('head', 90))
print(coin_flip('tail', 90))
print(cho_han('even', 50))