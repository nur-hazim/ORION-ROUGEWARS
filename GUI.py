import tkinter
from tkinter import *
from tkinter import messagebox

team1list = [[1,1],[2,15],[3,7],[4,4],[5,7],[6,6],[7,18],[8,8],[9,9],[10,20]]
team2list = [[11,1],[12,2],[13,3],[14,4],[15,5],[16,6],[17,7],[18,8],[19,9],[20,10]]
#team1list = [1,2,3,4,5,6,7,8,9,10]
#team2list= [11,12,13,14,15,16,17,18,19,20]
scorelist = []
scorelist2 = []

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
scorelist.sort()
scorelist.reverse()
for a in team1list:
    for b in scorelist:
        if a[1]==b:
            A = Button(text="{}".format(scorelist.index(b)+1),command=displayscore)
            A.place(x=500,y=(100+(a[0]*30)))

for i in team2list:
    scorelist2.append(i[1])
scorelist2.sort()
scorelist2.reverse()
for a in team2list:
    for b in scorelist2:
        if a[1]==b:
            B = Button(text="{}".format(scorelist2.index(b)+1),command=displayscore)
            B.place(x=700,y=(100+((a[0]-10)*30)))

            
                       
        



'''for i in team1list:
    A=Button(text="{}".format(i[a]),command = displayscore)
    A.place(x=500,y=(100+((i[a])*20)))
    #canvas.create_text(500,(100+((i+1)*20)), text = "{}".format(i+1))
    
for i in team2list:
    B=Button(text="{}".format(i[a]),command = displayscore)
    B.place(x=700,y=(100+((i[a]-10)*20)))
    #canvas.create_text(700,(100+((i+1)*20)), text = "{}".format(i+11))'''
    


window.mainloop()
