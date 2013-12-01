# -*- coding:utf-8 -*-
import Tkinter as Tk

class Frame(Tk.Frame):
    """Frame with three label"""

    def __init__(self, master=None):
        Tk.Frame.__init__(self, master, height=200, width=200)
        self.master.title('Pack Three Labels')

        # First label
        la = Tk.Label(self, text='Hello everybody', bg='yellow', relief=Tk.RIDGE, bd=2)
        la.pack(padx=5,pady=5, fill=Tk.X)

        # Second label
        lb = Tk.Label(self, text='OMG!', bg='red', relief=Tk.RIDGE, bd=2)
        lb.pack(padx=5,pady=5, fill=Tk.X)

        # Third label
        lc = Tk.Label(self, text='Goodbye', bg='lightSkyBlue', relief=Tk.RIDGE, bd=2)
        lc.pack(padx=5,pady=5)

if __name__=='__main__':
    f = Frame()
    f.pack()
    f.mainloop()
