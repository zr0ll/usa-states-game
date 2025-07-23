from turtle import Turtle
class State(Turtle):
    def __init__(self, x , y,name):
        super().__init__()
        self.state = name
        self.penup()
        self.hideturtle()
        self.setposition(x,y)
        self.setheading(270)
    def show_state(self):

        self.write(f"{self.state}", align='center', font=('Arial', 8, 'bold'))


