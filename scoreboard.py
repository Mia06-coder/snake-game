from turtle import Turtle 

# Constants for alignment and font style 
ALIGNMENT = "center" 
FONT = ('Courier', 10, 'bold') 

class Scoreboard(Turtle): 
    def __init__(self): 
        """  
        Initializes the scoreboard, sets initial score,  
        and places the scoreboard on the screen. 
        """ 
        super().__init__() 
        self.score = 0 
        self.color("black") 
        self.penup() 
        self.goto(0,230) # Scoreboard position 
        self.update_score() # Display the initial score 
        self.hideturtle() 

    def update_score(self): 
        """  
        Updates the displayed score on the screen. 
        """ 
        self.clear() # Clear previous score to prevent overlap 
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT) # Write the current score 

    def increase_score(self): 
        """  
        Increases the score by one and updates the  
        displayed score. 
        """ 
        self.score += 1 # Increment the score 
        self.update_score() # Refresh the score display