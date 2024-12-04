from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("600x600")
root.title("Canvas")

label = Label(root, text="Ingresa un color en ingles: ")
Input_box = Entry(root)

label.place(relx=0.6, rely=0.9, anchor=CENTER)
Input_box.place(relx=0.83, rely=0.9, anchor=CENTER)
canvas = Canvas(root, width=590, height=510, bg="white", highlightbackground="lightGray")
canvas.pack()
direccion=""
oldX= 50
oldY= 50
newX= 50
newY= 50

def right_dir(event):
    global direccion
    global oldX
    global oldY
    global newX
    global newY
    
    oldX=newX
    oldY=newY
    newX=newX+5
    direccion = "right"
    draw(direccion, oldX, oldY, newX, newY)

def left_dir(event):
    global direccion
    global oldX
    global oldY
    global newX
    global newY
    
    oldX=newX
    oldY=newY
    newX=newX-5
    direccion = "left"
    draw(direccion, oldX, oldY, newX, newY)

def up_dir(event):
    global direccion
    global oldX
    global oldY
    global newX
    global newY
    
    oldX=newX
    oldY=newY
    newY=newY-5
    direccion = "up"
    draw(direccion, oldX, oldY, newX, newY)

def down_dir(event):
    global direccion
    global oldX
    global oldY
    global newX
    global newY
    
    oldX=newX
    oldY=newY
    newY=newY+5
    direccion = "down"
    draw(direccion, oldX, oldY, newX, newY)

def draw(direccion, oldX, oldY, newX, newY):
    fill_color = Input_box.get()
    if(direccion=="right"):
        right_line = canvas.create_line(oldX, oldY, newX, newY, fill=fill_color)
    elif(direccion=="left"):
        left_line = canvas.create_line(oldX, oldY, newX, newY, fill=fill_color)
    elif(direccion=="up"):
        up_line = canvas.create_line(oldX, oldY, newX, newY, fill=fill_color)
    elif(direccion=="down"):
        down_line = canvas.create_line(oldX, oldY, newX, newY, fill=fill_color)

root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<Down>", down_dir)


root.mainloop()