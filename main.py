import tkinter
import tkinter as tk

App = tk.Tk()

App.title("test")

App.geometry("200x200")

playerChose = 0


def newTextWindow(title, label, type):

    def localTWQuit():
        newWindow.destroy()

    newWindow = tkinter.Toplevel(App)
    newWindow.title(title)

    tk.Label(newWindow, text=label).pack(padx = 15, pady = 5)

    if type == 1:
        tk.Button(newWindow, text="Ok", command=localTWQuit).pack(side=tk.BOTTOM, padx = 15, pady = 5)
    elif type == 2:
        tk.Button(newWindow, text="Yes", command=localTWQuit).pack(side=tk.LEFT, padx = 15, pady = 5)
        tk.Button(newWindow, text="No", command=localTWQuit).pack(side=tk.RIGHT, padx = 15, pady = 5)
    else:
        newWindow.destroy()
        newTextWindow("Error", "Wrong type of window!!!", 1)


def turns():
    None


def rpsRock():
    playerChose = 0
    print(playerChose)

    newTextWindow("Hello World!", "You've chosen Rock", 1)


def rpsPaper():
    playerChose = 1
    print(playerChose)

    newTextWindow("Hello World!", "You've chosen Paper", 2)


def rpsScissors():
    playerChose = 2
    print(playerChose)

    newTextWindow("Hello World!", "You've chosen Scissors", 3)


b_rock = tk.Button(App, text="Rock", command=rpsRock)
b_paper = tk.Button(App, text="Paper", command=rpsPaper)
b_scissors = tk.Button(App, text="Scissors", command=rpsScissors)

b_rock.pack(side=tk.LEFT)
b_paper.pack(side=tk.LEFT)
b_scissors.pack(side=tk.LEFT)

App.mainloop()
