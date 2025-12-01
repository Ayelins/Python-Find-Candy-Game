# Find the Candy

A simple memory game made with Python and Turtle graphics. You look at a grid of candies, memorize where they are, and then try to find all copies of a specific candy once the grid is covered.

---

## Step-by-Step Explanation of the Project

### 1. Setup and Images
- The game uses the `turtle` module to draw everything on the screen.
- Four candy images (`bluecandy.gif`, `greencandy.gif`, `purplecandy.gif`, `redcandy.gif`) are loaded.
- The screen is set to 800×800 with a white background.

### 2. Making the 4×4 Grid
- The function `make_grid()` calculates 16 positions so each candy has a spot on the grid.
- `candy_turtle()` creates 16 turtle objects that will hold the candy images.

### 3. Placing Random Candies
- `random_candylocation()` shuffles all candy images so the grid is different every round.
- `make_candy()` places each candy image onto the grid.

### 4. Covering the Candy
- After a short delay, `black_box()` puts black squares on top of all candies.
- This hides the candies so the player must remember where they were.

### 5. Choosing the Candy to Find
- The game randomly picks one candy (example: `bluecandy.gif`) as the **target candy**.
- `game_score()` displays:
  - Score
  - Current Level
  - Which candy you need to find

### 6. Clicking and Checking
- When the player clicks:
  - The game checks which square was clicked.
  - If the candy under the square matches the target candy:
    - The black square is removed
    - The game shows “Correct!”
  - If all copies of that candy are found:
    - Score increases
    - A new round starts
  - If the player clicks the wrong candy:
    - Score decreases (but never below 0)
    - A new shuffled round starts

### 7. Leveling Up
- Every 3 points, the level increases.
- A message “LEVEL UP!” appears for one second.

### 8. Start Screen
- Before the game begins, there is a welcome screen with:
  - A green Start button
  - A moving candy animation
  - A title message
- Clicking Start hides the intro screen and begins the game.

---
