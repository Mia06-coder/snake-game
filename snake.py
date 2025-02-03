from turtle import Turtle 

# Constants for snake behaviour and movement 
STRETCH_SIZE = 0.5 
DEFAULT_SIZE = 20 
STARTING_POSITIONS = [
    (0,0), 
    (-DEFAULT_SIZE*STRETCH_SIZE,0),
    (-2*DEFAULT_SIZE*STRETCH_SIZE,0),
    (-3*DEFAULT_SIZE*STRETCH_SIZE,0)
] # Initial positions of the snake segments 

class Snake:
    def __init__(self): 
         """ 
         Initializes the snake by creating the initial  
         segments and assigning the head. 
         """ 
         self.snake_body = [] # List to hold the snake segments 
         self.create_snake() # Create the initial snake 
         self.head = self.snake_body[0] # The head of the snake is the first segment 

    def create_snake(self):
         """ 
         Creates the initial snake segments at predefined 
         positions from the `STARTING_POSITIONS` constant. 
         """
         for position in STARTING_POSITIONS:
             self.add_segment(position) # Add each segment at the starting positions 

    def add_segment(self, position):
        """
        Adds a new segment to the snake at the specified position. 
        """ 
        segment = Turtle("square")
        segment.color("green")
        segment.penup() 
        segment.shapesize(stretch_len=STRETCH_SIZE, stretch_wid=STRETCH_SIZE)
        segment.goto(position) 
        self.snake_body.append(segment) 