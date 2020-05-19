import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
   coin = random.randint(1, 2)
   if coin == guess:
     if coin == 1:
       coin = "head"
     else:
       coin = "tail"
     return "Congrats! the coin lands on " + coin + " you won " + str(bet) + " pesos. You now have a total money of " + str(money + bet)
   else:
     if coin == 1:
       coin = "head"
     else:
       coin = "tail"
       return "Better luck next time.. the coin lands on " + coin + " you lost " + str(bet) + ". Your total money is " + str(money - bet)


#Call your game of chance functions here
print(coin_flip(1, 30))