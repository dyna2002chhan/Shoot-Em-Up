#IMPORT -----------------------------------------------------------------------------

from tkinter import *
import tkinter as tk
import random

#VARIABLES---------------------------------------------------------------------------

w = 1200
h = 700
x= w//2
y = h//2
x=1200
y2 = 300
y1 = 500
#CONSTANT----------------------------------------------------------------------------


root= tk.Tk()
root.title("cute")
root.geometry("1300x800")
canvas=tk.Canvas(root)
score =0
lives = 3

#GRAPHIC------------------------------------------------------------------------------

bg = tk.PhotoImage(file="spacebac.png")
background = canvas.create_image(650,400,image=bg)
root.title("SPACE INVADER")

# Amount of killed enemies
scoreLabel=Label(root, text="Kills :" + str(score), bg="white", fg="black", font= 50)
scoreLabel.place(x=1220,y=20)



# Amount of player's lives.
livesLabel= Label(root, text="Lives :" + str(lives), bg="white", fg="black", font= 50)
livesLabel.place(x=20,y=20) 
# Create bullet
bullets = tk.PhotoImage(file="missile.png")


plane= tk.PhotoImage(file="spaceship.png")
airplane_fly = canvas.create_image(100,y+40,image=plane) 


# enemy
planes= tk.PhotoImage(file="1enemy.png")
my_circle= canvas.create_image(1100,y-200,image=planes) 

plans= tk.PhotoImage(file="2enemy.png")
my_circles= canvas.create_image(1100,y,image=plans) 

# FUNCTIONS-------------------------------------------------------------------------

def missile():

    global leftBullet, rightBullet, middleBullet
    canvas.move(leftBullet,30,0)
    canvas.move(rightBullet, 35, 0)
    canvas.move(middleBullet,40, 0)
    myY = canvas.coords(leftBullet)[1]
    Shooting = myY <= 0
    
    if not Shooting:
        canvas.after(60, lambda:missile())
    else:
        canvas.delete(leftBullet)
        canvas.delete(rightBullet)
        canvas.delete(middleBullet)
        Shoot()

def Shoot():

    global airplane_fly, leftBullet, rightBullet,middleBullet
    X1 = canvas.coords(airplane_fly)[0]
    Y1 = canvas.coords(airplane_fly)[1]
    leftBullet = canvas.create_image(X1 +120, Y1 -20, image = bullets)
    middleBullet = canvas.create_image(X1 +150, Y1 , image = bullets)
    rightBullet = canvas.create_image(X1 + 120, Y1 +20, image = bullets)
    missile()
# function move

def moveLeft(event):
    if canvas.coords(airplane_fly)[0] > 100:
        canvas.move(airplane_fly, -20, 0)

def moveRight(event):
    if canvas.coords(airplane_fly)[0] < 1200:
        canvas.move(airplane_fly, 20, 0)

def moveUp(event):  
    if canvas.coords(airplane_fly)[1] > 50:
        canvas.move(airplane_fly, 0, -20)

def moveDown(event):
    if canvas.coords(airplane_fly)[1] < 750:
        canvas.move(airplane_fly, 0, 20)
# function enemy
def monster1():
    global x,y1,my_circle
    canvas.moveto(my_circle,x,y1)
    if x >50:
        x-=40
        canvas.after(300,lambda: monster1())
    else:
        x = 1100
        canvas.after(300,lambda :monster1())
def monster2():
    global x,y2,my_circles
    canvas.moveto(my_circles,x,y2)
    if x >50:
        x-=40
        canvas.after(300,lambda: monster2())
    else:
        x = 1100
        canvas.after(300,lambda :monster2())
def monster3():
    global x,y2,my_circles
    canvas.moveto(my_circles,x,y2)
    if x >50:
        x-=40
        canvas.after(300,lambda: monster3())
    else:
        x = 1100
        canvas.after(300,lambda :monster3())

#BINDING------------------------------------------------------------------------------
monster1()
monster2()
monster3()
Shoot()      
root.bind_all("<Left>", moveLeft) 
root.bind_all("<Right>", moveRight)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)

canvas.pack(expand=True,fill="both")
root.resizable(True,True)

root.mainloop() 
