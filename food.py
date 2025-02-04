from turtle import Turtle 
from random import randint 

STRETCH_SIZE = 0.5 
MOVE_DIST = 10

class Food(Turtle): 
    def __init__(self): 
        """ 
        Initializes the food object with its properties. 
        """ 
        super().__init__() 
        self.shape("circle") 
        self.penup() 
        self.shapesize(stretch_len=STRETCH_SIZE,stretch_wid=STRETCH_SIZE) 
        self.color("red") 
        self.speed("fastest") 
        self.display_food()  

    def display_food(self):
        """ 
        Displays the food at a new random location on  
        the screen. 
        """ 
        # Ensure food spawns on a grid-aligned position to match the snake movement
        rand_xcor = randint(-230//MOVE_DIST,230//MOVE_DIST)*MOVE_DIST # Generate random x coordinate within the game area 
        rand_ycor = randint(-230//MOVE_DIST,230//MOVE_DIST)*MOVE_DIST # Generate random y coordinate within the game area 
        self.goto(rand_xcor,rand_ycor) # Move the food to the random location 

 