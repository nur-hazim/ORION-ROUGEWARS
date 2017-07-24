import tkinter as tk
import time
import webbrowser
from tkinter import *
from table import table_results


team1list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]



'''def __init__(self, parent):
    Frame.__init__(self, parent)
    self.CreateUI()
    self.LoadTable()
    self.grid(sticky = (N,S,W,E))
    parent.grid_rowconfigure(0, weight = 1)
    parent.grid_columnconfigure
    __init__(0, weight = 1)

def CreateUI(self):
    tv = Treeview(self)
    tv['columns'] = ('ranking', 'teammem', 'school', 'points')
    tv.heading("#0", text='Sources', anchor='w')
    tv.column("#0", anchor="w")
    tv.heading('ranking', text='Ranking')
    tv.column('ranking', anchor='center', width=100)
    tv.heading('teammem', text='Team Member')
    tv.column('teammem', anchor='center', width=100)
    tv.heading('school', text='School')
    tv.column('school', anchor='center', width=100)
    tv.heading('points', text='Points')
    tv.column('points', anchor='center', width=100)
    tv.grid(sticky = (N,S,W,E))
    self.treeview = tv
    self.grid_rowconfigure(0nnk, weight = 1)
    self.grid_columnconfigure(0, weight = 1)

def LoadTable(self):
    for i in team1list:
        self.treeview.insert('', 'end', text="i", values=('10:00',
                         '10:10', 'Ok'))'''


def create_result_window():
    window = table_results()
    window.geometry("500x520")



def refresh():
    root
    print("Refreshed")




#main window    
root = tk.Tk()
root.title("StrITwise: The Final Battle")
root.geometry("400x420")
time1 = ""
clock = Label(root, font=("times", 25, "bold"), bg="white")
clock.pack(fill=BOTH, expand=1)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime("%H:%M:%S")
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()


#main window refresh button

refresh = tk.Button(root, text="Refresh", command= refresh)
refresh.pack()

#google link

Link = tk.Button(root, text="Google link")
Link.pack()

#main window result link
NewWin = tk.Button(root, text="Result Page", command= create_result_window)
NewWin.pack()




root.mainloop()
