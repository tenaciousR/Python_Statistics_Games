import random num = random.randint(1, 6) money = 100



def dice_roll(guess, bet):

if bet > money or bet <= 0:
    print ("Sorry you can't do that")
    return 0 
if guess > 6 or guess < 1:
    print ("Pick a number within range of dice")
    return 0 

if guess == num:
    bet = bet * 3
    print("--------------")
    print ("You just won " + str(bet))
    print("--------------")
    return bet

if guess != num:
    print("--------------")
    print("Sorry you lost -" + str(bet))
    print("--------------")
    return -bet 
#dice_roll(4, 10) #coin flip game

def coin_flip(guess, bet): 
    if bet > money: 
      print ("Sorry you can't do that") 
      return 0 
 
if result == 1:
    print("Heads!")
elif result == 2:
    print("Tails!")
if (guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
    bet = bet * 2
    print("--------------") 
    print("You won {}".format(bet))
    return bet
else:
    print("--------------") 
    print("You lost {}".format(bet))
    return -bet

result = random.randint(1, 36)

if result == 37:
    print("--------------") 
    print("The wheel landed on 00")
else:
    print("--------------") 
    print("The wheel landed on " + str(result))

if guess == "Even" and result % 2 == 0 and guess != 0:
    bet = bet * 2
    print(str(result) + " is an even number")
    print("--------------") 
    print("You won " + str(bet))
    print("------------------")
    return bet

if guess == "Odd" and result % 2 == 1 and result != 37:
    print(str(result) + " is an odd number")
    print("--------------") 
    print("You won " + str(bet))
    print("------------------")
    return bet 

elif guess == result:
    bet = bet * 35
    print("The result was" + str(result))
    print (" you guessed exactly right! You won" + str(bet))
    print("------------------")
    return bet

else:
    print("------------------")
    print("The result was {}, sorry you lost {}".format(result, bet))
    print("------------------")
    return -bet 



compute bets & games played so far
money += dice_roll(6, 10)
money += coin_flip("Heads", 50)
money += roulette("Odd", 40)

print("Your total amount is $" + str(money))

