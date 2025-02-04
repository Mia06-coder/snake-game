from turtle import Screen 
from snake import Snake 
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

    # Main game loop 
    game_on = True 
    while game_on:
        screen.update() # Refresh the screen to show current state 
        time.sleep(MOVE_DELAY) # Control the speed of the game 
        snake.move() # Move the snake forward 

    # Exit the game on click 
    screen.exitonclick()

if __name__ == "__main__":
    main()