import tkinter
from tkinter import messagebox

window = tkinter.Tk()

window.iconbitmap("tic tac toe.ico")

window.title("Tic Tac Toe")

window.resizable(False,False)

click = True

count = 0

btn1 = tkinter.StringVar()
btn2 = tkinter.StringVar()
btn3 = tkinter.StringVar()
btn4 = tkinter.StringVar()
btn5 = tkinter.StringVar()
btn6 = tkinter.StringVar()
btn7 = tkinter.StringVar()
btn8 = tkinter.StringVar()
btn9 = tkinter.StringVar()

xPhoto = tkinter.PhotoImage(file="X.png")
oPhoto = tkinter.PhotoImage(file="O.png")

def play():
    button1 = tkinter.Button(window, height=9, width=19,bd=.5, relief="ridge", bg = "#F9F6EE", textvariable=btn1, command=lambda:press(1,0,0))
    button2 = tkinter.Button(window, height=9, width=19,bd=.5, relief="ridge", bg = "#F9F6EE", textvariable=btn2, command=lambda:press(2,0,1))
    button3 = tkinter.Button(window, height=9, width=19,bd=.5, relief="ridge", bg = "#F9F6EE", textvariable=btn3, command=lambda:press(3,0,2))
    button4 = tkinter.Button(window, height=9, width=19,bd=.5, relief="ridge", bg = "#F5F5DC", textvariable=btn4, command=lambda:press(4,1,0))
    button5 = tkinter.Button(window, height=9, width=19,bd=.5, relief="ridge", bg = "#F5F5DC", textvariable=btn5, command=lambda:press(5,1,1))
    button6 = tkinter.Button(window, height=9, width=19,bd=.5, relief="ridge", bg = "#F5F5DC", textvariable=btn6, command=lambda:press(6,1,2))
    button7 = tkinter.Button(window, height=9, width=19,bd=.5, relief="ridge", bg = "#EDEADE", textvariable=btn7, command=lambda:press(7,2,0))
    button8 = tkinter.Button(window, height=9, width=19,bd=.5, relief="ridge", bg = "#EDEADE", textvariable=btn8, command=lambda:press(8,2,1))
    button9 = tkinter.Button(window, height=9, width=19,bd=.5, relief="ridge", bg = "#EDEADE", textvariable=btn9, command=lambda:press(9,2,2))

    button1.grid(row=0,column=0)
    button2.grid(row=0,column=1)
    button3.grid(row=0,column=2)
    button4.grid(row=1,column=0)
    button5.grid(row=1,column=1)
    button6.grid(row=1,column=2)
    button7.grid(row=2,column=0)
    button8.grid(row=2,column=1)
    button9.grid(row=2,column=2)

def press(num,r,c):
    global click,count
    if click == True:
        labelPhoto = tkinter.Label(window,image=xPhoto)
        labelPhoto.grid(row=r,column=c)
        if num == 1:
            btn1.set("X")
        if num == 2:
            btn2.set("X")
        if num == 3:
            btn3.set("X")
        if num == 4:
            btn4.set("X")
        if num == 5:
            btn5.set("X")
        if num == 6:
            btn6.set("X")
        if num == 7:
            btn7.set("X")
        if num == 8:
            btn8.set("X")
        if num == 9:
            btn9.set("X")
        count+=1
        click = False
        checkWin()
    else:
        labelPhoto = tkinter.Label(window,image=oPhoto)
        labelPhoto.grid(row=r,column=c)
        if num == 1:
            btn1.set("O")
        if num == 2:
            btn2.set("O")
        if num == 3:
            btn3.set("O")
        if num == 4:
            btn4.set("O")
        if num == 5:
            btn5.set("O")
        if num == 6:
            btn6.set("O")
        if num == 7:
            btn7.set("O")
        if num == 8:
            btn8.set("O")
        if num == 9:
            btn9.set("O")
        count+=1
        click = True
        checkWin()

def checkWin():
    global click, count
    if(btn1.get() == "X" and btn2.get() == "X" and btn3.get() == "X" or
       btn4.get() == "X" and btn5.get() == "X" and btn6.get() == "X" or
       btn7.get() == "X" and btn8.get() == "X" and btn9.get() == "X" or
       btn1.get() == "X" and btn4.get() == "X" and btn7.get() == "X" or
       btn2.get() == "X" and btn5.get() == "X" and btn8.get() == "X" or
       btn3.get() == "X" and btn6.get() == "X" and btn9.get() == "X" or
       btn1.get() == "X" and btn5.get() == "X" and btn9.get() == "X" or
       btn3.get() == "X" and btn5.get() == "X" and btn7.get() == "X"):
        messagebox.showinfo("tic tac toe","X Wins!")
        click = True
        count = 0
        clear()
        play()

    elif(btn1.get() == "O" and btn2.get() == "O" and btn3.get() == "O" or
         btn4.get() == "O" and btn5.get() == "O" and btn6.get() == "O" or
         btn7.get() == "O" and btn8.get() == "O" and btn9.get() == "O" or
         btn1.get() == "O" and btn4.get() == "O" and btn7.get() == "O" or
         btn2.get() == "O" and btn5.get() == "O" and btn8.get() == "O" or
         btn3.get() == "O" and btn6.get() == "O" and btn9.get() == "O" or
         btn1.get() == "O" and btn5.get() == "O" and btn9.get() == "O" or
         btn3.get() == "O" and btn5.get() == "O" and btn7.get() == "O"):
        messagebox.showinfo("tic tac toe","O Wins!")
        count = 0
        clear()
        play()

    elif(count == 9):
        messagebox.showinfo("tic tac toe","Tie Game!")
        click == True
        count = 0
        clear()
        play()
def clear():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')
play()
window.mainloop()