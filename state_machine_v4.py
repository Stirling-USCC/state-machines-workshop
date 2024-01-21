#!/usr/bin/env python

class StateMachine():

    def __init__(self, states, initial_state, input_alphabet, transition):

        self.states = states
        self.state = initial_state
        self.input_alphabet = input_alphabet
        self.transition = transition

    def run(self, input):
        for c in input:
            self.state = self.transition(self.state,c)

# Even Binary

input1 = "10001110101010101"        # 9 -- Odd
input2 = ""                         # 0 -- Even
input3 = "01010110101001000110"     # 9 -- Odd
input4 = "10110001"                 # 4 -- Even

def evenBinaryTransition(state, input):
    if state == "even":
        if input == "1":
            return "odd"
        else:
            return "even"
    else:
        if input == "1":
            return "even"
        else:
            return "odd"

machine = StateMachine(["even", "odd"], "even", ["1","0"], evenBinaryTransition)
