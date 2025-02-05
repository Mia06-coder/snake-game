from turtle import Screen 
from snake import Snake 
from food import Food
from scoreboard import Scoreboard
import time 

SCREEN_SIZE = 500 # Screen size constant 
STRETCH_SIZE = 0.5 
MOVE_DELAY = 0.3

def main():
    # Screen setup 
    screen = Screen() 
    screen.setup(width=SCREEN_SIZE,height=SCREEN_SIZE) 
    screen.bgcolor("white") # Screen background color 
    screen.title("SNAKE🐍") # Window Title 

    # Prevent window resizing
    try:
        screen.cv._rootwindow.resizable(False, False)
    except AttributeError:
        pass  # If it doesn't work, just ignore it (Turtle behavior varies)

    screen.tracer(0) # Turn off the screen updates for performance reasons 

    # Create instances of game entities 
    snake = Snake() 
    food = Food()
    scoreboard = Scoreboard()

    # Control keys for snake's movement 
    screen.listen() 
    screen.onkey(snake.up,"Up") # Move the snake up 
    screen.onkey(snake.down,"Down") # Move the snake down 
    screen.onkey(snake.left, "Left") # Move the snake left 
    screen.onkey(snake.right,"Right") # Move the snake right 

    # Main game loop 
    game_on = True 
    while game_on:
        screen.update() # Refresh the screen to show current state 
        time.sleep(MOVE_DELAY) # Control the speed of the game 
        snake.move() # Move the snake forward 

        # Check for collision with food 
        if snake.head.distance(food) < 8: 
            food.display_food() # Display food on new location
            snake.extend_snake()
            scoreboard.increase_score() # Update the score

    # Exit the game on click 
    screen.exitonclick()

if __name__ == "__main__":
    main()