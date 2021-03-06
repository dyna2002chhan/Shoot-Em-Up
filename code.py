#IMPORT -----------------------------------------------------------------------------

from tkinter import *
import tkinter as tk
import random

#VARIABLES---------------------------------------------------------------------------

w = 1200
h = 700
x= w//2
y = h//2
xs=1200
y2 = 300
y1 = 500
#CONSTANT----------------------------------------------------------------------------


root= tk.Tk()
root.title("cute")
root.geometry("1300x800")
canvas=tk.Canvas(root)
score =0
lives = 3

#GRAPHIC-----------------------------------------------------------------------------

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
plane1= tk.PhotoImage(file="1enemy.png")
my_plane1= canvas.create_image(1100,y-200,image=plane1) 

plane2= tk.PhotoImage(file="2enemy.png")
my_plane2= canvas.create_image(1100,y,image=plane2) 

# FUNCTIONS------------------------------------------------------------------------- 

def missile():

    global upBullet, downBullet, middleBullet
    canvas.move(upBullet,30,0)
    canvas.move(downBullet, 30, 0)
    canvas.move(middleBullet,40, 0)
    myY = canvas.coords(upBullet)[1]
    
    
    if myY >0:
        canvas.after(100, lambda:missile())
    else:
        canvas.delete(leftBullet)
        canvas.delete(rightBullet)
        canvas.delete(middleBullet)
        Shoot()

def Shoot():

    global airplane_fly, upBullet, downBullet,middleBullet
    X1 = canvas.coords(airplane_fly)[0]
    Y1 = canvas.coords(airplane_fly)[1]
    upBullet = canvas.create_image(X1 +120, Y1 -20, image = bullets)
    middleBullet = canvas.create_image(X1 +150, Y1 , image = bullets)
    downBullet = canvas.create_image(X1 + 120, Y1 +20, image = bullets)
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
    global xs,y1,my_plane1
    canvas.moveto(my_plane1,xs,y1)
    if xs >50:
        xs-=40
        canvas.after(300,lambda: monster1())
    else:
        xs = 1100
        canvas.after(300,lambda :monster1())
def monster2():
    global xs,y2,my_plane2
    canvas.moveto(my_plane2,xs,y2)
    if xs >50:
        xs-=40
        canvas.after(300,lambda: monster2())
    else:
        xs = 1100
        canvas.after(300,lambda :monster2())


#BINDING------------------------------------------------------------------------------
monster1()
monster2()

Shoot()      
root.bind_all("<Left>", moveLeft) 
root.bind_all("<Right>", moveRight)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)

canvas.pack(expand=True,fill="both")
root.resizable(True,True)

root.mainloop()