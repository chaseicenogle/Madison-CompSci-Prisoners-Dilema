''' this file actually runs the tournament '''

''' Player 4 is your main guy. You can change this on line 12.
    Just add your players in the spaces, do not worry about creating many blank
    spaces for people. I can take care of that in the pull requests.'''

import prisoners_dilemma
def main():
    rounds = int(raw_input("Rounds: "))
    '''scores = []
    for _ in range(rounds):
        scores += [prisoners_dilemma.play_tournament(6, 4)]
    summ = 0
    for a in scores:
        summ += a
    print("Average: " + str(summ / rounds) + "\nPoints: " + str(summ))'''
    numberOfPlayers = int(raw_input("Number of Players: "))
    statisticsOnWhom = int(raw_input("Who should statistics be reported on?: "))
    print("Points for " + str(rounds) + "-ish rounds: " + str(prisoners_dilemma.play_tournament(numberOfPlayers, statisticsOnWhom, rounds)))
        
if __name__ == '__main__':
    main()