import pygame
import random
import time


# Initialize Pygame
pygame.init()


# Screen dimensions
width = 800
height = 800
screen = pygame.display.set_mode((width, height))


# Background color
background_color = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)


snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]


snake_speed = 20
direction = 'RIGHT' # setting the default direction at the start to be 'right'
fps = pygame.time.Clock()


fruit_position = [random.randrange(1, ((width-10)/10))*10,
                  random.randrange(1, ((height-10)/10))*10]
fruit_spawned = False


# end game when snake hits wall
def die():
    my_font = pygame.font.SysFont("saucecodepronerdfont", 50)


    game_over_surface = my_font.render("GAME OVER", True, red)
   
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.center = [(width/2), (height/2)]

    screen.blit(game_over_surface, game_over_rect)

    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    quit()


# display the score
def scoring(value, color, font, size):
    # create a font object
    score_font = pygame.font.SysFont("comicsans", 10)


    # create a text surface
    score_surface = score_font.render("Score: " + str())

# function to check which key is pressed, and returning the direction based on that
def get_direction(pressedKey, direction):

    if pressedKey[pygame.K_RIGHT] or pressedKey[pygame.K_d]:
        direction = 'RIGHT'
    elif pressedKey[pygame.K_LEFT] or pressedKey[pygame.K_a]:
        direction = 'LEFT'
    elif pressedKey[pygame.K_UP] or pressedKey[pygame.K_w]:
        direction = 'UP'
    elif pressedKey[pygame.K_DOWN] or pressedKey[pygame.K_s]:
        direction = 'DOWN'
    return direction

# function to move the snake based on the direction
def move_snake(direction):
    if direction == 'RIGHT':
        snake_position[0] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    else:
        pass # if no key is pressed, do nothing

def check_game_over(snake_position):
     #conditions to end game
    if snake_position[0] < -10 or snake_position[0] > width:
        die()
    if snake_position[1] < -10 or snake_position[1] > height:
        die()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            die()
    
direction = 'RIGHT' # setting default direction to move right
# main game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
        

    # getting the key pressed by the user 
    pressedKey = pygame.key.get_pressed()

    # getting the direction based on the key pressed by user
    direction = get_direction(pressedKey, direction)

    # moving the snake based on the direction that we got from the user's pressed key
    move_snake(direction)

    # checking if game is over
    check_game_over(snake_position)
   
    if not fruit_spawned:
        pygame.draw.rect(screen, red, pygame.Rect(fruit_position[0], fruit_position[1], 40, 40))


    # fruit being eaten
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        print("Fruit Eaten")
        # updating fruit position
        fruit_position = [random.randrange(1, ((width-10)/10))*10,
                  random.randrange(1, ((height-10)/10))*10]
       
    #fruit_spawned = False

    snake_body.insert(0, list(snake_position))
    snake_body.pop()

    pygame.display.flip()

    fps.tick(snake_speed)


pygame.quit()


