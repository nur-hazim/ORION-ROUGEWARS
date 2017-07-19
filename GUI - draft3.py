import tkinter as tk



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


def create_window():
    window = tk.Toplevel(root)
    window.geometry("500x520")

    


def refresh():
    root
    print("Refreshed")

#main window    
root = tk.Tk()
root.title("StrITwise: The Final Battle")
root.geometry("400x420")
#main window refresh button

refresh = tk.Button(root, text="Refresh", command= refresh)
refresh.pack()

#google link

Link = tk.Button(root, text="Google link")
Link.pack()

#main window result link
NewWin = tk.Button(root, text="Result Page", command= create_window)
NewWin.pack()




root.mainloop()
