import tkinter as tk
import StateMachine

# --- STATES ---
states = ['A', 'B', 'C', 'D', 'E']

# --- TRANSITIONS ---
transitions = [
    {'trigger' : 'a', 'src' : 'A', 'target' : 'B'},
    {'trigger' : 'a', 'src' : 'B', 'target' : 'D'},
    {'trigger' : 'b', 'src' : 'B', 'target' : 'C'},
    {'trigger' : 'a', 'src' : 'C', 'target' : 'D'},
    {'trigger' : 'b', 'src' : 'C', 'target' : 'C'},
    {'trigger' : 'a', 'src' : 'D', 'target' : 'E'},
    {'trigger' : 'b', 'src' : 'D', 'target' : 'E'},
    {'trigger' : 'a', 'src' : 'E', 'target' : 'E'},
    {'trigger' : 'b', 'src' : 'E', 'target' : 'E'}
]

# Color red the path the state machine takes.
def showTransitions(color, statesPassed):
    for state in statesPassed:

        a, b, c = state
        canvas.itemconfigure(sA, fill=color)

        if a == 'A' and b == 'B':
            canvas.itemconfigure(sB, fill=color)
            canvas.itemconfigure(aAB, fill=color)
        if a == 'B' and b == 'D':
            canvas.itemconfigure(sD, fill=color)
            canvas.itemconfigure(aBD, fill=color)
        if a == 'B' and b == 'C':
            canvas.itemconfigure(sC, fill=color)
            canvas.itemconfigure(aBC, fill=color)
        if a == 'D' and b == 'E' and c == 'a':
            canvas.itemconfigure(sE, fill=color)
            canvas.itemconfigure(aDE, fill=color)
            canvas.itemconfigure(tDEa, fill=color)
        if a == 'D' and b == 'E' and c == 'b':
            canvas.itemconfigure(sE, fill=color)
            canvas.itemconfigure(aDE, fill=color)
            canvas.itemconfigure(tDEb, fill=color)
        if a == 'C' and b == 'D':
            canvas.itemconfigure(sD, fill=color)
            canvas.itemconfigure(aCD, fill=color)
        if a == 'C' and b == 'C':
            canvas.itemconfigure(arcC, outline=color)
        if a == 'E' and b == 'E' and c == 'a':
            canvas.itemconfigure(arcE, outline=color)
            canvas.itemconfigure(tEEa, fill=color)
        if a == 'E' and b == 'E' and c == 'b':
            canvas.itemconfigure(arcE, outline=color)
            canvas.itemconfigure(tEEb, fill=color)

# Colors everything back to black.
def resetTransiotions():
    canvas.itemconfigure(sA, fill='black')
    canvas.itemconfigure(sB, fill='black')
    canvas.itemconfigure(sC, fill='black')
    canvas.itemconfigure(sD, fill='black')
    canvas.itemconfigure(sE, fill='black')
    canvas.itemconfigure(aAB, fill='black')
    canvas.itemconfigure(aBD, fill='black')
    canvas.itemconfigure(aDE, fill='black')
    canvas.itemconfigure(aBC, fill='black')
    canvas.itemconfigure(aCD, fill='black')
    canvas.itemconfigure(arcC, outline='black')
    canvas.itemconfigure(arcE, outline='black')
    canvas.itemconfigure(tDEa, fill='black')
    canvas.itemconfigure(tDEb, fill='black')
    canvas.itemconfigure(tEEa, fill='black')
    canvas.itemconfigure(tEEb, fill='black')

# Determines whether the regular expression is accepted or not. If accepted draws the path taken by the
# state machine and displays a message saying it was accepted. If denied, it displays a message saying
# it was denied.
def accepted():

    resetTransiotions()
    re = str(entry.get())

    test = StateMachine.StateMachine(states, 'A', transitions)
    tof = test.transitionRE(re)
    if not test.accepted:
        tof = False

    if tof:
        test.currState = 'A'
        statesPassed = []
        statesPassed.append((test.getstate(), test.getstate(), ' '))

        for letter in re:
            test.transition(letter)
            statesPassed.append((test.prevState, test.getstate(), test.currTrigg))

        showTransitions('red', statesPassed)

    if tof:
        status = 'accepted.'
    else:
        status = 'denied.'

    acceptedTxt.configure(text=(str(tof) + '. Your regular expression has been ' + status))


#Code below creates GUI.
window = tk.Tk()

window.geometry('500x500')
window.title('Regular expression = ab*(a|b)*')

entry = tk.Entry()
entry.pack()

button = tk.Button(text='Insert regular expression', command=accepted)
button.pack()

canvas = tk.Canvas(window, width=400, height=200)
canvas.pack()

acceptedTxt = tk.Label()
acceptedTxt.pack()


# Code below creates the state machine diagram.
oA = canvas.create_oval(25, 50, 75, 100)
oB = canvas.create_oval(125, 50, 175, 100)
oC = canvas.create_oval(125, 150, 175, 200)
oD = canvas.create_oval(225, 50, 275, 100)
oE = canvas.create_oval(325, 50, 375, 100)
oDacc = canvas.create_oval(230, 55, 270, 95)
oEacc = canvas.create_oval(330, 55, 370, 95)


aAB = canvas.create_line(75, 75, 125, 75, arrow=tk.LAST)
aBD = canvas.create_line(175, 75, 225, 75, arrow=tk.LAST)
aDE = canvas.create_line(275, 75, 325, 75, arrow=tk.LAST)
aBC = canvas.create_line(150, 100, 150, 150, arrow=tk.LAST)
aCD = canvas.create_line(175, 175, 250, 100, arrow=tk.LAST)

arcC = canvas.create_arc(50, 160, 200, 190, style=tk.ARC, start=90, extent=180)
arcE = canvas.create_arc(330, 10, 370, 100, style=tk.ARC, start=0, extent=180)

sA = canvas.create_text(50, 75, text='A')
sB = canvas.create_text(150, 75, text='B')
sC = canvas.create_text(150, 175, text='C')
sD = canvas.create_text(250, 75, text='D')
sE = canvas.create_text(350, 75, text='E')

tAB = canvas.create_text(100, 60, text='a')
tBC = canvas.create_text(160, 120, text='b')
tBD = canvas.create_text(200, 60, text='a')
tCC = canvas.create_text(50, 160, text='b')
tCD = canvas.create_text(220, 150, text='a')
tDEa = canvas.create_text(300, 60, text='a')
tDEb = canvas.create_text(300, 90, text='b')
tEEa = canvas.create_text(385, 30, text='a')
tEE = canvas.create_text(390, 30, text='|')
tEEb = canvas.create_text(396, 30, text='b')

window.mainloop()