# Jurassic Park Text Adventure Game

## Description

This Python script implements an interactive text-based adventure game set in Jurassic Park. Players navigate through various scenarios, making choices that affect the outcome of their adventure. The game features multiple paths, random events, and different endings based on player decisions.

## Features

- Multiple starting points and branching storylines
- Interactive decision-making throughout the game
- Random events to increase replayability
- Various endings based on player choices
- Incorporation of Jurassic Park themes and locations

## How to Play

1. Run the script in a Python environment.
2. Enter your name when prompted.
3. Choose your starting location from the available options.
4. Make decisions throughout the game by selecting numbered options.
5. Try to survive and escape the island!

## Game Structure

- The game is divided into several main functions:
  - `Welcome()`: Introduces the game and allows the player to choose their starting point.
  - `Scene1()`, `Scene2()`, `Scene3()`: Different storylines based on the player's choices.
  - `PanicMode()`: A reusable function to create tension in the story.
  - `DriveTo()`, `MeetUp()`, `JungleOasis()`: Additional scenario functions.

## Requirements

- Python 3.x

## Running the Game

To start the game, run the following command in your terminal:

```
python jurassic_park_adventure.py
```

## Notes

- The game uses random number generation to create variability in outcomes.
- Some paths may lead to survival, while others result in various game-over scenarios.
- The story incorporates elements from the Jurassic Park franchise, including dinosaurs and iconic locations.

## Author

Sayed Abdul Ahad Ibrahimi

## Acknowledgments

This game was created as an assignment to demonstrate the use of conditionals, boolean expressions, and functions in Python programming.
