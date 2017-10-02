trans_probs = [
        ('a','a',0.9),
        ('a','b',0.075),
        ('a','c',0.025),
        ('b','a',0.15),
        ('b','b',0.8),
        ('b','c',0.05),
        ('c','a',0.25),
        ('c','b',0.25),
        ('c','c',0.5)
        ]

# Starting from state 'a', simulate 1000 transitions in the Markov chain
# and print out how many times each state was transitioned to.

import random

transitionStates = {} # key: name of state, value: counts of transitions

def markovChain_simulator(startState='a', prob=1.0, rounds=1000):
        if rounds <= 0:
            return
                    
        for state in trans_probs:
            if startState == state[0]:
                #print 'DEBUG:', state, rounds
                if state[1] not in transitionStates:
                    transitionStates[state[1]] = 0.0
                transitionStates[state[1]] += state[2] * prob

                markovChain_simulator(state[1], state[2], rounds-1)       



if __name__ == '__main__':
    markovChain_simulator(rounds=20)
    print transitionStates
