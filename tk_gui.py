
import sys
from tkinter.filedialog import askopenfilename
from campionato import Campionato
from dati import DatiPartite
#import metodi
from acquisizione import Acquisizione
import tkinter.messagebox
import requests

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

primo_tempo=False


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        return

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






def setPrimoTempo():
    global primo_tempo
    if not primo_tempo:
        primo_tempo=True
    else:
        primo_tempo=False



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
        self.squadre.configure(text='''Squadre''',command=self.stampa_squadre)



        self.classifica1tp = Button(top)
        self.classifica1tp.place(relx=0.56, rely=0.54, height=32, width=127)
        self.classifica1tp.configure(activebackground="#d9d9d9")
        self.classifica1tp.configure(activeforeground="#000000")
        self.classifica1tp.configure(background="#d9d9d9")
        self.classifica1tp.configure(foreground="#000000")
        self.classifica1tp.configure(highlightbackground="#d9d9d9")
        self.classifica1tp.configure(highlightcolor="black")
        self.classifica1tp.configure(text='''Ultimi 5 Risultati''', command=self.ultimi_risultati)
        self.classifica1tp.configure(width=87)

        self.risultati = Button(top)
        self.risultati.place(relx=0.31, rely=0.54, height=32, width=87)
        self.risultati.configure(activebackground="#d9d9d9")
        self.risultati.configure(activeforeground="#000000")
        self.risultati.configure(background="#d9d9d9")
        self.risultati.configure(foreground="#000000")
        self.risultati.configure(highlightbackground="#d9d9d9")
        self.risultati.configure(highlightcolor="black")
        self.risultati.configure(text='''Classifica''', command=self.classifica)
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

        self.campionato = Entry(top)
        self.campionato.place(relx=0.3, rely=0.3, relheight=0.05, relwidth=0.3)
        self.campionato.configure(background="white")
        self.campionato.configure(font="TkFixedFont")
        self.campionato.configure(foreground="#000000")
        self.campionato.configure(highlightbackground="#d9d9d9")
        self.campionato.configure(highlightcolor="black")
        self.campionato.configure(insertbackground="black")
        self.campionato.configure(selectbackground="#c4c4c4")
        self.campionato.configure(selectforeground="black")



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


        self.interok = Entry(top)
        self.interok.place(relx=0.3, rely=0.44, relheight=0.05, relwidth=0.3)
        self.interok.configure(background="white")
        self.interok.configure(font="TkFixedFont")
        self.interok.configure(foreground="#000000")
        self.interok.configure(highlightbackground="#d9d9d9")
        self.interok.configure(highlightcolor="black")
        self.interok.configure(insertbackground="black")
        self.interok.configure(selectbackground="#c4c4c4")
        self.interok.configure(selectforeground="black")

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

        self.squadra = Entry(top)
        self.squadra.place(relx=0.3, rely=0.23, relheight=0.05, relwidth=0.3)
        self.squadra.configure(background="white")
        self.squadra.configure(font="TkFixedFont")
        self.squadra.configure(foreground="#000000")
        self.squadra.configure(highlightbackground="#d9d9d9")
        self.squadra.configure(highlightcolor="black")
        self.squadra.configure(insertbackground="black")
        self.squadra.configure(selectbackground="#c4c4c4")
        self.squadra.configure(selectforeground="black")

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

        self.giornata = Entry(top)
        self.giornata.place(relx=0.3, rely=0.16, relheight=0.05, relwidth=0.3)
        self.giornata.configure(background="white")
        self.giornata.configure(font="TkFixedFont")
        self.giornata.configure(foreground="#000000")
        self.giornata.configure(highlightbackground="#d9d9d9")
        self.giornata.configure(highlightcolor="black")
        self.giornata.configure(insertbackground="black")
        self.giornata.configure(selectbackground="#c4c4c4")
        self.giornata.configure(selectforeground="black")

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
        self.classifica1.configure(text='''Sfoglia''', command=self.chooseFile)
        self.classifica1.configure(width=97)

        self.giorno = Entry(top)
        self.giorno.place(relx=0.3, rely=0.37, relheight=0.05, relwidth=0.3)
        self.giorno.configure(background="white")
        self.giorno.configure(font="TkFixedFont")
        self.giorno.configure(foreground="#000000")
        self.giorno.configure(highlightbackground="#d9d9d9")
        self.giorno.configure(highlightcolor="black")
        self.giorno.configure(insertbackground="black")
        self.giorno.configure(selectbackground="#c4c4c4")
        self.giorno.configure(selectforeground="black")

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


        var = IntVar()
        R1=self.Radiobutton = Radiobutton(top)
        R1=self.Radiobutton.place(relx=0.67, rely=0.19, relheight=0.04, relwidth=0.17)
        R1=self.Radiobutton.configure(activebackground="#d9d9d9")
        R1=self.Radiobutton.configure(activeforeground="#000000")
        R1=self.Radiobutton.configure(background="#d9d9d9")
        R1=self.Radiobutton.configure(foreground="#000000")
        R1=self.Radiobutton.configure(highlightbackground="#d9d9d9")
        R1=self.Radiobutton.configure(highlightcolor="black")
        R1=self.Radiobutton.configure(justify=LEFT)
        R1=self.Radiobutton.configure(text='''Max Goal''',variable=var, value=1, command=self.max_goal)

        R2=self.Radiobutton = Radiobutton(top)
        R2=self.Radiobutton.place(relx=0.67, rely=0.3, relheight=0.04, relwidth=0.17)
        R2=self.Radiobutton.configure(activebackground="#d9d9d9")
        R2=self.Radiobutton.configure(activeforeground="#000000")
        R2=self.Radiobutton.configure(background="#d9d9d9")
        R2=self.Radiobutton.configure(foreground="#000000")
        R2=self.Radiobutton.configure(highlightbackground="#d9d9d9")
        R2=self.Radiobutton.configure(highlightcolor="black")
        R2=self.Radiobutton.configure(justify=LEFT)
        R2=self.Radiobutton.configure(text='''Min Goal''', variable=var, value=2, command=self.min_goal)

        R3=self.Radiobutton = Radiobutton(top)
        R3=self.Radiobutton.place(relx=0.67, rely=0.4, relheight=0.04, relwidth=0.17)
        R3=self.Radiobutton.configure(activebackground="#d9d9d9")
        R3=self.Radiobutton.configure(activeforeground="#000000")
        R3=self.Radiobutton.configure(background="#d9d9d9")
        R3=self.Radiobutton.configure(foreground="#000000")
        R3=self.Radiobutton.configure(highlightbackground="#d9d9d9")
        R3=self.Radiobutton.configure(highlightcolor="black")
        R3=self.Radiobutton.configure(justify=LEFT)
        R3=self.Radiobutton.configure(text='''Diff Goal''', variable=var, value=3, command=self.diff_goal)


        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.62, rely=0.63, relheight=0.04, relwidth=0.17)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''1° Tempo''', command=setPrimoTempo)


        self.squadre1 = Button(top)
        self.squadre1.place(relx=0.08, rely=0.63, height=32, width=77)
        self.squadre1.configure(activebackground="#d9d9d9")
        self.squadre1.configure(activeforeground="#000000")
        self.squadre1.configure(background="#d9d9d9")
        self.squadre1.configure(foreground="#000000")
        self.squadre1.configure(highlightbackground="#d9d9d9")
        self.squadre1.configure(highlightcolor="black")
        self.squadre1.configure(relief=RAISED)
        self.squadre1.configure(text='''Partite''', command=self.partite)

        self.squadre2 = Button(top)
        self.squadre2.place(relx=0.32, rely=0.63, height=32, width=97)
        self.squadre2.configure(activebackground="#d9d9d9")
        self.squadre2.configure(activeforeground="#000000")
        self.squadre2.configure(background="#d9d9d9")
        self.squadre2.configure(foreground="#000000")
        self.squadre2.configure(highlightbackground="#d9d9d9")
        self.squadre2.configure(highlightcolor="black")
        self.squadre2.configure(relief=RAISED)
        self.squadre2.configure(text='''Max Vittorie''', command=self.dati_squadra)
        self.squadre2.configure(width=97)

    def chooseFile(self):
        try:
            filename = askopenfilename()
            acquisisci = Acquisizione()
            self.dati = acquisisci.acquisisci(filename)
            self.richiesta = requests.Richieste(self.dati)
            tkinter.messagebox.showinfo('Success', 'File caricato!')

        except ValueError:
            tkinter.messagebox.showinfo('Error', 'Si è verificato un errore!')
        except FileNotFoundError:
            return


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




    def stampa_squadre(self):
        try:
            str = ''
            var=self.campionato.get()
            for element in list(self.richiesta.richiesta_uno(var)):
                str+=element+ '\n'
            tkinter.messagebox.showinfo('Squadre', str)

        except KeyError:
            tkinter.messagebox.showinfo('Error','Campionato non presente!')
        except AttributeError:
            tkinter.messagebox.showinfo('Error', 'File non caricato!')

    def classifica(self):

        try:
            if self.richiesta is None:
                raise AttributeError
            if self.giornata.get() == '':
                var = 1
                raise KeyError

            elif self.campionato.get() == '':
                var = 2
                raise KeyError
            else:

                var1 = int(self.giornata.get())
                var2 = self.campionato.get()

            if primo_tempo==False:
                classifica, avversari = self.richiesta.richiesta_due(var1, var2)
                string = "Squadra - Punti - Partite giocate:\n"
                for element in classifica:
                    pg = avversari[element[0]]
                    string += element[0] + " - " + str(element[1]) + " - " + str(pg) + "\n"
                tkinter.messagebox.showinfo('Classifica',string)
            else:
                classifica, avversari = self.richiesta.richiesta_tre(var1, var2)
                string = "Squadra - Punti - Partite giocate:\n"
                for element in classifica:
                    pg = avversari[element[0]]
                    string += element[0] + " - " + str(element[1]) + " - " + str(pg) + "\n"
                tkinter.messagebox.showinfo('Classifica', string)
        except KeyError:

                if var==1:
                    tkinter.messagebox.showinfo('Error', 'Giornata non presente!')
                    return
                elif var==2:
                    tkinter.messagebox.showinfo('Error', 'Campionato non presente!')
                    return

        except AttributeError:
            tkinter.messagebox.showinfo('Error', 'File non caricato!')

    def ultimi_risultati(self):
        try:
            if self.richiesta is None:
                raise AttributeError
            if self.giornata.get() == '':
                var = 1
                raise KeyError

            elif self.squadra.get() == '':
                var = 2
                raise KeyError
            else:

                var1 = int(self.giornata.get())
                var2 = self.squadra.get()
                classifica = self.richiesta.richiesta_quattro(var1, var2)
                i=0
                str2=''
                for element in classifica:
                    i+=1
                    str2+= "Giornata " + str(var1- len(classifica) + i) + '  ' +element +'\n'
                tkinter.messagebox.showinfo('Ultimi 5 risultati', str2)

        except KeyError:

                if var==1:
                    tkinter.messagebox.showinfo('Error', 'Giornata non presente!')
                    return
                elif var==2:
                    tkinter.messagebox.showinfo('Error', 'Squadra non presente!')
                    return

        except AttributeError:
            tkinter.messagebox.showinfo('Error', 'File non caricato!')


    def partite(self):
        try:
            if self.richiesta is None:
                raise AttributeError

            if self.giorno.get() == '':
                var = 1
                raise KeyError

            else:
                var2 = self.giorno.get()
                var3=var2.split('/')
                var1=var3[2]+ ','+ var3[1]+','+ var3[0]
                partite = self.richiesta.richiesta_cinque(var1)
                str1=''
                for element in list(self.richiesta.richiesta_cinque(var1)):
                    str1 += element + '\n'
                print('\n\nPartite del '+ var2+':'+'\n\n' + str1)

        except KeyError:
                if var==1:
                    tkinter.messagebox.showinfo('Error', 'Giorno non presente!')
                    return

        except AttributeError:
            tkinter.messagebox.showinfo('Error', 'File non caricato!')


    def max_goal(self):
        try:
            if self.richiesta is None:
                raise AttributeError
            if self.giornata.get() == '':
                var = 1
                raise KeyError

            elif self.interok.get() == '':
                var = 2
                raise KeyError
            else:
                var1 = int(self.giornata.get())
                var2 = int(self.interok.get())

                str1 = ''
                for element in list(self.richiesta.richiesta_sei(var1,var2)):
                    str1 += element + '\n'
                tkinter.messagebox.showinfo('Le ' +str(var2) +' squadre con più goal fatti:  ', str1)

        except KeyError:

            if var == 1:
                tkinter.messagebox.showinfo('Error', 'Giornata non presente!')
                return
            elif var == 2:
                tkinter.messagebox.showinfo('Error', 'Intero k non presente!')
                return

        except AttributeError:
            tkinter.messagebox.showinfo('Error', 'File non caricato!')

    def min_goal(self):
        try:
            if self.richiesta is None:
                raise AttributeError
            if self.giornata.get() == '':
                var = 1
                raise KeyError

            elif self.interok.get() == '':
                var = 2
                raise KeyError
            else:
                var1 = int(self.giornata.get())
                var2 = int(self.interok.get())
                str1 = ''
                for element in list(self.richiesta.richiesta_sei(var1, var2)):
                    str1 += element + '\n'
                tkinter.messagebox.showinfo('Le ' +str(var2) +' squadre con meno goal subiti:  ', str1)
        except KeyError:

            if var == 1:
                tkinter.messagebox.showinfo('Error', 'Giornata non presente!')
                return
            elif var == 2:
                tkinter.messagebox.showinfo('Error', 'Intero k non presente!')
                return

        except AttributeError:
            tkinter.messagebox.showinfo('Error', 'File non caricato!')

    def diff_goal(self):
        try:
            if self.richiesta is None:
                raise AttributeError
            if self.giornata.get() == '':
                var = 1
                raise KeyError

            elif self.interok.get() == '':
                var = 2
                raise KeyError
            else:
                var1 = int(self.giornata.get())
                var2 = int(self.interok.get())
                str1 = ''
                for element in list(self.richiesta.richiesta_sei(var1, var2)):
                    str1 += element + '\n'
                tkinter.messagebox.showinfo('Le ' +str(var2) +' squadre con migliore differenza reti:  ', str1)
        except KeyError:

            if var == 1:
                tkinter.messagebox.showinfo('Error', 'Giornata non presente!')
                return
            elif var == 2:
                tkinter.messagebox.showinfo('Error', 'Intero k non presente!')
                return

        except AttributeError:
            tkinter.messagebox.showinfo('Error', 'File non caricato!')


    def dati_squadra(self):
        try:
            if self.richiesta is None:
                raise AttributeError
            if self.giornata.get() == '':
                var = 1
                raise KeyError

            elif self.campionato.get() == '':
                var = 2
                raise KeyError
            else:

                var1 = int(self.giornata.get())
                var2 = self.campionato.get()


            result= self.richiesta.richiesta_nove(var1, var2)
            string = "MaxWin - MaxWinHome - MaxWinAway:\n" + result[0] + " - " + result[1] + " - " + result[2]

            tkinter.messagebox.showinfo('Risultati',string)

        except KeyError:

                if var==1:
                    tkinter.messagebox.showinfo('Error', 'Giornata non presente!')
                    return
                elif var==2:
                    tkinter.messagebox.showinfo('Error', 'Campionato non presente!')
                    return

        except AttributeError:
            tkinter.messagebox.showinfo('Error', 'File non caricato!')

if __name__ == '__main__':
    vp_start_gui()



