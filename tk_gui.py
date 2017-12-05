
import sys
from tkinter.filedialog import askopenfilename

from acquisizione import Acquisizione

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None

def ChooseFile():
    filename = askopenfilename()
    acquisisci=Acquisizione()
    acquisisci.acquisisci(filename)



class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family Courier -size 13 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("504x571+667+86")
        top.title("Gruppo 13")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.squadre = Button(top)
        self.squadre.place(relx=0.08, rely=0.54, height=32, width=77)
        self.squadre.configure(activebackground="#d9d9d9")
        self.squadre.configure(activeforeground="#000000")
        self.squadre.configure(background="#d9d9d9")
        self.squadre.configure(foreground="#000000")
        self.squadre.configure(highlightbackground="#d9d9d9")
        self.squadre.configure(highlightcolor="black")
        self.squadre.configure(text='''Squadre''')

        self.classifica1tp = Button(top)
        self.classifica1tp.place(relx=0.62, rely=0.54, height=32, width=87)
        self.classifica1tp.configure(activebackground="#d9d9d9")
        self.classifica1tp.configure(activeforeground="#000000")
        self.classifica1tp.configure(background="#d9d9d9")
        self.classifica1tp.configure(foreground="#000000")
        self.classifica1tp.configure(highlightbackground="#d9d9d9")
        self.classifica1tp.configure(highlightcolor="black")
        self.classifica1tp.configure(text='''Classifica''')
        self.classifica1tp.configure(width=87)

        self.risultati = Button(top)
        self.risultati.place(relx=0.3, rely=0.54, height=32, width=127)
        self.risultati.configure(activebackground="#d9d9d9")
        self.risultati.configure(activeforeground="#000000")
        self.risultati.configure(background="#d9d9d9")
        self.risultati.configure(foreground="#000000")
        self.risultati.configure(highlightbackground="#d9d9d9")
        self.risultati.configure(highlightcolor="black")
        self.risultati.configure(text='''Ultimi 5 Risultati''')
        self.risultati.configure(width=127)

        self.Text1 = Text(top)
        self.Text1.place(relx=1.37, rely=0.56, relheight=0.13, relwidth=0.19)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(undo="1")
        self.Text1.configure(width=10)
        self.Text1.configure(wrap=WORD)

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.3, rely=0.3, relheight=0.05, relwidth=0.3)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.08, rely=0.16, height=31, width=78)
        self.Label1.configure(activebackground="#000000")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify=LEFT)
        self.Label1.configure(text='''Giornata:''')
        self.Label1.configure(width=78)

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.3, rely=0.44, relheight=0.05, relwidth=0.3)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")

        self.Label3 = Label(top)
        self.Label3.place(relx=0.08, rely=0.44, height=31, width=78)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Intero k:''')
        self.Label3.configure(width=78)

        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.3, rely=0.23, relheight=0.05, relwidth=0.3)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.Label4 = Label(top)
        self.Label4.place(relx=0.08, rely=0.23, height=31, width=80)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(justify=LEFT)
        self.Label4.configure(text='''Squadra:''')
        self.Label4.configure(width=80)

        self.Entry6 = Entry(top)
        self.Entry6.place(relx=0.3, rely=0.16, relheight=0.05, relwidth=0.3)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")

        self.Label6 = Label(top)
        self.Label6.place(relx=0.1, rely=0.05, height=24, width=83)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Percorso:''')

        self.classifica1 = Button(top)
        self.classifica1.place(relx=0.28, rely=0.05, height=22, width=97)
        self.classifica1.configure(activebackground="#d9d9d9")
        self.classifica1.configure(activeforeground="#000000")
        self.classifica1.configure(background="#d9d9d9")
        self.classifica1.configure(foreground="#000000")
        self.classifica1.configure(highlightbackground="#d9d9d9")
        self.classifica1.configure(highlightcolor="black")
        self.classifica1.configure(text='''Sfoglia''', command=ChooseFile)
        self.classifica1.configure(width=97)

        self.Entry7 = Entry(top)
        self.Entry7.place(relx=0.3, rely=0.37, relheight=0.05, relwidth=0.3)
        self.Entry7.configure(background="white")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(selectbackground="#c4c4c4")
        self.Entry7.configure(selectforeground="black")

        self.Label7 = Label(top)
        self.Label7.place(relx=0.1, rely=0.37, height=34, width=55)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(font=font9)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Giorno:''')
        self.Label7.configure(width=55)

        self.Label8 = Label(top)
        self.Label8.place(relx=0.08, rely=0.3, height=34, width=95)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(font=font9)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(justify=LEFT)
        self.Label8.configure(text='''Campionato:''')
        self.Label8.configure(width=95)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.67, rely=0.19, relheight=0.04
                , relwidth=0.17)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(text='''Max Goal''')

        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.62, rely=0.63, relheight=0.04
                , relwidth=0.17)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''1 Tempo''')

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.67, rely=0.3, relheight=0.04
                , relwidth=0.17)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''Min Goal''')

        self.Radiobutton3 = Radiobutton(top)
        self.Radiobutton3.place(relx=0.67, rely=0.4, relheight=0.04
                , relwidth=0.17)
        self.Radiobutton3.configure(activebackground="#d9d9d9")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#d9d9d9")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify=LEFT)
        self.Radiobutton3.configure(text='''Diff Goal''')

        self.squadre1 = Button(top)
        self.squadre1.place(relx=0.08, rely=0.63, height=32, width=77)
        self.squadre1.configure(activebackground="#d9d9d9")
        self.squadre1.configure(activeforeground="#000000")
        self.squadre1.configure(background="#d9d9d9")
        self.squadre1.configure(foreground="#000000")
        self.squadre1.configure(highlightbackground="#d9d9d9")
        self.squadre1.configure(highlightcolor="black")
        self.squadre1.configure(relief=RAISED)
        self.squadre1.configure(text='''Partite''')

        self.squadre2 = Button(top)
        self.squadre2.place(relx=0.32, rely=0.63, height=32, width=97)
        self.squadre2.configure(activebackground="#d9d9d9")
        self.squadre2.configure(activeforeground="#000000")
        self.squadre2.configure(background="#d9d9d9")
        self.squadre2.configure(foreground="#000000")
        self.squadre2.configure(highlightbackground="#d9d9d9")
        self.squadre2.configure(highlightcolor="black")
        self.squadre2.configure(relief=RAISED)
        self.squadre2.configure(text='''Max Vittorie''')
        self.squadre2.configure(width=97)

    @staticmethod
    def popup1(event):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event):
        Popupmenu2 = Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#f9f9f9")
        Popupmenu2.configure(activeforeground="black")
        Popupmenu2.configure(background="#d9d9d9")
        Popupmenu2.configure(disabledforeground="#a3a3a3")
        Popupmenu2.configure(foreground="black")
        Popupmenu2.post(event.x_root, event.y_root)

    @staticmethod
    def popup3(event):
        Popupmenu3 = Menu(root, tearoff=0)
        Popupmenu3.configure(activebackground="#f9f9f9")
        Popupmenu3.configure(activeforeground="black")
        Popupmenu3.configure(background="#d9d9d9")
        Popupmenu3.configure(disabledforeground="#a3a3a3")
        Popupmenu3.configure(foreground="black")
        Popupmenu3.post(event.x_root, event.y_root)

    @staticmethod
    def popup4(event):
        Popupmenu4 = Menu(root, tearoff=0)
        Popupmenu4.configure(activebackground="#f9f9f9")
        Popupmenu4.configure(activeforeground="black")
        Popupmenu4.configure(background="#d9d9d9")
        Popupmenu4.configure(disabledforeground="#a3a3a3")
        Popupmenu4.configure(foreground="black")
        Popupmenu4.post(event.x_root, event.y_root)

    @staticmethod
    def popup5(event):
        Popupmenu5 = Menu(root, tearoff=0)
        Popupmenu5.configure(activebackground="#f9f9f9")
        Popupmenu5.configure(activeforeground="black")
        Popupmenu5.configure(background="#d9d9d9")
        Popupmenu5.configure(disabledforeground="#a3a3a3")
        Popupmenu5.configure(foreground="black")
        Popupmenu5.post(event.x_root, event.y_root)

    @staticmethod
    def popup6(event):
        Popupmenu6 = Menu(root, tearoff=0)
        Popupmenu6.configure(activebackground="#f9f9f9")
        Popupmenu6.configure(activeforeground="black")
        Popupmenu6.configure(background="#d9d9d9")
        Popupmenu6.configure(disabledforeground="#a3a3a3")
        Popupmenu6.configure(foreground="black")
        Popupmenu6.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()



