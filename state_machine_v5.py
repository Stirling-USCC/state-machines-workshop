#!/usr/bin/env python

from typing import TypeVar, Callable, List, FrozenSet, Generic

I = TypeVar('I')
S = TypeVar('S')

class StateMachine(Generic[I,S]):

    def __init__(self
               , states : FrozenSet[S]
               , initial_state : S
               , input_alphabet : FrozenSet[I]
               , transition : Callable[[S,I],S]):

        if initial_state not in states:
            raise ValueError("Invalid initial state")

        self.states = states
        self.state = initial_state
        self.input_alphabet = input_alphabet
        self.transition = transition

    def run(self, input : List[I]):
        for c in input:
            if c in self.input_alphabet:
                self.state = self.transition(self.state,c)
            else:
                raise ValueError(f"{c} not in input alphabet!")

# Even Binary

input1 = "10001110101010101"        # 9 -- Odd
input2 = ""                         # 0 -- Even
input3 = "01010110101001000110"     # 9 -- Odd
input4 = "10110001"                 # 4 -- Even

def evenBinaryTransition(state : str, input : str):
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

machine = StateMachine(frozenset(["even", "odd"])
                     , "even"
                     , frozenset(["1","0"])
                     , evenBinaryTransition)
