# State Machines & Regular Expressions

## Introduction

- What *is* a computer? What does it *mean* to compute?
- How do we talk about computation in a *grounded* manner
	- i.e., unambiguous and rigorously defined
- What is a model of a computer? What are the different models of computation?
- Why would we choose one model of computation over another?

## Outline

- Motivation
- Terminology
- Finite Automata
- Regular Languages
- RegEx
- Finite State Transducers
- Modelling State Machines in Python
- RegEx in Python
- More Theory

## Motivation

- Sometimes limiting your power is good!
- Many problems lend themselves to being modelled as state machines
	- TCP/IP
	- CPUs
- Regexes, regexes, regexes!
- CS theory baby steps

<Image: A state-diagram of the TCP/IP request flow showing states labelled "closed", "listen", "syn-rcvd", etc and state transition arrows labelled "passive", "syn sent", "fin/ack", etc>
<Image: A state-diagram of a CPU showing states labelled "loadstore", "start_2", "exception_0", etc and unlabelled state transition arrows>

## Terminology: Sets & Sequences

- Sets: Collections of objects; order does not matter and repetition is meaningless
	- $\{1,2,3\}$
	- $\{a,b,c, \{x, y, z\}\}$
	- $\{1,2,3\} = \{1,3,2\} = \{1,2,2,3\}$
- Sequences/Tuples: Collections of objects; order matters and repetition is meaningful
	- $(1,2,3)$
	- $(1,2,3) ≠ (1,3,2) ≠ (1,2,2,3)$

## Terminology: Functions

- $f : A \rightarrow B$ is a function from (the set) $A$ to (the set) $B$
- Associate each object in a set (domain) to at most one object in another set (codomain)
- Two objects in the domain may be associated to the same object in the range
- An object in the domain may be associated to only one object in the range
- Not all objects in the range may be associate-to by an object in the domain

## Terminology: Strings & Languages

- String: Any sequence of characters drawn from a set of symbols, or alphabet, conventionally denoted $\Sigma$
- Language: A non-empty set of strings. For $\Sigma = \{a,b,c,d\}$
	- $abcd$, $acccdba$, $a$, are all strings
	- $\varepsilon$ is the empty string (Note $\emptyset \ne \{\varepsilon\}$)
	- $L_1 = \{abcd,abbcccdddd\}$, $L_2 = \{a,b,bb,c,cc,ccc\}$, and $L_3 = \{\varepsilon\}$are examples of languages over $\Sigma$

# Finite Automata & Regular Languages

## Finite Automata

- A limited form of computation
- Models computation that takes constant/no memory
- Alphabet
- States
- Transitions
- Initial state
- Final state(s)
- What does it mean for a finite automaton to compute?

## Intuitive Definition

<Image: A state diagram modelling a candy dispenser. The states are "Closed" and "Open". There is a transition arrow from "Closed" to "Open" labelled "Insert Coin" and a transition arrow from "Open" to "Closed" labelled "Dispense Candy">
<Image: An image of a candy dispenser>

## Formal Definition

-  $M = (\Sigma, Q, q_0, F, \delta)$ is a finite state automaton
	- $\Sigma$ – Alphabet / set of symbols
	- $Q$ – (non-empty , finite) set of states
	- $q_0$ - start state
	- $F$ – set of accepting states
	- $\delta : \Sigma \times Q \rightarrow Q$ – transition function
- Computation is defined in terms of strings that a machine accepts. $M$ accepts a string $w_1w_2 \dots w_n$ if a sequence of states $r_0r_1 \dots r_n$ exists in $Q$ such that
	- $r_0 = w_0$
	- $\delta(r_i,w_{i+1}) = r_{i+1}$ for $i = 1,2 \dots n-1$
	- $r_n \in F$
- $M$ is said to recognize a language $L$ if it accepts all strings in $L$

## What makes an FSA finite?

- What can a finite automata do?
	- Where am I? (current state)
	- What just happened? (input)
- Specifically, it cannot —
	- Choose inconsistently
	- Decide "at runtime" where to transition
	- "Remember" previous input
	- Know if/when the end of the input is coming

## Example: Even Number

- A state machine that recognizes when a binary string represents an even number

<Image: A state diagram with states q0 and q1. q0 is the start state. q0 goes to q1 on input 1 and stays on q0 on input 0. q1 goes to q0 on input 0 and stays on q1 on input 1. q1 is the accept state>

## Remember

- There must be start state
- Each state must have one and only one arrow going out of it for each symbol in the alphabet
- There may or may not be an accept state (although, not having one is not very useful)

## Excercise: Even Binary

- Design a state machine that checks if a binary number has an even number of ones. $\Sigma = \{0,1\}$
- Hint: You do not need the machine to count how many ones there are in the string, just whether or not it has an even number of ones

## Regular Languages

- Languages recognized by a finite automaton
- Each finite automata *defines* a regular language
- What makes a regular language regular?
	- Exactly what makes a finite automaton finite

## Regular Expressions

- An algebra for regular languages
- The regular operations –
	- Union
	- Kleene Star
	- Concatenation
- Construct bigger regular languages from smaller regular languages

## Regular Expressions

