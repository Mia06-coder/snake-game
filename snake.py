from turtle import Turtle 

# Constants for snake behaviour and movement 
STRETCH_SIZE = 0.5 
DEFAULT_SIZE = 20 
BODY_SIZE = MOVE_DIST = DEFAULT_SIZE*STRETCH_SIZE 
STARTING_POSITIONS = [
    (0,0), 
    (-BODY_SIZE,0),
    (-2*BODY_SIZE,0),
    (-3*BODY_SIZE,0)
] # Initial positions of the snake segments 

UP = 90 # Heading angle for upward movement 
DOWN = 270 # Heading angle for downward movement 
LEFT = 180 # Heading angle for leftward movement 
RIGHT = 0 # Heading angle for rightward movement 

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
        segment = Turtle("circle")
        segment.color("green")
        segment.penup() 
        segment.shapesize(stretch_len=STRETCH_SIZE, stretch_wid=STRETCH_SIZE)
        segment.goto(position) 
        self.snake_body.append(segment) 

    def extend_snake(self): 
        """ 
        Adds a new segment to the snake at the position  
        of the last segment. 
        """ 
        self.add_segment(self.snake_body[-1].position()) 

    def move(self): 
        """ 
        Moves the snake forward by updating the position of 
        each segment, starting from the tail. 
        """ 
        # Shift all segments except the head to the position of the segment in front of them
        for seg_num in range(len(self.snake_body) - 1, 0, -1): 
            new_x = self.snake_body[seg_num - 1].xcor() 
            new_y = self.snake_body[seg_num - 1].ycor() 
            self.snake_body[seg_num].goto(new_x, new_y) 

        # Move the head forward by MOVE_DIST 
        self.head.forward(MOVE_DIST)

    def up(self): 
        """
        Change the direction of the snake to up if it's  
        not currently heading down. 
        """ 
        if self.head.heading()!= DOWN: 
            self.head.setheading(UP) 


    def down(self): 
        """ 
        Change the direction of the snake to down if it's  
        not currently heading up. 
        """ 
        if self.head.heading()!= UP: 
            self.head.setheading(DOWN) 

    def left(self):  
        """ 
        Change the direction of the snake to left if it's  
        not currently heading right. 
        """ 
        if self.head.heading()!= RIGHT: 
            self.head.setheading(LEFT) 

    def right(self): 
        """ 
        Change the direction of the snake to right if  
        it's not currently heading left. 
        """ 
        if self.head.heading()!= LEFT: 
            self.head.setheading(RIGHT) 
            