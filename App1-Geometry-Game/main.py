from random import randint
from turtle import *
import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else: return False


class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


class Rectangle:

    """
    Point1: Lower Left Point
    Point2: Upper Right Point
    """
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return ((self.point2.x - self.point1.x) * (self.point2.y - self.point1.y))


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        x_dist = self.point2.x - self.point1.x
        y_dist = self.point2.y - self.point1.y
        canvas.forward(x_dist)
        canvas.left(90)
        canvas.forward(y_dist)
        canvas.left(90)
        canvas.forward(x_dist)
        canvas.left(90)
        canvas.forward(y_dist)





rectangle = GuiRectangle(Point(randint(0, 9)*10, randint(0, 9)*10), Point(randint(10, 19)*10, randint(10, 19)*10))

print(
    "Rectangle Coordinates: ",
    rectangle.point1.x, ",",
    rectangle.point1.y, "and",
    rectangle.point2.x, ",",
    rectangle.point2.y
)

user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))

user_area = float(input("Guess rectangle area: "))

print("Point inside the rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)


# set screen
width = 400
height = 400
screen = Screen()
screen.setup(width, height)

# Canvas to draw rectangle on
canvas = turtle.Turtle()


rectangle.draw(canvas=canvas)
user_point.draw(canvas=canvas)

turtle.done()