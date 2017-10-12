trans_probs = [
    ('a', 'a', 0.9),
    ('a', 'b', 0.075),
    ('a', 'c', 0.025),
    ('b', 'a', 0.15),
    ('b', 'b', 0.3),
    ('b', 'c', 0.55),
    ('c', 'a', 0.4),
    ('c', 'b', 0.5),
    ('c', 'c', 0.1)
]

# Starting from state 'a', simulate 1000 transitions in the Markov chain
# and print out how many times each state was transitioned to.

import random
import numpy as np


def markovChain_simulator(startStates, rounds=1000):
    if rounds <= 0:
        return startStates

    endStates = {}
    for k, v in startStates.iteritems():
        for state in trans_probs:
            if k == state[0]:
                # print 'DEBUG:', state, rounds
                if state[1] not in endStates:
                    endStates[state[1]] = 0.0

                endStates[state[1]] += startStates[state[0]] * state[2]

    return markovChain_simulator(endStates, rounds - 1)


def convert_transitionM(trans_probs):
    states = set()
    for s in trans_probs:
        states.add(s[0])
        states.add(s[1])

    N = len(states)
    ind_dict = {}

    for cnt, s in enumerate(sorted(list(states))):
        ind_dict[s] = cnt

    trans_M = []
    for i in xrange(N):
        trans_M.append([0 for i in xrange(N)])

    for s in trans_probs:
        row = ind_dict[s[0]]
        col = ind_dict[s[1]]
        trans_M[row][col] = s[2]

    return np.array(trans_M)


def markovChain_transitionM(startState, trans_M, rounds=1000):
    assert type(startState) is np.ndarray and \
        type(trans_M) is np.ndarray, \
        'check your input types'

    metaState = startState
    count_state = startState

    for i in xrange(rounds):
        print metaState
        metaState = np.transpose(trans_M).dot(metaState)
        print metaState
        count_state = metaState + count_state

    return count_state


if __name__ == '__main__':
    # recursive
    print 'Recursive:'
    # key: name of state, value: counts of transitions
    transitionStates = {'a': 1., 'b': 0., 'c': 0.}
    print markovChain_simulator(transitionStates, rounds=10)

    # matrix multiplication
    trans_matrix = convert_transitionM(trans_probs)
    print 'Matrix multiplication:'
    print markovChain_transitionM(np.array([1, 0, 0]), trans_matrix, rounds=10)
