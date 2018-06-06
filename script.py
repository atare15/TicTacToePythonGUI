#Tic-Tac-Toe
#Developed by The Binary Trio
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
E=tk.E
W=tk.W
N=tk.N
S=tk.S

LARGE_FONT = ("Verdana", 20, "bold")
playerLetter=' '
bclick=True
# Define the board
theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def isSpaceFree(board, move):
    # Returns true if the move is free on the passed board
    return board[move] == ' '

def getBoardCopy(board):
        # Make a copy of the board list and return it
        boardCopy = []
        for i in board:
            boardCopy.append(i)
        return boardCopy


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns none if there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def isWinner(b, le):
    # Takes a board and player's letter and evaluates to return true if that player has won.
    return (
            (b[7] == le and b[8] == le and b[9] == le) or  # Horizontal top
            (b[4] == le and b[5] == le and b[6] == le) or  # Horizontal middle
            (b[1] == le and b[2] == le and b[3] == le) or  # Horizontal bottom
            (b[7] == le and b[4] == le and b[1] == le) or  # Vertical left
            (b[8] == le and b[5] == le and b[2] == le) or  # Vertical middle
            (b[9] == le and b[6] == le and b[3] == le) or  # Vertical right
            (b[7] == le and b[5] == le and b[3] == le) or  # Diagonal_1
            (b[9] == le and b[5] == le and b[1] == le)  # Diagonal_2
    )

def drawBoard(board):
    #This function will print out the board that it was passed
    #the variable board is a list of 10 strings representing the board (0 is ignored)
    print(board[1]+'|'+board[2]+'|'+board[3])
    print("-------------")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-------------")
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")



def makeMoveTest(board, letter, move):
    board[move] = letter

def chooseLetter(msg):
    global playerLetter
    chooseLetter = tk.Tk()
    def leaveX():
        global playerLetter
        playerLetter='X'
        chooseLetter.destroy()
        return 'X'
    def leaveO():
        global playerLetter
        playerLetter='O'
        chooseLetter.destroy()
        return 'O'
    chooseLetter.wm_title("Choose a letter")
    chooseLetter.geometry("300x100")
    label = ttk.Label(chooseLetter, text=msg,font=('Times 18 bold'))
    label.pack()
    b1 = ttk.Button(chooseLetter, text='X', command=leaveX)
    b1.pack()
    b2 = ttk.Button(chooseLetter, text='O', command=leaveO)
    b2.pack()
    chooseLetter.mainloop()


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


class MainFrame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = tk.Frame(self, width=400, height=230, bg="lightblue")
        frame.pack_propagate(0)
        frame.pack(expand=True)
        frame1 = tk.Frame(self, width=400, height=230, bg="lightblue")
        frame1.pack_propagate(0)
        frame1.pack()
        label = tk.Label(frame, text="Welcome to Tic-Tac-Toe", font=('Times 23 bold'), bg="lightblue",
                           fg="black")
        label.pack()
        label1 =tk.Label(frame, text="Developed by The Binary Trio", font=('Times 14 bold'), bg="lightblue",
                            fg="black")
        label1.pack()
        label2 = tk.Label(frame1, text="Choose a game mode", font=('Times 18 bold'), bg="lightblue",
                          fg="red")
        label2.pack()
        newGame = tk.Button(frame1, font=('Times 18 bold'), text="1 Player",command=lambda: [controller.show_frame(PageOne),chooseLetter("Choose a letter to play")], bg='black', fg="white",
                              activebackground='skyblue')
        newGame.pack()
        newGame2 = tk.Button(frame1, font=('Times 18 bold'), text="2 Players",
                            command=lambda:[controller.show_frame(PageTwo)], bg='black', fg="white",
                            activebackground='skyblue')
        newGame2.pack()
        quitButton = tk.Button(frame1, font=('Times 18 bold'), text="Quit Game", command=self.quit, bg='black',
                                 fg="white", activebackground='skyblue')
        quitButton.pack()


