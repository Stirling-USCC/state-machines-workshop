#!/usr/bin/env python

from enum import Enum

class StateMachine:

    class State(Enum):
        EVEN = 0
        ODD = 1

    class Alphabet(Enum):
        ZERO = 0
        ONE = 1

    state = State.EVEN

    def transition(self, input):
        if self.state == StateMachine.State.EVEN:
            if input == StateMachine.Alphabet.ONE:
                self.state = StateMachine.State.ODD
            else:
                self.state = StateMachine.State.EVEN

        if self.state == StateMachine.State.ODD:
            if input == StateMachine.Alphabet.ZERO:
                self.state = StateMachine.State.EVEN
            else:
                self.state = StateMachine.State.ODD

    def run(self, input):
        for c in input:
            if c == "1":
                self.transition(StateMachine.Alphabet.ONE)
            elif c == "0":
                self.transition(StateMachine.Alphabet.ZERO)
            else:
                raise RuntimeError(f"Invalid input character: {c}")

statemachine1 = StateMachine()

input1 = "10001110101010101"        # 9 -- Odd
input2 = ""                         # 0 -- Even
input3 = "01010110101001000110"     # 9 -- Odd
input4 = "10110001"                 # 4 -- Even
