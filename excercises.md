# Excercises

1. Write a formal description (using the $(\Sigma, Q, q_0, \delta, F)$ formulation) of the finite automaton that recognizes binary strings that represent even numbers
2. Can you design a finite automaton that checks if a binary string has an even number of ones and an even number of zeros?
3. Can you design a finite automaton that checks if a binary string has an equal number of ones and zeros *such that no '0' follows any '1' character*? That is, strings of the form '01', '0011', '000111', but not '0101', '001', '0110', etc.
4. What is the language recognized by this machine? <Image: A non-deterministic state machine with two states labelled '1' and '2'. '1' is the starting state. The alphabet is $\{a,b\}$. '1' transitions to 2 on input 'b' and to itself on input 'a'. '2' transitions to 1 on input 'a' and to itself on input 'b'>
5. Give examples of two strings that are accepted by and two strings that are not accepted by the following regular expressions
	1. $(aaa)\ast$
	2. $(\varepsilon \cup a)b$
6. Write the regular expression that recognizes each of the following regular languages. For each regular expression, implement it using Python's RegEx syntax. Try to find the minimal DFA that recognizes each language. Note: $a^n$ denotes the string $a$ concatenated with itself $n$ times. So $a^5$ denotes $aaaaa$

	1. $\{waz^nup : z \in [0,4]\}$
	2. $\{a^nb^m : n \in [2,4], m \in [0,6]\}$
7. In certain programming languages, comments appear between delimiters such as '/#' and '#/'. Let $C$ be the language of all valid delimited comment strings. A member of $C$ must begin with '/#' and end with '#/' but have not intervening '#/'. For simplicity, we'll say that the comments themselves are written with only the symbols $a$ and $b$. Hence the alphabet of $C$ is $\Sigma = \{a,b,/,\#\}$
	1. Give a DFA that recognizes C
	2. Give a regular expression that generates $C$ 
8. Show that, if $M$ is a finite automata that recognizes language $B$, swapping the accept and non-accept states in $M$ yields a new automata that recognizes the complement of $B$. Conclude that the class of regular languages in closed under complement.
9. Write functions/Using Python's `re` module, write a program to check if an input string is a valid phone number. A valid phone has a two- or three-digit country code (which may or may not be surrounded by parentheses), followed by a six-digit number. The country code and the number are separated by a hyphen. So (91)-551232 and 881-456987 are both valid phone numbers. 