class PageOne(tk.Frame):
    global playerLetter
    move = 0
    def __init__(self, parent, controller):
        global playerLetter
        global move
        tk.Frame.__init__(self, parent, bg="light sea green")
        self.grid(sticky=N + S + E + W)
        button1 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='lightblue', fg='black', height=4, width=8,
                            command=lambda: makePlayerMove(button1, 1))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='lightblue', fg='black', height=4, width=8,
                            command=lambda: makePlayerMove(button2, 2))
        button2.grid(row=1, column=1)
        button3 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='lightblue', fg='black', height=4, width=8,
                            command=lambda: makePlayerMove(button3, 3))
        button3.grid(row=1, column=2)
        button4 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='lightblue', fg='black', height=4, width=8,
                            command=lambda: makePlayerMove(button4, 4))
        button4.grid(row=2, column=0)
        button5 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='lightblue', fg='black', height=4, width=8,
                            command=lambda: makePlayerMove(button5, 5))
        button5.grid(row=2, column=1)
        button6 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='lightblue', fg='black', height=4, width=8,
                            command=lambda: makePlayerMove(button6, 6))
        button6.grid(row=2, column=2)
        button7 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='lightblue', fg='black', height=4, width=8,
                            command=lambda: makePlayerMove(button7, 7))
        button7.grid(row=3, column=0)
        button8 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='lightblue', fg='black', height=4, width=8,
                            command=lambda: makePlayerMove(button8, 8))
        button8.grid(row=3, column=1)
        button9 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='lightblue', fg='black', height=4, width=8,
                            command=lambda: makePlayerMove(button9, 9))
        button9.grid(row=3, column=2)
        button10 = tk.Button(self, text="Reset", command=lambda: reset())
        button10.grid(row=4, column=0)

        def reset():
            global theBoard
            theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            button1["text"] = " "
            button2["text"] = " "
            button3["text"] = " "
            button4["text"] = " "
            button5["text"] = " "
            button6["text"] = " "
            button7["text"] = " "
            button8["text"] = " "
            button9["text"] = " "

        def makeMove(board, letter, move):
            board[move] = letter
            if move == 1:
                button1["text"] = letter
            elif move == 2:
                button2["text"] = letter
            elif move == 3:
                button3["text"] = letter
            elif move == 4:
                button4["text"] = letter
            elif move == 5:
                button5["text"] = letter
            elif move == 6:
                button6["text"] = letter
            elif move == 7:
                button7["text"] = letter
            elif move == 8:
                button8["text"] = letter
            elif move == 9:
                button9["text"] = letter

        def makePlayerMove(array, bId):
            computerLetter = ' '
            global playerLetter
            if playerLetter == 'X':
                computerLetter = 'O'
            elif playerLetter == 'O':
                computerLetter = 'X'
            if array["text"] == " " and playerLetter == 'X':
                array["text"] = "X"
            elif array["text"] == " " and playerLetter == 'O':
                array["text"] = "O"
            else:
                messagebox.showwarning("Invalid Move", "That spot is already taken")
                return
            move = bId

            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                popup("Horray, You Win!!")
                return
            else:
                if isBoardFull(theBoard):
                    popup("The Game is a Tie!")
                    return

            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                popup("The Computer Wins!")
                return
            else:
                if isBoardFull(theBoard):
                    popup("The Game is a Tie!")
                    return
            drawBoard(theBoard)

        def getComputerMove(board, computerLetter):
            if computerLetter == 'X':
                playerLetter = 'O'
            else:
                playerLetter = 'X'
            # check if computer can win in one move
            for i in range(1, 10):
                boardCopy = getBoardCopy(board)
                if isSpaceFree(boardCopy, i):
                    makeMoveTest(boardCopy, computerLetter, i)
                    if isWinner(boardCopy, computerLetter):
                        return i
            # check if player can win in one move
            for i in range(1, 10):
                boardCopy = getBoardCopy(board)
                if isSpaceFree(boardCopy, i):
                    makeMoveTest(boardCopy, playerLetter, i)
                    if isWinner(boardCopy, playerLetter):
                        return i
            # try to move to corner
            move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
            if move != None:
                return move
            # try to move to center
            if isSpaceFree(board, 5):
                return 5
            # try to move to middle points
            return chooseRandomMoveFromList(board, [2, 4, 6, 8])

        def popup(msg):
            popup = tk.Tk()
            def leaveX():
                reset()
                controller.show_frame(StartPage)
                popup.destroy()
            def leaveO():
                reset()
                popup.destroy()
            popup.wm_title("GAME OVER")
            popup.geometry("400x200")
            label = ttk.Label(popup, text=msg, font=LARGE_FONT)
            label.pack()
            label1 = ttk.Label(popup, text="Do you want to play again?", font=('Times 16'))
            label1.pack()
            label2 = ttk.Label(popup, text=" ", font=LARGE_FONT)
            label2.pack()
            b1 = ttk.Button(popup, text='Yes', command=leaveO)
            b1.pack()
            b2 = ttk.Button(popup, text='No', command=leaveX)
            b2.pack()
            popup.mainloop()


