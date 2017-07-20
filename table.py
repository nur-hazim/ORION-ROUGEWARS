from tkinter import *
from tkinter.ttk import *
import random
rankingList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
team1list = [[1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0], [8,0], [9,0], [10,0], [11,0], [12,0], [13,0], [14,0], [15,0], [16,0], [17,0], [18,0], [19,0], [20,0]]



class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('teamnum', 'school', 'points')
        tv.heading("#0", text='Ranking')
        tv.column("#0", anchor="e", width=100)
        tv.heading('teamnum', text='Team Number')
        tv.column('teamnum', anchor='center', width=100)
        tv.heading('school', text='School')
        tv.column('school', anchor='center', width=100)
        tv.heading('points', text='Points')
        tv.column('points', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        

    def LoadTable(self):
        for i in rankingList:
            self.treeview.insert('', 'end', text=i, values=(
                             'Teams {}'.format(i), 'ALIBABA', 0))

def main():
    root = Tk()
    App(root)
    root.mainloop()
    

if __name__ == '__main__':
    main()
    
