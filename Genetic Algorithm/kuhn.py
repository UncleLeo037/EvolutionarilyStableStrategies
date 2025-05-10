import random

ROUNDS = 9
BANKROLL = 9

def poker(population):
    for _ in range(ROUNDS):
        random.shuffle(population)
        new_population = []
        for i in range(0, len(population)-1, 2):
            p1 = population[i]
            p2 = population[i+1]
            
            #Each player antes 1
            p1[1] -= 1
            p2[1] -= 1
            pot = 2

            #Each player is dealt one of the three cards
            c1, c2 = random.sample(range(3), 2)

            s1 = bin(int(p1[0][c1]))[2:].zfill(2)
            s2 = bin(int(p2[0][c2+3]))[2:].zfill(2)
            
            #Player one can check or bet 1
            if (int(s1[0]) and p1[1] > 0):
                p1[1] -= 1
                pot += 1
                #If player one bets then player two can fold or call
                if (int(s2[1]) and p2[1] > 0):
                    p2[1] -= 1
                    pot += 1
                #If player two folds the player one gets the pot
                else:
                    p1[1] += pot
                    pot = 0
            #If player one checks then player two can check or bet 1
            elif (int(s2[0]) and p2[1] > 0):
                p2[1] -= 1
                pot += 1
                #If player two bets then player one can fold or call
                if(int(s1[1]) and p1[1] > 0):
                    p1[1] -= 1
                    pot += 1
                #If player one folds the player two gets the pot
                else:
                    p2[1] += pot
                    pot = 0
            #showdown for the pot
            if (c1 > c2):
                p1[1] += pot
            if (c1 < c2):
                p2[1] += pot
            
            if (p1[1] > 0):
                new_population.append(p1)
            if (p2[1] > 0):
                new_population.append(p2)
        population = new_population
    return population
