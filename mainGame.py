import pygame
import sys
import random
from pygame.math import Vector2


# Class for snake(player)
class SNAKE:
    # Initialize snake's starting position
    # Draw snake
    # Move snake
    # Increment snake's length by 1
    # Play crunch sound
    # Reset snake
    
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        
        # Load snake graphics images
        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        
        # Load crunch sound
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
        
    # Draw snake on display_surface    
    def draw_snake(self):
        # Create a rectangle
        # Draw the snake on display_surface according to its direction(there are different images based on snake's path and direction)
        
        self.update_head_graphics()
        self.update_tail_graphics()
        
        # Via index there is better access to each block of the snake
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # If index == 0 --> we are looking at head --> draw head
            if index == 0:
                display_surface.blit(self.head, block_rect)
            # If index == last block --> we are looking at tail --> draw tail
            elif index == len(self.body) - 1:
                display_surface.blit(self.tail, block_rect)
            # Otherwise we are looking at body --> draw body
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                # If x coordinates equal on neighbour blocks --> snake goes vertically straight
                if previous_block.x == next_block.x:
                    display_surface.blit(self.body_vertical, block_rect)
                # If y coordinates equal on neighbouring blocks --> snake goes horizontally straight
                elif previous_block.y == next_block.y:
                    display_surface.blit(self.body_horizontal, block_rect)
                else:
                    # If previous_block is to the left of the block and next_block is on top of the block(or the same way in reverse) --> draw corner that goes from left to the top(tl = TopLeft)
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        display_surface.blit(self.body_tl, block_rect)
                    # If previous_block is on the bottom of the block and next_block is to the left of the block(or the same way in reverse) --> draw corner that goes from bottom to the left(bl = BottomLeft)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        display_surface.blit(self.body_bl, block_rect)
                    # If previous_block is on the top of the block and next_block is to the right of the block(or the same way in reverse) --> draw corner that goes from top to the right(tr = TopRight)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        display_surface.blit(self.body_tr, block_rect)
                    # If previous_block is on the bottom of the block and next_block is to the right of the block(or the same way in reverse) --> draw corner that goes from bottom to the right(br = BottomRight)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        display_surface.blit(self.body_br, block_rect)
         
    # Help function, which picks the right image of the snake's head, based on its direction        
    def update_head_graphics(self):
        # Subtracts the head block vector from the 1. block vector --> from this we get the relation
        # of the 1. block and head block(if it is to the left, then the result will be (-1, 0), etc.)
            
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down
            
    # Help function, which picks the right image of the snake's tail, based on its direction
    def update_tail_graphics(self):
        # Subtracts the last block vector from the block vector before --> from this we get the relation
        # of the last block and block before(if it is to the left, then the result will be (-1, 0), etc.)
        
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right  
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up  
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down      
    
    # Move the snake (if self.new_block is True, move the snake and also add new block to the snake)       
    def move_snake(self):
        # Logic behind moving the snake:
        # Copy whole body without last block of body and insert 
        # new block of body in the direction the snake is facing
            # If self.new_block is True --> Copy whole body and insert 
            # new block of body in the direction the snake is facing
        
        if self.new_block == False and self.direction.x  != 0 or self.direction.y != 0:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        elif self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
    
    # Increment the length of the snake by 1 block    
    def add_block(self):
        # Set self.new_block to True
        self.new_block = True
    
    # Function that plays crunch sound    
    def play_crunch_sound(self):
        self.crunch_sound.play()
    
    # Reset the snake    
    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


# Class for fruit(snake's objective)
class FRUIT:
    # Create position coordinates x and y
    # Draw the fruit on position x and y
    # Reposition the fruit
    
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    
    # Draw fruit on display_surface    
    def draw_fruit(self):
        # Create a rectangle
        # Draw the fruit on display_surface
        
        x_pos_fruit = int(self.pos.x * cell_size)
        y_pos_fruit = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(x_pos_fruit, y_pos_fruit, cell_size, cell_size)
        display_surface.blit(apple, fruit_rect)
    
    # Reposition the fruit    
    def randomize(self):
        # Create position coordinates x and y
        
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


