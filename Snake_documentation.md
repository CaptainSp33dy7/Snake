# Snake Python Game Documentation

## Overview

This documentation provides detailed descriptions of the classes and functions. Each section focuses on a specific class, describing its purpose and functionality.

## Classes

### 1. class SNAKE
#### Purpose

The `SNAKE` class represents a snake object in a game. The snake has a body composed of interconnected blocks, and it can move in different directions, grow in length, and interact with the game environment.

#### Attributes:

##### `body`
- Type: List of Vector2
- Description: Represents the snake's body, where each element is a Vector2 object representing the position of a block in the game grid.

##### `direction`
- Type: Vector2
- Description: Represents the current direction in which the snake is moving.

##### `new_block`
- Type: Boolean
- Description: Indicates whether the snake needs to grow by adding a new block.

##### `Head and Tail Graphics:`
- Type: Pygame image objects
- Description: Images representing the snake's head and tail in different orientations.

##### `Body Graphics:`
- Type: Pygame image objects
- Description: Images representing different configurations of the snake's body based on its path and direction.

##### `crunch_sound`
- Type: Pygame sound object
- Description: Sound played when the snake consumes food.

#### Methods:

##### `__init__(self)`
- Description: Initializes the snake with a default body, direction, and graphics.

##### `draw_snake(self)`
- Description: Draws the snake on the game display surface using different images for the head, tail, and body.

##### `update_head_graphics(self)`
- Description: Updates the snake's head image based on its current direction.

##### `update_tail_graphics(self)`
- Description: Updates the snake's tail image based on its last movement.

##### `move_snake(self)`
- Description: Moves the snake in its current direction, and if a new block is flagged, it also adds a new block to the snake.

##### `add_block(self)`
- Description: Flags the need to add a new block to the snake, typically called when the snake consumes food.

##### `play_crunch_sound(self)`
- Description: Plays the crunch sound when the snake consumes food.

##### `reset(self)`
- Description: Resets the snake to its initial state with a default body and direction.


### 2. class FRUIT
#### Purpose

The `FRUIT` class represents the fruit object in the game, which serves as the snake's objective. The fruit appears at a random position on the game grid, and the snake should aim to consume it.

#### Attributes:

##### `x`
- Type: Integer
- Description: The x-coordinate of the fruit's position on the game grid.

##### `y`
- Type: Integer
- Description: The y-coordinate of the fruit's position on the game grid.

##### `pos`
- Type: Vector2
- Description: A Vector2 object representing the position of the fruit on the game grid.

#### Methods:

##### `__init__(self)`
- Description: Initializes the fruit object with random x and y coordinates within the game grid.

##### `draw_fruit(self)`
- Description: Draws the fruit on the game display surface at its current position.

##### `randomize(self)`
- Description: Repositions the fruit to a new random position on the game grid.


### 3. class MAIN
#### Purpose

The `MAIN` class encompasses the entire game logic, managing the snake, fruit, and various game elements. It controls the game loop, checks for collisions, updates the display, and handles game over scenarios.

#### Attributes:

##### `snake`
- Type: SNAKE object
- Description: Represents the snake in the game.

##### `fruit`
- Type: FRUIT object
- Description: Represents the fruit (snake's objective) in the game.

##### `gameover`
- Type: Boolean
- Description: Indicates whether the game is over.

#### Methods:

##### `__init__(self)`
- Description: Initializes the game with instances of the snake, fruit, and sets the initial game over state to False.

##### `update(self)`
- Description: Utilizes game logic, including moving the snake, checking for collisions, and checking for game failure.

##### `draw_elements(self)`
- Description: Draws game elements on the display surface, including the grass background, snake, fruit, and score.

##### `check_collision(self)`
- Description: Checks if the snake has eaten the fruit and updates the game state accordingly.

##### `check_fail(self)`
- Description: Checks for game failure conditions, such as hitting the wall or colliding with the snake's own body.

##### `game_over(self)`
- Description: Handles the game over scenario by resetting the snake and updating the game over state.

##### `draw_game_over(self)`
- Description: Draws the game over text on the display surface.

##### `draw_grass(self)`
- Description: Draws a checkered grass background on the display surface.

##### `draw_score(self)`
- Description: Draws the current score on the display surface.


### 4. outside of classes
#### Purpose

The main objectives of the code include initializing the game, handling user input, updating game logic, and displaying game elements.

#### Variables

##### Pygame Initialization and Constants:

- `pygame.init()`: Initializes the Pygame library.
- `pygame.mixer.pre_init(44100, -16, 2, 512)`: Sets up the mixer for immediate crunch sound playback.

##### Game Configuration:

- `cell_size`: Defines the size of each cell in the virtual grid.
- `cell_number`: Specifies the number of cells in the grid.
- `FPS`: Represents frames per second for the game loop.
- `SCREEN_UPDATE`: Pygame USEREVENT for periodic game logic updates(150ms).
- `display_surface`: Pygame display surface with dimensions based on cell size and number.
- `clock`: Pygame clock for controlling the frame rate.
- `main_game`: Instance of the `MAIN` class managing game logic.
- `apple`: Pygame image representing the apple graphic.
- `game_font`: Pygame font for displaying text.
- `running`: Flag for controlling the game loop.
- `score`: Tracks the player's score.

##### User Input Processing:

- `event`: Pygame event variable processing user inputs.
- `pygame.KEYDOWN`: Pygame event type for a key press.
- Arrow key constants (`pygame.K_UP`, `pygame.K_DOWN`, `pygame.K_RIGHT`, `pygame.K_LEFT`): Represent arrow key presses.

#### Game Loop Explained

The game loop is the core structure of the code, responsible for continually updating, rendering, and processing user input to create a dynamic gaming experience. The key components of the game loop include:

- **Event Processing:** The loop processes various events, including quitting the game (`pygame.QUIT`), updating the screen (`SCREEN_UPDATE`), and handling key presses (`pygame.KEYDOWN`).
  
- **User Input Handling:** Detects arrow key presses to change the snake's direction. Checks for game over scenarios, resets the score on a new game, and prevents the snake from moving in the opposite direction, causing immediate failure.

- **Background Coloring:** Fills the display surface with a background color.

- **Drawing Elements:** Calls the `draw_elements` method of the `MAIN` class to draw the grass background, snake, fruit, and score on the display surface.

- **Display Update:** Updates the display surface to reflect the changes made during the frame.

- **Frame Rate Control:** Sets the frame rate using the `clock.tick(FPS)` function to control the speed of the game.