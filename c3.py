from turtle import *
import turtle
speed(0)

def up(): # 向上
    setheading(90) # 海龟面向屏幕上方
    fd(10) # 向上前进50像素

def down1(): # 向下
    setheading(-90) # 海龟面向屏幕下方
    fd(10) # 向下前进50像素

def left1(): # 向左
    setheading(180) # 向左
    fd(10) # 向左前进50像素
def h():
    home()
def right1(): # 向右
    setheading(360) # 向右
    fd(10) # 向右前进50像素
def q():
    up()
    home()
    clear()
    down()
def c():
    circle(10)
def r():
    color('red')
def b():
    color('black')
def o():
    color('orange')
def v():
    turtle.up()
def m():
    turtle.down()