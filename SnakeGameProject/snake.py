from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.x_axis = 0
        self.y_axis = 0
        self.snake_bodies = []
        self.create_snake()
        self.head = self.snake_bodies[0]

    def create_snake(self):
        """Creates the snake."""
        for snake_index in STARTING_POSITIONS:
            self.add_to_snake_body(snake_index)

    def add_to_snake_body(self, snake_index):
        snake_body = Turtle(shape="square")
        snake_body.color("white", "blue")
        snake_body.penup()
        snake_body.goto(snake_index)
        self.snake_bodies.append(snake_body)
        #self.x_axis -= 20

    def extend(self):
        """Add a new segment to the snake body."""
        self.add_to_snake_body(self.snake_bodies[-1].position())

    def reset_snake(self):
        """Reset the snake."""
        for body in self.snake_bodies:
            body.goto(1000, 1000)
        self.snake_bodies.clear()
        self.create_snake()
        self.head = self.snake_bodies[0]

    def move(self):
        """Moves the snake."""
        for body_index in range(len(self.snake_bodies) - 1, 0,
                                -1):  # start = len(snake_bodies), stop = 0, step = -1
            new_x_axis = self.snake_bodies[body_index - 1].xcor()
            new_y_axis = self.snake_bodies[body_index - 1].ycor()
            self.snake_bodies[body_index].goto(new_x_axis, new_y_axis)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        """Moves the snake up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        """Moves the snake down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        """Moves the snake to the left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        """Moves the snake to the right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