class PageTwo(tk.Frame):
    move=0
    bclick=True
    def __init__(self, parent, controller):
        global move
        tk.Frame.__init__(self, parent, bg="DeepSkyBlue2")
        self.grid(sticky=N + S + E + W)
        button1 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='SlateGray1', fg='black', height=4, width=8,command=lambda:makePlayerMove(button1,1))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='SlateGray1', fg='black', height=4, width=8,command=lambda:makePlayerMove(button2,2))
        button2.grid(row=1, column=1)
        button3 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='SlateGray1', fg='black', height=4, width=8,command=lambda:makePlayerMove(button3,3))
        button3.grid(row=1, column=2)
        button4 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='SlateGray1', fg='black', height=4, width=8,command=lambda:makePlayerMove(button4,4))
        button4.grid(row=2, column=0)
        button5 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='SlateGray1', fg='black', height=4, width=8,command=lambda:makePlayerMove(button5,5))
        button5.grid(row=2, column=1)
        button6 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='SlateGray1', fg='black', height=4, width=8,command=lambda:makePlayerMove(button6,6))
        button6.grid(row=2, column=2)
        button7 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='SlateGray1', fg='black', height=4, width=8,command=lambda:makePlayerMove(button7,7))
        button7.grid(row=3, column=0)
        button8 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='SlateGray1', fg='black', height=4, width=8,command=lambda:makePlayerMove(button8,8))
        button8.grid(row=3, column=1)
        button9 = tk.Button(self, text=" ", font=('Times 20 bold'), bg='SlateGray1', fg='black', height=4, width=8,command=lambda:makePlayerMove(button9,9))
        button9.grid(row=3, column=2)
        button10 = tk.Button(self,text="Reset",command=lambda : reset())
        button10.grid(row=4,column=0)

        def reset():
            global theBoard
            theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            button1["text"] = " "
            button2["text"] = " "
            button3["text"] = " "
            button4["text"] = " "
            button5["text"] = " "
            button6["text"] = " "
            button7["text"] = " "
            button8["text"] = " "
            button9["text"] = " "

        def makeMove(board, letter, move):
            board[move] = letter
            if move==1:
                button1["text"]=letter
            elif move==2:
                button2["text"]=letter
            elif move==3:
                button3["text"]=letter
            elif move==4:
                button4["text"]=letter
            elif move==5:
                button5["text"]=letter
            elif move==6:
                button6["text"]=letter
            elif move==7:
                button7["text"]=letter
            elif move==8:
                button8["text"]=letter
            elif move==9:
                button9["text"]=letter

        def makePlayerMove(array,bId):
            global bclick
            computerLetter = 'O'
            playerLetter = 'X'
            move = bId
            if array["text"] == " " and bclick == True:
                array["text"] = computerLetter
                bclick = False
                makeMove(theBoard, playerLetter, move)
            elif array["text"] == " " and bclick == False:
                array["text"] = playerLetter
                bclick = True
                makeMove(theBoard, computerLetter, move)
            else:
                messagebox.showwarning("Invalid Move", "That spot is already taken")
                return



            if isWinner(theBoard, playerLetter):
                popup("Player1 Wins!")
                return
            else:
                if isBoardFull(theBoard):
                    popup("The Game is a Tie!")
                    return

            if isWinner(theBoard, computerLetter):
                popup("Player 2 Wins!")
                return
            else:
                if isBoardFull(theBoard):
                    popup("The Game is a Tie!")
                    return
            drawBoard(theBoard)

        def getComputerMove(board, computerLetter):
            if computerLetter == 'X':
                playerLetter = 'O'
            else:
                playerLetter = 'X'
            # check if computer can win in one move
            for i in range(1, 10):
                boardCopy = getBoardCopy(board)
                if isSpaceFree(boardCopy, i):
                    makeMoveTest(boardCopy, computerLetter, i)
                    if isWinner(boardCopy, computerLetter):
                        return i
            # check if player can win in one move
            for i in range(1, 10):
                boardCopy = getBoardCopy(board)
                if isSpaceFree(boardCopy, i):
                    makeMoveTest(boardCopy, playerLetter, i)
                    if isWinner(boardCopy, playerLetter):
                        return i
            # try to move to corner
            move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
            if move != None:
                return move
            # try to move to center
            if isSpaceFree(board, 5):
                return 5
            #try to move to middle points
            return chooseRandomMoveFromList(board, [2, 4, 6, 8])



        def popup(msg):
            popup = tk.Tk()
            def leaveX():
                reset()
                controller.show_frame(StartPage)
                popup.destroy()
            def leaveO():
                reset()
                popup.destroy()
            popup.wm_title("GAME OVER")
            popup.geometry("400x200")
            label = ttk.Label(popup, text=msg, font=LARGE_FONT)
            label.pack()
            label1 = ttk.Label(popup, text="Do you want to play again?", font=('Times 16'))
            label1.pack()
            label2 = ttk.Label(popup, text=" ", font=LARGE_FONT)
            label2.pack()
            b1 = ttk.Button(popup, text='Yes', command=leaveO)
            b1.pack()
            b2 = ttk.Button(popup, text='No', command=leaveX)
            b2.pack()
            popup.mainloop()



app = MainFrame()
app.title("Tic-Tac-Toe")
app.mainloop()
