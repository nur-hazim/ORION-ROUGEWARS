import tkinter
from tkinter import *
from tkinter import messagebox

team1list = [[1,1],[2,15],[3,7],[4,4],[5,7],[6,6],[7,18],[8,8],[9,9],[10,20]]
team2list = [[11,1],[12,2],[13,3],[14,4],[15,5],[16,6],[17,7],[18,8],[19,9],[20,10]]
scorelist = []
scorelist2 = []
teamlista = []
teamlistb = []

window = Tk()
window.title("Final Scores")
window.geometry("1280x720")

def displayscore():
   msg = messagebox.showinfo( "Score for Group", "Criteria")

def refreshscore():
    msg = messagebox.showinfo("Refreshing Scores","Scores have been refreshed")

scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT,fill = Y)

canvas= Canvas(window,width=1280, height=720, bg="white")
canvas.pack()
team1 = canvas.create_text(500,100, text = ("Team 1"))
team2 = canvas.create_text(700,100, text = ("Team 2"))
C = Button(window, text = "Refresh", command = refreshscore)
C.place(x = 50,y = 50)

#score sorting
for i in team1list:
    scorelist.append(i[1])
scorelist = list(set(scorelist))
scorelist.sort()
scorelist.reverse()
for a in scorelist:
    for b in team1list:
        if a == b[1]:
            teamlista.append(b[0])
for i in range(len(teamlista)):
        A = Button(text="{}".format(teamlista[i]),command=displayscore)
        A.place(x=500,y=(120+(i*30)))

for i in team2list:
    scorelist2.append(i[1])
scorelist2 = list(set(scorelist2))
scorelist2.sort()
scorelist2.reverse()
for a in scorelist2:
    for b in team2list:
        if a == b[1]:
            teamlistb.append(b[0])
for i in range(len(teamlistb)):
    B = Button(text="{}".format(teamlistb[i]),command=displayscore)
    B.place(x=700,y=(120+((i)*30)))

             

window.mainloop()
