# Optional Exercise 5

Assmue that we are playing the game *rock, paper and scissors*. 
Please check (this)[https://en.wikipedia.org/wiki/Rock_paper_scissors] if you are not familiar with this game.

Please write a program for this. 

- initlization: multiple players are created and added to a game
- at the beginning of a game, each player makes a choce;
- then we check who wins the game;
	- if there is only one winner, the game ends;
	- if there is no winner, the game move to the next round;
	- if there are multiple winners, the game move to the next round with only these winners;
- in the next round, the players make a new choice again.
- ...
- until the final winner is found.


Note: There are many ways to implement this. If you want to check if your implementation is correct or not, please send your code to yqtian@ust.hk.


In this program, you are expected to define the following classes.
(1) Player, (2) Choice and (3) game.


Class Player should have at least the following attributes:
- name: name of the player;
- choice: current choice of the player; default is None;
- status: status of this player in one game; can be either win, lose, or tie

Class Player should have at least the following methods: 
- __init__: constructor, which creates and initilizes all variables;
- make_a_choice: it will randomly create one object choice
- print_choice: it will print the current choice


Class Choice should have at least the following attributes:
- name: can be paper, rock, or scissors

Class Choice should have at least the following methods: 
- __init__: constructor, which creates and initilizes all variables;
- compare(other): this function will compare it self with the *other* choice, and return win/lose/even 

Class Game should have at least the following attributes:
- num_player: the number of players; at least two, can be muliple;
- players: the list of players
- winner: the palyer who wins the game; default is None.

Class Game should have at least the following methods: 
- __init__: constructor, which creates a game and a list of players;
- start: it will ask each player to make a choice; then it calls function who_is_winner to determine who is the winner of this round;
if this round is a tie (multiple winners), it will ask the winners of this round to do one more round, until only one winner is left;
if there is no winner in one round, it will ask the players of this round to do one more round, until only one winner is left;
This function will print the intermediate results as detailed as possible.
- who_is_winner_in_this_round: It will check the choice of all players and call the choice.compare to determine who is the winner of one round.
The winner of one round can be 0 (no winner), 1 (one winner), or multiple (tie, means multiple winners in this game).



An example of the detailed intermediate resutls:
Game Starts with 3 players.
Player 1 chose rock
Player 2 chose rock
Player 3 chose scissors
This round: 
Player 1 and Player 2 are tie, Player 3 is excluded for the next round. 
Game continues with 2 players.
Player 1 chose rock
Player 2 chose paper
This round: 
Player 1 is the final winners. 

An second example of the detailed intermediate resutls:
Game Starts with 3 players.
Player 1 chose rock
Player 2 chose paper
Player 3 chose scissors
This round: No winner in this round
Game continues with 3 players.
Player 1 chose rock
Player 2 chose scissors
Player 3 chose scissors
This round: Player 1 is the final winners. 
