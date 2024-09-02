# Boggle Game

## Overview

This is a Boggle game implemented in Python using Tkinter for the GUI. The game allows users to find valid words on a randomized 4x4 board of letters, following the traditional Boggle rules.

## Features

- **Randomized Board**: The board is randomly generated each time a new game starts.
- **Word Validation**: The game checks if the words formed by the player are valid according to a dictionary.
- **Score Calculation**: Scores are calculated based on the length of the words submitted, with longer words earning more points.
- **GUI**: The game features a user-friendly GUI with different screens for home, main game, and end screen.
- **Timer**: A countdown timer is implemented to limit the duration of the game.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python)
- A valid dictionary file (`boggle_dict.txt`) containing valid words.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/boggle-game.git
    cd boggle-game
    ```

2. Ensure you have Python installed on your system.

3. Run the game using the following command:
    ```bash
    python boggle.py
    ```

## How to Play

1. **Start the Game**: Run `boggle.py` to start the game. You'll be greeted with the home screen.
2. **Play the Game**: 
   - Click the "Start Game" button to begin.
   - A 4x4 board of letters will be displayed.
   - Form words by clicking on adjacent letters. Letters must be adjacent horizontally, vertically, or diagonally.
   - Click "Submit Word" to submit your word. Valid words will be added to your score.
3. **End Game**: The game ends either when the timer runs out or if you choose to end the game manually.

## File Descriptions

- **board.py**: Handles the logic of the board, including checking word paths and updating the GUI with chosen letters.
- **boggle.py**: Manages the overall game flow, including loading different screens.
- **boggle_board_randomizer.py**: Contains the logic for randomizing the Boggle board.
- **end_screen.py**: Implements the end screen of the game, including buttons and labels for game summary.
- **home_screen.py**: Implements the home screen of the game, where players can start a new game.
- **main_screen.py**: Implements the main game screen, including the board, score display, and word submission.
- **boggle_dict.txt**: The dictionary file containing valid words for the game.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the creators of Tkinter for providing a simple and effective GUI toolkit for Python.
- The inspiration for this game comes from the classic Boggle game by Parker Brothers.

