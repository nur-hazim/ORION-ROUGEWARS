
from tkinter import *
from tkinter.ttk import *

team1list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

class App(Frame):

    def __init__(self, parent):
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
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        for i in team1list:
            self.treeview.insert('', 'end', text="i", values=('10:00',
                             '10:10', 'Ok'))

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
