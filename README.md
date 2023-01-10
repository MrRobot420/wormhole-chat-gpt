# Wormhole

A simple game written using the Pygame library.

## How to play

The objective of the game is to control the player (a circle) and consume as many enemies (also circles) as possible. The player starts off small and grows larger with each enemy it consumes. The player wins if it grows to a certain size (half the size of the window).

The player is controlled using the W,A,S,D keys to move up, down, left, and right.

The game also keeps track of the player's score, which increases by 100 points for each enemy consumed.

---

## Code structure

The game code is structured into three main classes: Game, Player, and Enemy.

The Game class is responsible for initializing and running the game. It creates and manages the player and enemy objects, and handles the game loop and events.
The Player class is responsible for representing and updating the player object in the game.
The Enemy class is responsible for representing and updating the enemy objects in the game.

---

## How to run

This game is written in Python, and requires the Pygame library to be installed. To run the game, make sure Pygame is installed, and then run the following command in the terminal from the root of the project:

```bash
python main.py
```

---

# Future Work

-   Add more levels and increasing difficulty.
-   Add sound effects.
-   Add more power-ups.
-   Add different type of enemies.
-   Add support for multiple players.
