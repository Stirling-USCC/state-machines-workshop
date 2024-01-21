
# Finite Automata

## Introduction

### Outline of this Workshop

1. Motivation
2. Terminology
3. Theory
    - Finite State Machines
    - Regular Expressions
    - Finite State Transducers
4. Applications
    - State Machines in Python
    - Regexes
    - `re`
5. Exercises

### Prerequisites

- Basic Python

### Motivation

1. Many problems lend themselves to being modelled as state machines
    - TCP/IP
    - CPUs
2. Sometimes limiting your power is good!
3. Regexes, regexes, regexes!
4. CS theory baby steps

### Terminology

1. Sets
2. Relations & Functions
3. Strings & Languages

## Finite Automata & Regular Languages

### Models of Computation

- What *is* a computer? What does it *mean* to compute?
- Abstract, but **precisely** and **rigorously** defined computation
- Chomsky hierarchy

### Finite Automata

- Most basic model of computation
- Captures computation that uses *constant* memory
- Intuitive definition
- State diagrams
- Formal definition
- What does it mean for a finite automaton to compute?
- What can a finite automata do?
    - Where am I? (current state)
    - What just happened? (input)
- Specifically, it cannot —
    - Choose inconsistently
    - Decide "at runtime" where to transition
    - "Remember" previous input
    - Know if/when the end of the input is coming

#### Example: Even Number

- A finite automata that accepts a binary string if it represents an even number

#### Exercise: Even Binary

- Design a finite automata that accepts a binary string if it has an even number of 1s
- Design a finite automata that accepts a binary string if it has an even number of 1s and an even number of 0s
- Design a finite automata that accepts a binary string if it has an **equal** number of 1s and 0s

### Regular Languages

- Languages that are recognized by finite automata
- **Equivalent to finite automata**
- What makes a language regular? -- Exactly what makes a finite automaton a finite automaton
    - Can be decided "on the fly"
    - Don't need to store information about all input seen so far (only need current input)

#### Regular expressions

- An **algebra** for regular languages
- The regular operations -- Union, Kleene star, concatenation
- Constructing bigger regular languages from smaller ones

### RegEx

- Evolved out of regular expressions, but have diverged significantly since
- Most common implementations (Python, Perl, vim, etc.) can recognize more than regular languages
- Essential programming tool
- Used for **both** search / search & replace
	- Note that the second operation is, strictly speaking, impossible with finite automaton

### RegEx Blitz

- Strings
- Character Classes ('.', ranges, inverses)
- Repetition (?, \*, +, {n}, {n,},{,m},{n,m})
- Special Characters ([:alnum:], [:alpha:], [:lower:], [:upper:], [:digit:])
- The Regular Operations (concatenation, alternation)
- Anchors (^,$)

### Finite State Transducers

- Finite automata with a notion of "output"
- State diagrams
- What does it mean for a transducer to compute?
	- Transducers establish relations between sets of strings (languages)
- Formal definition
- Applications
	- Mostly computational linguistic
	- Compilers -- lexing

#### Video Game NPC

A finite state transducer that models a video game NPC for a turn based game ---

- The scenario -- the player is an adventurer and the NPC is a castle guard
- The input will be the player action -- {Talk, Attack}
- The output will be the NPC's action -- {Talk, Attack}

#### Exercise: Video Game NPC - Add Bribery Mechanic

Add a bribery mechanism to the guard --

- The input alphabet - {Talk, Bribe, Attack}
- The output alphabet - {Talk, Open Gate, Attack}
- When bribed, the guard should --
	- Stop attacking, if currently attacking
	- Open gate, if the player has *never* attacked the guard
	- Talk, if the player has *ever* attacked the guard

### Modelling State Machines in Python

#### Even Binary

- Five iterations, each demonstrating a general software design principle
	- 1 to 2 gives us encapsulation
	- 2 to 3 gives us more structure
	- 3 to 4 gives us reusability
	- 4 to 5 gives us "type safety" and error handling

#### Exercise: Video Game NPC

- Use what we just learnt to implement the video game NPC transducer in Python

### Using RegEx in Python: `re`

## Aside: More Theory

### Non-Deterministic Finite Automaton

### Equivalence of NDFAs and DFAs

### Closure of Regular Languages Under ∪, ○, *

### Thomson's Construction / Kleene's Construction

### Markov Chains

#### Page Rank

### Non-Regular Languages

## Exercises

### Model the HTTP Request/Response Flow as a FSA

### !! PROOFS !!

https://web.stanford.edu/class/archive/cs/cs103/cs103.1142/button-fsm/

http://raganwald.com/2018/02/23/forde.html

Michael Sipser's "Introduction to the Theory of Computation" Part 1, Chapter 1

https://regexr.com/

https://docs.python.org/3/library/re.html

https://www.regular-expressions.info/
