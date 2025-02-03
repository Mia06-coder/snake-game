from turtle import Screen 

SCREEN_SIZE = 500 # Screen size constant 

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

    # Exit the game on click 
    screen.exitonclick()

if __name__ == "__main__":
    main()