# Class for entire game logic(move the snake, draw elements, check collisions, check fail, game over)
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.gameover = False
    
    # Utilize game logic(move the snake, check collision, check fail)
    def update(self):
        if self.gameover == False:
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()
    
    # Draw elements on display_surface
    def draw_elements(self):
        if self.gameover == False:
            self.draw_grass()
            self.snake.draw_snake()
            self.fruit.draw_fruit()
            self.draw_score()
        else:
            self.draw_game_over()
            self.draw_score()
        
    # Check if snake has eaten the fruit
    def check_collision(self):
        # If snake has eaten the fruit do:
            # Reposition the fruit
            # Increment the length of the snake by 1 block
            
        global score
        
        # If fruit position == snake position --> snake has eaten the fruit
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
            score += 1
        
        # If the fruit repoositioned itself under the snake's body --> reposition it again   
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    
    # Check if the game should be over
    def check_fail(self):
        # Check if snake hits the wall(goes outside of the screen)
        # Check if snake hits itself
        
        # If the snake's position is not within the grid area(between 0 and cell_number) --> game over
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
            
        # If the snake's head hits any of the snake blocks --> game over
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    # Game over function --> stop the game, reset the snake
    def game_over(self):
        # Reset the game
        self.snake.reset()
        self.gameover = True
        
    # Draw game over text    
    def draw_game_over(self):
        # Create game over text -> rectangle -> display it
        game_over_text = "Game over! Press any arrow to play again." 
        game_over_surface = game_font.render(game_over_text, True, (56, 74, 12))
        
        game_over_x = int(cell_size * cell_number / 2)
        game_over_y = int(cell_size * cell_number / 2)
        game_over_rect = game_over_surface.get_rect(center = (game_over_x, game_over_y))
        display_surface.blit(game_over_surface, game_over_rect)

    # Grass drawing function
    def draw_grass(self):
        # Draw rectangle, which is a little bit darker than background color to make a checkboard
        
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            # Coloring every even row and cell
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(display_surface, grass_color, grass_rect)
            # Coloring every odd row and cell
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(display_surface, grass_color, grass_rect)
    
    # Score drawing function
    def draw_score(self):
        # Create score
        global score
        score_text = str(score) #str(len(self.snake.body) - 3) # Subtracting 3 because we don't count the first three cells as score
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        
        # Create score rectangle, apple rectangle, border and draw it onto the display_surface
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left - 5, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left - 5, apple_rect.top - 5, apple_rect.width + score_rect.width + 20, apple_rect.height + 10)
        
        display_surface.blit(score_surface, score_rect)
        display_surface.blit(apple, apple_rect)
        pygame.draw.rect(display_surface, (56, 74, 12), bg_rect, 2)
       
         
# Pygame initialization
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512) # Set up mixer so it plays the crunch sound immediately


# Constants
    # Cell_size and cell_number are used to define size of each cell in a virtual grid
cell_size = 40
cell_number = 20
    # Frames per second
FPS = 60
    # Event SCREEN_UPDATE with a 150 millisecond timer to periodically update game logic at the same pace
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


# Set up the display surface
display_surface = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))


# Set up clock
clock = pygame.time.Clock()


# Set up game logic
main_game = MAIN()


# Load apple graphics image
apple = pygame.image.load('Graphics/apple.png').convert_alpha()


# Set up game font for text
game_font = pygame.font.Font('Font/SuperEnjoy.ttf', 25)


# Game loop
running = True
main_game.gameover = False
score = 0
while running:
    
    # Process input (events)
    for event in pygame.event.get():
        
        # If the event is QUIT --> quit Pygame, exit the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # If the event is SCREEN_UPDATE --> utilize game logic(move the snake, check collision, etc)
        if event.type == SCREEN_UPDATE:
            main_game.update()
            
        # If the event is KEYDOWN --> player pressed a key
        if event.type == pygame.KEYDOWN:
            
            # If player presses UP arrow --> change the direction of the snake UP
            if event.key == pygame.K_UP:
                # If the game was over --> reset the score with the start of the new game
                if main_game.gameover == True:
                    score = 0
                main_game.gameover = False
                # If statement that prevents the snake from going reverse instantly killing itself
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            
            # If player presses DOWN arrow --> change the direction of the snake DOWN
            if event.key == pygame.K_DOWN:
                # If the game was over --> reset the score with the start of the new game
                if main_game.gameover == True:
                    score = 0
                main_game.gameover = False
                # If statement that prevents the snake from going reverse instantly killing itself
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            
            # If player presses RIGHT arrow --> change the direction of the snake RIGHT
            if event.key == pygame.K_RIGHT:
                # If the game was over --> reset the score with the start of the new game
                if main_game.gameover == True:
                    score = 0
                main_game.gameover = False
                # If statement that prevents the snake from going reverse instantly killing itself
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            
            # If player presses LEFT arrow --> change the direction of the snake LEFT
            if event.key == pygame.K_LEFT:
                # If the game was over --> reset the score with the start of the new game
                if main_game.gameover == True:
                    score = 0
                main_game.gameover = False
                # If statement that prevents the snake from going reverse instantly killing itself
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
                
    
    # Color the background
    display_surface.fill((175, 215, 70))
    
    
    # Draw elements on display_surface
    main_game.draw_elements()
    
    
    # Update the display surface
    pygame.display.update()
    
    
    # Set the FPS of the game
    clock.tick(FPS)