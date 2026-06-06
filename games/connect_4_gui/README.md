# Connect 4 GUI Game

## Overview
This is a playable Connect4 game with a visual interface built using Pygame.

## Features
- ✅ 7x6 game board
- ✅ Two-player gameplay (alternating turns)
- ✅ Visual representation with red and blue discs
- ✅ Click-to-play interface
- ✅ Win detection (horizontal, vertical, diagonal)
- ✅ Game-over detection

## Requirements
- Python 3.7+
- pygame 2.0+

### Installation
```bash
pip install pygame
```

## How to Play
1. Run the game:
   ```bash
   python connect_4_game.py
   ```

2. **Controls:**
   - Click any column (0-6) to drop your disc
   - Red circles = Player 1
   - Blue circles = Player 2
   - Close the window to exit

3. **Win Condition:**
   - First player to get 4 discs in a row (horizontal, vertical, or diagonal) wins
   - The game prevents further moves after a win

## Game Logic
The game uses the `Connect4` class from `array/Connect_4.py` which handles:
- Board state management (6 rows × 7 columns)
- Turn management (alternates between Player 1 and Player 2)
- Win detection (checks all 4 directions)
- Column full detection

## Complexity Analysis
- **Time Complexity:** O(1) per move (board checking is constant for 4-in-a-row)
- **Space Complexity:** O(42) = O(1) (6×7 board)

## Files
- `connect_4_game.py` - Main game file with Pygame implementation
- `__init__.py` - Package initialization

## Future Enhancements
- [ ] AI opponent (minimax algorithm)
- [ ] Score tracking
- [ ] Difficulty levels
- [ ] Game replay/undo functionality
- [ ] Sound effects and animations
