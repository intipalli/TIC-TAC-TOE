from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")
pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()
score1 = 0
score2 = 0

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=9)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=9)

bclick = True
flag = 0


def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins this round!"
        pa = p1.get() + " Wins this round!"
        checkForWin()
        flag += 1
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def checkForWin():
    global score1, score2
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        score1 = score1 + 1
        label3["text"] = score1
        again()

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        score2 = score2 + 1

        label4["text"] = score2
        again()
    elif (flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie for this Round!!")
        again()
        # disableButton()
    


def again():
    global flag, bclick
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)
    EndGame.configure(state=NORMAL)
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    flag = 0


def reset():
    Startgame.configure(state=DISABLED)
    global score1, score2, bclick
    score1 = 0
    score2 = 0
    label3["text"] = score1
    label4["text"] = score2
    p1.set("")
    p2.set("")
    global bclick, flag, player2_name, player1_name, playerb, pa
    bclick = True
    again()


buttons = StringVar()

label = Label(tk, text="Player 1:", font='Times 20 bold', bg='black', fg='white', height=1, width=8)
label.grid(row=1, column=0)

label2 = Label(tk, text="Player 2:", font='Times 20 bold', bg='blue', fg='white', height=1, width=8)
label2.grid(row=2, column=0)

label3 = Label(tk, text=score1, font='Times 20 bold', bg='black', fg='white', height=1, width=8)
label3.grid(row=1, column=10)

label4 = Label(tk, text=score2, font='Times 20 bold', bg='blue', fg='white', height=1, width=8)
label4.grid(row=2, column=10)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button1))
button1.grid(row=3, column=1, columnspan=3)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,
                 command=lambda: btnClick(button2))
button2.grid(row=3, column=4, columnspan=3)

button3 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button3))
button3.grid(row=3, column=7, columnspan=3)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,
                 command=lambda: btnClick(button4))
button4.grid(row=4, column=1, columnspan=3)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button5))
button5.grid(row=4, column=4, columnspan=3)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,
                 command=lambda: btnClick(button6))
button6.grid(row=4, column=7, columnspan=3)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button7))
button7.grid(row=5, column=1, columnspan=3)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8,
                 command=lambda: btnClick(button8))
button8.grid(row=5, column=4, columnspan=3)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button9))
button9.grid(row=5, column=7, columnspan=3)

tk.resizable(width=False, height=False)


def endgame():
    if score1 > score2:
        pa = p1.get() + " Wins the game!"
        tkinter.messagebox.showinfo("winner", pa)
    elif score2 > score1:
        playerb = p2.get() + " Wins the game!"
        tkinter.messagebox.showinfo("winner", playerb)
    else:
        tkinter.messagebox.showinfo("tie", "It's a tie for the game")
    disableButton()
    EndGame.configure(state=DISABLED)
    Startgame.configure(state=NORMAL)


EndGame = Button(tk, text="End Game", font='Times 20 bold', bg='#991f00', fg='white', height=4, width=8, command=endgame)
EndGame.grid(row=6, column=10)
Startgame = Button(tk, text="Start New\nGame", font='Times 20 bold', bg='#991f00', fg='white', height=4, width=8, command=reset)
Startgame.grid(row=6, column=0)
Startgame.configure(state=DISABLED)

tk.mainloop()