- $R$ is a regular expression if $R$ is ($R_1$ and $R_2$ are other regular expressions)
	- $a$ for some $a \in \Sigma$
	- $\varepsilon$
	- $\emptyset$
	- $(R_1 \cup R_2)$
	- $(R_1 \circ R_2)$
	- $(R_1 \ast)$

# RegEx

## What is a RegEx?

- One of the most useful things FSAs do is recognize patterns in strings
	- This is almost a literal programming equivalent of language recognition
- RegEx evolved out of regular expressions, but have diverged significantly since
	- Most common implementations can recognize more than just regular languages

## RegEx Blitz

- Strings (.)
- Character Classes ([], ^)
- Repetition (?, *, +, {n}, {n,},{,m},{n,m})
- Pre-defined character classes (\d, \D, \s, \S, \w, \W)
- The Regular Operations (concatenation, alternation)
- Anchors (^,$)

# Finite State Tranducers

## Finite State Transducers

- Finite automata with a notion of "output"
- What does it mean for a transducer to compute?
	- Transducers establish relations between sets of strings (languages)
- Formal definition
- Applications
	- Mostly computational linguistic
	- Compilers - lexing

## Formal Definition

- $M = (\Sigma, \Gamma, Q, q_0, \delta)$ is a finite state transducer
- $\Sigma$ – Alphabet
- $\Gamma$ – Output alphabet
- $Q$ – (non-empty, finite) set of states
- $q_0$ - start state
- $\delta : \Sigma \times Q \rightarrow Q \times Q$ – transition function
- Computation is repeated application of $\delta$ to a sequence of symbols, from a starting state, to generate an output string

## What does this do?

<Image: A state diagram with a single state q which transitions to itself with output 1 when input 0 and transitions to itself with output 0 when input 1>

## Example: Video Game NPC

- A finite state transducer that models a video game NPC for a turn based game. The scenario - the player is an adventurer and the NPC is a castle guard.
- $\Sigma = \{TALK, ATTACK\}$
- $\Gamma = \{TALK, ATTACK\}$

## Excercise: Video Game NPC - Add Bribery Mechanism

- Add a bribery mechanism to the guard –
- When bribed, the guard should --
	- Stop attacking, if currently attacking
	- Open gate, if the player has never attacked the guard
	- Talk, if the player has ever attacked the guard
- $\Sigma = \{TALK, BRIBE, ATTACK\}$
- $\Gamma = \{TALK, OPEN GATE, ATTACK\}$

# Applications

## Modelling State Machines in Python

- Five iterations, each demonstrating a general software design principle
	- 1 is the basic implementation
	- 2 gives us encapsulation
	- 3 gives us more structure
	- 4 gives us reusability
	- 5 gives us "type safety" and error handling

## Exercise: Video Game NPC

- Using what we learned, implement a finite state transducer that models the video game NPC (either version)

## RegEx in Python

- Python’s standard library has the module `re` which provides RegEx functionality
	- Basic workflow
	- `import re`
	- `compile`
	- `match`/`search`/`findall`/`finditer`
	- Match Objects
	- `group`/`start`/`end`/`span`

# More Theory

## Non-Deterministic FSA

- Jump to many states “at once” while consuming a single symbol
- Makes many state machines simpler to design (but more complex to implement)
- Equivalent to (i.e., no more powerful than a deterministic FSA)

## Closure of Regular Languages under the Regular Operations

- Non-Deterministic FSAs lead to elegant proofs of the closure of regular languages under the regular operations

<Image: A image showing how NDFAs can prove that regular expressions are closed under union>
<Image: A image showing how NDFAs can prove that regular expressions are closed under concatenation>
<Image: A image showing how NDFAs can prove that regular expressions are closed under kleene star>

## Markov Chains

- Weighted FSA
- Transitions are tagged with probabilities
- Primitive text generation
- Google’s PageRank

## Non-Regular Languages

- Some languages cannot be recognized by FSA (non-deterministic or otherwise)

<Image: A hierarchy of automata and the languages they recognize. At the bottom are fintie automata, recognizing regular languages; then push-down automata, recognizing context-free languages; then linear-bounded automata recognizing context-sensitive languages; then turing machines, recognizing recursively-enumerable languages>

## Other Models of Computation

- Pushdown Automata (Recognizes context-free languages)
<Image: A state diagram of a pushdown automata which looks very similar to a FSA but each transition has symbols denoting the top of the stack and what, if anything, to push to the stack>
- Turing Machine (Recognizes recursively-enumerable languages)
<Image: A state diagram of a turing machine which looks very similar to a FSA but each transition has symbols denoting the read-head symbols and what to output to the write tape>

## External Links & Notes

- web.stanford.edu/class/archive/cs/cs103/cs103.1142/button-fsm/
- raganwald.com/2018/02/23/forde.html
- "Introduction to the Theory of Computation“, Part 1, Chapter 1, Sipser.
- regexr.com
- docs.python.org/3/library/re.html
- www.regular-expressions.info/
- https://cstheory.stackexchange.com/a/14818
- inst.eecs.berkeley.edu//~cs150/fa05/CLD_Supplement/chapter11/chapter11.doc3.html
