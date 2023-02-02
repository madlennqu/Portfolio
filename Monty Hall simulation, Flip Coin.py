#Monty Hall Simulation
# Suppose you're on a game show, and you're given the choice of three doors:
# Behind one door is a car; behind the others, goats.
#
# You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
# He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
#
# http://onlinestatbook.com/2/probability/monty_hall_demo.html


import random

def createSetup():
    doors = [False, False, False]
    doors[random.randint(0,2)] = True
    return doors


# Given your initial choice and whether you want to switch
def pick(choice,switch):
    doors = createSetup()
    if doors[choice]:
        if switch:
            return False
        else:
            return True

    else:
        if switch:
            return True
        else:
            return False

# return win rate
def simulation(switch,num_trial):
    win_count = 0
    for i in range(num_trial):
        if pick(random.randint(0,2),switch):
            win_count += 1
    return win_count/num_trial

print("Probability of Switching     {}".format(simulation(True, 100000)))
print("Probability of Not Switching {}".format(simulation(False, 100000)))


#Flip Coin
# Non bias Coin Flippling Game
#
# Win Odds = 2.03
# That means if you you bet 10, you will get back 20.3 when you win. i.e. you win 10.3 dollar

def play_game(win_odds, bet_amount):
    import random
    if random.randint(0,1):
        return win_odds * bet_amount
    else:
        return 0

def play_a_strategy(win_odds, starting_capital, bet_percentage, min_bet, num_bet):
    capital = starting_capital
    bet = capital * bet_percentage
    count_bet = 0

    while capital > min_bet and count_bet < num_bet:
        capital -= bet
        payout = play_game(win_odds, bet)

        capital += payout

        bet = capital * bet_percentage
        count_bet += 1

    return capital


def simulation(win_odds, starting_capital, bet_percentage, min_bet, num_bet, num_simulation):
    win_count = 0

    for i in range(num_simulation):
        result = play_a_strategy(win_odds, starting_capital, bet_percentage, min_bet, num_bet)
        if result > starting_capital:
            win_count += 1

    print("Win Rate {}".format(win_count/num_simulation))


simulation(2.1, 1000000, 0.01, 10, 3000, 500)

#https://www.youtube.com/watch?v=caQ41ivxO7Y
