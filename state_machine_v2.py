#!/usr/bin/env python

class StateMachine:

    def __init__(self):
        self.state = "even"

    def transition(self, input):

        if self.state == "even":
            if input == "1":
                self.state = "odd"
                return
            else:
                self.state = "even"
                return

        if self.state == "odd":
            if input == "1":
                self.state = "even"
                return
            else:
                self.state = "odd"
                return

    def run(self, input):

        for c in input:
            self.transition(c)

statemachine1 = StateMachine()

input1 = "10001110101010101"        # 9 -- Odd
input2 = ""                         # 0 -- Even
input3 = "01010110101001000110"     # 9 -- Odd
input4 = "10110001"                 # 4 -- Even
