# Minesweeper Game

## Overview
This is a **Minesweeper** game implemented in Python as a project for my **Programming Fundamentals (PF)** course. The game follows the classic Minesweeper mechanics, where players uncover tiles to avoid hidden mines while using numerical hints to navigate safely.

## Features
- Classic Minesweeper gameplay
- Randomly generated minefield
- Number hints indicating adjacent mines
- User-friendly Command Line Interface (CLI)
- Customizable grid size and difficulty levels
- Win/Loss detection

## Technologies Used
- **Python**: Core programming language
- **Random module**: For mine placement
- **OS module** (if needed for CLI enhancements)

## Installation & Running the Game
### Prerequisites
- Install **Python 3.x**

### Steps to Run
1. Clone or download the repository:
   ```sh
   git clone https://github.com/your-username/minesweeper.git
   cd minesweeper
   ```
2. Run the game:
   ```sh
   python minesweeper.py
   ```

## How the Game Works
### Board Generation
- The board is created based on user-specified dimensions and mine count.
- Mines are placed randomly on the board while ensuring no duplicates.
- The board contains:
  - `0`: Hidden blank cells
  - `-1`: Hidden mine cells
  - Revealed cells show adjacent mine counts.

### Gameplay Mechanics
- The player selects a tile by entering its row and column.
- If the tile contains a **mine**, the game ends with a loss.
- If the tile is blank, the game recursively reveals surrounding safe tiles.
- The player wins when all non-mine tiles are revealed.

### Win/Loss Detection
- The game continuously checks if all safe tiles have been revealed.
- If so, the player is congratulated for winning.
- If a mine is uncovered, the game reveals all tiles and displays "Game Over".

## How to Play
- Start the game and enter the board dimensions and number of mines.
- Select a tile by entering its row and column.
- Avoid mines and use number hints to uncover safe tiles.
- Win by revealing all safe tiles.

## Screenshots
(Add screenshots of the game here if available)

## Future Improvements
- Add timer and score tracking
- Implement difficulty levels
- Improve CLI interactions

## Credits
Developed by **Aakash Ali** as a Programming Fundamentals project.

## License
This project is open-source and available under the MIT License.

