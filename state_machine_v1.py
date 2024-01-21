#!/usr/bin/env python

input1 = "10001110101010101"        # 9 -- Odd
input2 = ""                         # 0 -- Even
input3 = "01010110101001000110"     # 9 -- Odd
input4 = "10110001"                 # 4 -- Even

def transition(state, input):

    if state == "even":
        if input == "1":
            return "odd"
        else:
            return "even"


    if state == "odd":
        if input == "1":
            return "even"
        else:
            return "odd"

def run(input):

    state = "even"

    for c in input:
        state = transition(state, c)

    return state
