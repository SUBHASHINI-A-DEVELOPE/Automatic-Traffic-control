from tkinter import*

def red():
    canvas1.create_oval(120,120,50,50,fill = 'red', outline = 'lightgray', width = 4)
    canvas2.create_oval(120,120,50,50,fill = 'white', outline = 'lightgray', width = 4)
    canvas3.create_oval(120,120,50,50,fill = 'white', outline = 'lightgray', width = 4)
    
def orange():
    canvas1.create_oval(120,120,50,50,fill = 'white', outline = 'lightgray', width = 4)
    canvas2.create_oval(120,120,50,50,fill = 'orange', outline = 'lightgray', width = 4)
    canvas3.create_oval(120,120,50,50,fill = 'white', outline = 'lightgray', width = 4)
    
def green():
    canvas1.create_oval(120,120,50,50,fill = 'white', outline = 'lightgray', width = 4)
    canvas2.create_oval(120,120,50,50,fill = 'white', outline = 'lightgray', width = 4)
    canvas3.create_oval(120,120,50,50,fill = 'green', outline = 'lightgray', width = 4)
    
count = 25
def start():
    counter(count)
    
def new(c):
    if c>15:
        red()
        e.config(text = c)
        play.update()
        sleep(1)
        counter(c)
        
    elif c>10 and c<= 15:
        orange()
        e.config(text = c)
        play.update()
        sleep(1)
        counter(c)
        
    elif c>0 and c<=10:
        green()
        e.config(text = c)
        play.update()
        sleep(1)
        counter(c)
        
    elif c == 0:
        count = 25
        red()
        e.config(text = c)
        play.update()
        sleep(1)
        counter(count)
        
def counter(value):
    if value>0:
       value = value-1
    new(value)
    
play = Tk()
play.geometry('300x400')
play.title('Traffic light - Automatic')
play.configure(bg = 'gray')
e = Label(play, font = ('calibri', '14', 'bold'), fg = 'red')
e.pack()

canvas1 = Canvas(play,height = 13, bg = 'black')
canvas1.pack()

canvas2 = Canvas(play,height = 13, bg = 'black')
canvas2.pack()

canvas3 = Canvas(play,height = 13, bg = 'black')
canvas3.pack()

button1 = Button(play, text = 'start', font = ('Arial',13), bg = 'lightgray', height = '1', width = '12', command = start)
button1.pack()

play.mainloop()
    
