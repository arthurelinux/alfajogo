from tkinter import*
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import random


#alfa jgo tradiciona
def alfa():
    def muda_cor():
        j['bg'] = 'DarkSlateGray'

    def muda_2():
        res = A1.get()
        res1 = B1.get()
        res2 = C1.get()
        re2 = ['A', 'a', 'B', 'b', 'C', 'c']
        if res or res1 or res2 in re2:
            j['bg'] = 'blue'
        else:
            j['bg'] = 'red'

    def a():
        a4 = A1.get()
        lista = ['A', 'a']
        if a4 in lista:
            A['bg'] = 'green'
        else:
            A['bg'] = 'red'

    def b():
        b4 = B1.get()
        lista = ['B', 'b']
        if b4 in lista:
            B['bg'] = 'green'
        else:
            B['bg'] = 'red'

    def c():
        c4 = C1.get()
        lista = ['C', 'c']
        if c4 in lista:
            C['bg'] = 'green'
        else:
            C['bg'] = 'red'

    def d():
        d4 = D1.get()
        lista = ['D', 'd']
        if d4 in lista:
            D['bg'] = 'green'
        else:
            D['bg'] = 'red'

    def e():
        e4 = E1.get()
        lista = ['E', 'e']
        if e4 in lista:
            E['bg'] = 'green'
        else:
            E['bg'] = 'red'

    def f():
        f4 = F1.get()
        lista = ['F', 'f']
        if f4 in lista:
            F['bg'] = 'green'
        else:
            F['bg'] = 'red'

    def g():
        g4 = G1.get()
        lista = ['G', 'g']
        if g4 in lista:
            G['bg'] = 'green'
        else:
            G['bg'] = 'red'

    def h():
        h4 = H1.get()
        lista = ['H', 'h']
        if h4 in lista:
            H['bg'] = 'green'
        else:
            H['bg'] = 'red'

    def i():
        i4 = I1.get()
        lista = ['I', 'i']
        if i4 in lista:
            I['bg'] = 'green'
        else:
            I['bg'] = 'red'

    def ja():
        j4 = J1.get()
        lista = ['J', 'j']
        if j4 in lista:
            J['bg'] = 'green'
        else:
            J['bg'] = 'red'

    def k():
        k4 = K1.get()
        lista = ['K', 'k']
        if k4 in lista:
            K['bg'] = 'green'
        else:
            K['bg'] = 'red'

    def l():
        l4 = L1.get()
        lista = ['L', 'l']
        if l4 in lista:
            L['bg'] = 'green'
        else:
            L['bg'] = 'red'

    def m():
        m4 = M1.get()
        lista = ['M', 'm']
        if m4 in lista:
            M['bg'] = 'green'
        else:
            M['bg'] = 'red'

    def n():
        n4 = N1.get()
        lista = ['N', 'n']
        if n4 in lista:
            N['bg'] = 'green'
        else:
            N['bg'] = 'red'

    def o():
        o4 = O1.get()
        lista = ['O', 'o']
        if o4 in lista:
            O['bg'] = 'green'
        else:
            O['bg'] = 'red'

    def p():
        p4 = P1.get()
        lista = ['P', 'p']
        if p4 in lista:
            P['bg'] = 'green'
        else:
            P['bg'] = 'red'

    def q():
        q4 = Q1.get()
        lista = ['Q', 'q']
        if q4 in lista:
            Q['bg'] = 'green'
        else:
            Q['bg'] = 'red'

    def r():
        r4 = R1.get()
        lista = ['R', 'r']
        if r4 in lista:
            R['bg'] = 'green'
        else:
            R['bg'] = 'red'

    def s():
        s4 = S1.get()
        lista = ['S', 's']
        if s4 in lista:
            S['bg'] = 'green'
        else:
            S['bg'] = 'red'

    def t():
        t4 = T1.get()
        lista = ['T', 't']
        if t4 in lista:
            T['bg'] = 'green'
        else:
            T['bg'] = 'red'

    def u():
        u4 = U1.get()
        lista = ['U', 'u']
        if u4 in lista:
            U['bg'] = 'green'
        else:
            U['bg'] = 'red'

    def v():
        v4 = V1.get()
        lista = ['V', 'v']
        if v4 in lista:
            V['bg'] = 'green'
        else:
            V['bg'] = 'red'

    def w():
        w4 = W1.get()
        lista = ['w', 'W']
        if w4 in lista:
            W['bg'] = 'green'
        else:
            W['bg'] = 'red'

    def y():
        y4 = Y1.get()
        lista = ['Y', 'y']
        if y4 in lista:
            Y['bg'] = 'green'
        else:
            Y['bg'] = 'red'

    def x():
        x4 = X1.get()
        lista = ['X', 'x']
        if x4 in lista:
            X['bg'] = 'green'
        else:
            X['bg'] = 'red'

    def z():
        z4 = Z1.get()
        lista = ['Z', 'z']
        if z4 in lista:
            Z['bg'] = 'green'
        else:
            Z['bg'] = 'red'

    j = Tk()
    j.title('alfaJOGO')

    j.geometry('1500x1500')

    La = Label(j, text='''Bem vindo! está na hora de aprender! 
        vamos encontrar as letras no seu teclado?''''', font='Helvetica 20', bg='Azure3')
    La.place (x=400, y=20)


    A = Label(j, text='A', font='Helvetica 60 bold')
    A.place(x=100, y=100)
    A1 = Entry(j)
    A1.place(x=160, y=150)
    A2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=a)
    A2.place(x=160, y=120)

    A3 = Label(j, text='')

    B = Label(j, text='B', font='Helvetica 60 bold')
    B.place(x=100, y=200)
    B1 = Entry(j)
    B1.place(x=160, y=250)
    B2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=b)
    B2.place(x=160, y=220)

    C = Label(j, text='C', font='Helvetica 60 bold')
    C.place(x=100, y=300)
    C1 = Entry(j)
    C1.place(x=160, y=350)
    C2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=c)
    C2.place(x=160, y=320)

    D = Label(j, text='D', font='Helvetica 60 bold')
    D.place(x=100, y=400)
    D1 = Entry(j)
    D1.place(x=160, y=450)
    D2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=d)
    D2.place(x=160, y=420)

    E = Label(j, text='E', font='Helvetica 60 bold')
    E.place(x=100, y=500)
    E1 = Entry(j)
    E1.place(x=160, y=550)
    E2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=e)
    E2.place(x=160, y=520)

    F = Label(j, text='F', font='Helvetica 60 bold')
    F.place(x=100, y=600)
    F1 = Entry(j)
    F1.place(x=160, y=650)
    F2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=f)
    F2.place(x=160, y=620)

    G = Label(j, text='G', font='Helvetica 60 bold')
    G.place(x=300, y=100)
    G1 = Entry(j)
    G1.place(x=360, y=150)
    G2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=g)
    G2.place(x=360, y=120)

    H = Label(j, text='H', font='Helvetica 60 bold')
    H.place(x=300, y=200)
    H1 = Entry(j)
    H1.place(x=360, y=250)
    H2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=h)
    H2.place(x=360, y=220)

    I = Label(j, text='I', font='Helvetica 60 bold')
    I.place(x=300, y=300)
    I1 = Entry(j)
    I1.place(x=360, y=350)
    I2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=i)
    I2.place(x=360, y=320)

    J = Label(j, text='J', font='Helvetica 60 bold')
    J.place(x=300, y=400)
    J1 = Entry(j)
    J1.place(x=360, y=450)
    J2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=ja)
    J2.place(x=360, y=420)

    K = Label(j, text='K', font='Helvetica 60 bold')
    K.place(x=300, y=500)
    K1 = Entry(j)
    K1.place(x=360, y=550)
    K2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=k)
    K2.place(x=360, y=520)

    L = Label(j, text='L', font='Helvetica 60 bold')
    L.place(x=300, y=600)
    L1 = Entry(j)
    L1.place(x=360, y=650)
    L2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=l)
    L2.place(x=360, y=620)

    M = Label(j, text='M', font='Helvetica 60 bold')
    M.place(x=500, y=100)
    M1 = Entry(j)
    M1.place(x=580, y=150)
    M2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=m)
    M2.place(x=580, y=120)

    N = Label(j, text='N', font='Helvetica 60 bold')
    N.place(x=500, y=200)
    N1 = Entry(j)
    N1.place(x=560, y=250)
    N2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=n)
    N2.place(x=560, y=220)

    O = Label(j, text='O', font='Helvetica 60 bold')
    O.place(x=500, y=300)
    O1 = Entry(j)
    O1.place(x=560, y=350)
    O2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=o)
    O2.place(x=560, y=320)

    P = Label(j, text='P', font='Helvetica 60 bold')
    P.place(x=500, y=400)
    P1 = Entry(j)
    P1.place(x=560, y=450)
    P2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=p)
    P2.place(x=560, y=420)

    Q = Label(j, text='Q', font='Helvetica 60 bold')
    Q.place(x=500, y=500)
    Q1 = Entry(j)
    Q1.place(x=560, y=550)
    Q2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=q)
    Q2.place(x=560, y=520)

    R = Label(j, text='R', font='Helvetica 60 bold')
    R.place(x=500, y=600)
    R1 = Entry(j)
    R1.place(x=560, y=650)
    R2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=r)
    R2.place(x=560, y=620)

    S = Label(j, text='S', font='Helvetica 60 bold')
    S.place(x=720, y=100)
    S1 = Entry(j)
    S1.place(x=780, y=150)
    S2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=s)
    S2.place(x=780, y=120)

    T = Label(j, text='T', font='Helvetica 60 bold')
    T.place(x=700, y=200)
    T1 = Entry(j)
    T1.place(x=760, y=250)
    T2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=t)
    T2.place(x=760, y=220)

    U = Label(j, text='U', font='Helvetica 60 bold')
    U.place(x=700, y=300)
    U1 = Entry(j)
    U1.place(x=760, y=350)
    U2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=u)
    U2.place(x=760, y=320)

    V = Label(j, text='V', font='Helvetica 60 bold')
    V.place(x=700, y=400)
    V1 = Entry(j)
    V1.place(x=760, y=450)
    V2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=v)
    V2.place(x=760, y=420)

    W = Label(j, text='W', font='Helvetica 60 bold')
    W.place(x=700, y=500)
    W1 = Entry(j)
    W1.place(x=780, y=550)
    W2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=w)
    W2.place(x=780, y=520)

    Y = Label(j, text='Y', font='Helvetica 60 bold')
    Y.place(x=700, y=600)
    Y1 = Entry(j)
    Y1.place(x=760, y=650)
    Y2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=y)
    Y2.place(x=760, y=620)

    X = Label(j, text='X', font='Helvetica 60 bold')
    X.place(x=920, y=100)
    X1 = Entry(j)
    X1.place(x=980, y=150)
    X2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=x)
    X2.place(x=980, y=120)

    Z = Label(j, text='Z', font='Helvetica 60 bold')
    Z.place(x=900, y=300)
    Z1 = Entry(j)
    Z1.place(x=960, y=350)
    Z2 = Button(j, text='Confirmar', bg='MidnightBlue', fg='white', command=z)
    Z2.place(x=960, y=320)

    botao = Button(j, text='cor', bg='MidnightBlue', fg='white', command=muda_cor)
    botao.place(x=1070, y=640)
    botao = Button(j, text='como vc está', bg='MidnightBlue', fg='white', command=muda_2)
    botao.place(x=1000, y=670)
    j.mainloop()
#vogais
def vogal():
    def a():
        a4 = A1.get()
        lista = ['A', 'a']
        if a4 in lista:
            al ['text'] = lista
            al ['font'] = 'enflish 30 bold'
            al ['bg'] = 'green'
            A['bg'] = 'green'
        else:
            A['bg'] = 'red'
    def e():
        e4 = E1.get()
        lista = ['E', 'e']
        if e4 in lista:
            el1 ['text'] = lista
            el1 ['font'] = 'enflish 30 bold'
            el1 ['bg'] = 'green'
            E['bg'] = 'green'
        else:
            E['bg'] = 'red'
    def i():
        i4 = I1.get()
        lista = ['I', 'i']
        if i4 in lista:
            il ['text'] = lista
            il ['font'] = 'enflish 30 bold'
            il ['bg'] = 'green'
            I['bg'] = 'green'
        else:
            I['bg'] = 'red'

    def o():
        o4 = O1.get()
        lista = ['O', 'o']
        if o4 in lista:
            ol ['text'] = lista
            ol ['font'] = 'enflish 30 bold'
            ol ['bg'] = 'green'
            O['bg'] = 'green'
        else:
            O['bg'] = 'red'

    def u():
        u4 = U1.get()
        lista = ['U', 'u']
        if u4 in lista:
            ul ['text'] = lista
            ul ['font'] = 'enflish 30 bold'
            ul ['bg'] = 'green'
            U['bg'] = 'green'
        else:
            U['bg'] = 'red'

    jd = Tk ()
    jd.title ('vogais')
    jd ['bg'] ='DarkSlateGray'
    jd.geometry ('1500x1500')

    A = Label(jd, text='A', font='Helvetica 60 bold')
    A.place(x=100, y=100)
    A1 = Entry(jd)
    A1.place(x=160, y=150)
    A2 = Button(jd, text='Confirmar', bg='MidnightBlue', fg='white', command=a)
    A2.place(x=155, y=120)
    al = Label (jd, text='')
    al.place (x=160, y=225)

    E = Label(jd, text='E', font='Helvetica 60 bold')
    E.place(x=100, y=300)
    E1 = Entry(jd)
    E1.place(x=160, y=350)
    E2 = Button(jd, text='Confirmar', bg='MidnightBlue', fg='white', command=e)
    E2.place(x=160, y=320)
    el1 = Label (jd, text='')
    el1.place (x=160, y=420)

    I = Label(jd, text='I', font='Helvetica 60 bold')
    I.place(x=100, y=500)
    I1 = Entry(jd)
    I1.place(x=160, y=550)
    I2 = Button(jd, text='Confirmar', bg='MidnightBlue', fg='white', command=i)
    I2.place(x=160, y=520)
    il=Label (jd, text='')
    il.place (x=160, y=620)


    O = Label(jd, text='O', font='Helvetica 60 bold')
    O.place(x=800, y=100)
    O1 = Entry(jd)
    O1.place(x=860, y=150)
    O2 = Button(jd, text='Confirmar', bg='MidnightBlue', fg='white', command=o)
    O2.place(x=860, y=120)
    ol = Label (jd, text='')
    ol.place (x=800,y=225)

    U = Label(jd, text='U', font='Helvetica 60 bold')
    U.place(x=800, y=300)
    U1 = Entry(jd)
    U1.place(x=860, y=350)
    U2 = Button(jd, text='Confirmar', bg='MidnightBlue', fg='white', command=u)
    U2.place(x=860, y=320)
    ul=Label (jd, text='')
    ul.place (x=860, y=420)

    jd.mainloop()

#jogo da forca
def forca():
    sorteia = random.choice
    x = open('Nomes.txt', 'r')
    lista = x.readlines()
    x.close()

    palavra = sorteia(lista).split('\n')[0].upper()
    lista_letras = []
    lista_traco = []
    lista_erro = []
    digito = []

    for i in range(len(palavra)):
        lista_letras.append(palavra[i])
        lista_traco.append('__ ')

    class arquivos:
        def __init__(self, root):

            self.canvas = Canvas(root, width=200, height=200)
            self.canvas.pack(side=LEFT)
            self.canvas1 = Frame(root)
            self.canvas1.pack()
            self.canvas2 = Frame(root)
            self.canvas2.pack()
            self.canvas3 = Frame(root)
            self.canvas3.pack()
            self.canvas4 = Frame(root)
            self.canvas4.pack()

            self.caixa = StringVar()
            root.title('Jogo da Forca - Isaias Software')

            ret = self.canvas.create_rectangle

            ret(10, 190, 190, 185, fill='black')
            ret(10, 190, 15, 10, fill='black')
            ret(10, 10, 100, 15, fill='black')
            ret(95, 10, 105, 20, fill='black')

            Label(self.canvas1, text='___________________________________________________').pack()
            Label(self.canvas1, text='Letra').pack()

            self.nom = Entry(self.canvas1, textvariable=self.caixa)
            self.nom.focus_force()
            self.nom.pack()
            self.nom.bind('<Return>', self.forca)

            Label(self.canvas1, text='___________________________________________________').pack()

            self.msg = Label(self.canvas2, text=lista_traco)
            self.msg.pack(side=LEFT)

            Label(self.canvas3, text='Letras Erradas: ').pack(side=LEFT)
            self.msg2 = Label(self.canvas3, text=lista_erro)
            self.msg2.pack()
            self.msg3 = Label(self.canvas4, text='')
            self.msg3.pack()

        def forca(self, event):

            circulo = self.canvas.create_oval
            lin = self.canvas.create_line
            boca = self.canvas.create_arc

            b = str(self.nom.get().upper()[0])  # transforma em string e só pega o primeiro
            # caracter
            for t in range(len(lista_letras)):
                if b == lista_letras[t]:
                    lista_traco[t] = lista_letras[t]
                    self.msg['text'] = lista_traco
                    if b not in digito:
                        digito.append(b)  # só adciona ao digito se não houver nele
            if b not in lista_letras:
                lista_erro.append(b)
                self.msg2['text'] = lista_erro
            self.caixa.set('')
            if len(digito) == len(lista_traco):
                self.msg3['text'] = 'Jogo Ganho! Parabéns!'
                self.msg3['fg'] = 'green'
            if len(lista_erro) == 10:
                self.msg3['text'] = '10 erros, você perdeu!', lista_letras
                self.msg3['fg'] = 'red'
                self.msg.destroy()
                self.nom.destroy()

            # Desenhar o bonequinho enforcado
            if len(lista_erro) == 1:
                circulo(75, 15, 125, 65, fill='orange', outline='black')
            if len(lista_erro) == 2:
                lin(100, 65, 100, 125)
            if len(lista_erro) == 3:
                lin(100, 70, 50, 75)
            if len(lista_erro) == 4:
                lin(100, 70, 150, 75)
            if len(lista_erro) == 5:
                lin(100, 125, 75, 175)
            if len(lista_erro) == 6:
                lin(100, 125, 125, 175)
            if len(lista_erro) == 7:
                circulo(85, 30, 95, 40, fill='green', outline='black')
            if len(lista_erro) == 8:
                circulo(105, 30, 115, 40, fill='green', outline='black')
            if len(lista_erro) == 9:
                circulo(98, 40, 102, 44, fill='white', outline='black')
            if len(lista_erro) == 10:
                boca(65, 50, 115, 60, fill='white')

        def sair(self):
            janela.destroy()

        def novo(self):
            pass

        def ocadastra(self):
            import Forca

    janela1 = Tk()
    arquivos(janela1)
    janela1.mainloop()

#escreve palavras
def palavra():

    def escreve():
        Ev = Ex.get()
        la1 ['text'] = Ev

    jd2 = Tk ()
    jd2.title ('Escrevendo')
    jd2.geometry('1500x1000')
    La3 = Label (jd2, text='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z', font='Helvetica 35 bold')
    La3.place (x=25, y=60)
    La = Label (jd2,text='com a ajuda de alguém use as letras e construa palavras', font='Helvetiva 20 bold')
    La.pack (side=TOP, fill= X)

    la1 = Label (jd2, text='', font='Helvetica 60 bold')
    la1.place (x=100, y=300)

    Ex = Entry (jd2, font='bold 50 bold', bg='white', width=8,
             justify='right', relief='sunken')
    Ex.place (x=300, y=200)
    bt= Button (jd2, text='escrever', command=escreve)
    bt.place (x=300,y=150)

    jd2.mainloop()


#aqui fica um bloco de anotações
def escreve_text():
    class PyNotePad:
        # Aqui fica a função inicial:
        def __init__(self):
            self.root = Tk()
            self.root.wm_title("PyNotePad")  # Aqui é o digito
            self.root["bg"] = "purple"

            # "inicia" a scroolbar
            scrollbar = Scrollbar(self.root)
            scrollbar.pack(side=RIGHT, fill=Y)

            menubar = Menu(self.root)
            menubar["bg"] = "purple"
            menubar["fg"] = "white"
            # Aqui criamos os menus:
            MENUarquivo = Menu(menubar)
            MENUarquivo["bg"] = "purple"
            MENUarquivo["fg"] = "white"
            MENUarquivo.add_command(label="Salvar", command=self.salvar)
            MENUarquivo.add_command(label="Abrir", command=self.abrir)
            menubar.add_cascade(label="Arquivo", menu=MENUarquivo)

            MENUajuda = Menu(menubar)
            MENUajuda["bg"] = "purple"
            MENUajuda["fg"] = "white"
            MENUajuda.add_command(label="Sobre", command=self.sobre)
            menubar.add_cascade(label="Ajuda", menu=MENUajuda)
            self.root.config(menu=menubar)

            # Aqui adicionamos a parte que fica o texto:
            self.text = Text(self.root)
            self.text["bg"] = 'DarkSlateGray'
            self.text["fg"] = "yellow"
            self.text["font"] = "arial 16"
            self.text.pack(expand=YES, fill=BOTH)

            # aqui configura o scrollbar
            self.text.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=self.text.yview)

            # Por Fim, a janela:
            self.root.mainloop()

        def salvar(self):  # Aqui é a função que salva o arquivo:

            fileName = asksaveasfilename()
            try:
                file = open(fileName, 'w')
                textoutput = self.text.get(0.0, END)
                file.write(textoutput)
            except:
                pass
            finally:
                file.close()

        def abrir(self):  # Aqui é a função que abre um arquivo

            fileName = askopenfilename()
            try:
                file = open(fileName, 'r')
                contents = file.read()

                self.text.delete(0.0, END)
                self.text.insert(0.0, contents)
            except:
                pass

        def sobre(self):  # uma pequena função "sobre" :D
            root = Tk()
            root.wm_title("Sobre")
            texto = ("PyNotePad: Versão 1.0")
            textONlabel = Label(root, text=texto)
            textONlabel.pack()

    # inicia o programa:
    PyNotePad()

#sobre o jogo
def sobre_o():
    sobre = Tk()
    sobre.title ("Sobre o Jogo")
    sobre.geometry("600x300")
    La = Label (sobre, text="""
             este jogo foi desenvolvido em sua grande parte por Arthur Carlos da Silva,
            O jogo da forca presente neste jogo não foi desenvolvido pelo mesmo.
             O jogo estava disponível em site de terceiros
             Porém o jogo teve alterações no código e ganhou outras opções diferentes
             do codigo original. 
             O alfa jogo tem foco educacional e foi desenvolvido com o intuito de auxiliar 
             no processo de alfabetização/alfabetização digital
             Tornando-se mais uma ferramenta de ensino para pais e professores. 
             Para saber mais e visualizar algumas experiencias já desenvolvidas 
             com o jogo acesse www.educadoresnolinux.top e siga na aba alfaJOGO""")
    La.pack()
    sobre.mainloop()

#adiciona palavra a forca
def adiciona_p():
    def escreve1():
        abrir=open("Nomes.txt", a)
        abrir.write("{}".formt(lae.get()))

        lar = Label(jey, text="Palavra adicionada")
        lar.place(x=10, y=10)


    jey= Tk ()
    jey.title("adicionar palavras")
    jey.geometry ("300x200")

    lau = Label(jey, text="Adione palavras ao jogo da Forca")
    lau.place (x=30, y=40)
    lae = Entry (jey)
    lae.place (x=30, y=80)
    lab = Button (jey, text="Adicionar", command=escreve1)
    lab.place(x=200, y=80)
    aviso = Label (jey, text="""Atenção,
     certifique-se de que as palavras 
     estão escritas corretamente.""")
    aviso.place (x=30, y=140)

    jey.mainloop()

#recados
def recados():
    rec = Tk()
    rec.title("deixe seu recado")

    def salva1():
        registo01 = open("recados.txt", "a")
        registo01.write("{} \n".format(reg.get(0.0, END)))


    btr = Button(rec, text="guardar", command=salva1)
    btr.pack(side=LEFT, fill=Y)
    low = Scrollbar(rec)
    low.pack(side=RIGHT, fill=Y)

    reg = Text(rec, font="Arial 14", bd=6, bg="DarkSlateGray", fg="white")
    reg.pack(expand=YES, fill=BOTH)
    reg.config(yscrollcommand=low.set)
    low.config(command=reg.yview)

    rec.mainloop()

#ler recados
def ler_recados():
    recl=Tk()
    recl.title("ler recados")


    leit = open("recados.txt", "r")
    book = leit.read()

    b = Button(recl, text="fechar", bg="red", command=exit)
    b.pack(fill=X)
    low = Scrollbar(recl)
    low.pack(side=RIGHT, fill=Y)

    z = Text(recl, font="arial 14", bd=6, bg="DarkSlateGray", fg="white")
    z.pack(expand=YES, fill=BOTH)
    z.insert(0.0, book)
    z.config(yscrollcommand=low.set)
    low.config(command=z.yview)

#janla principal
alfajogo = Tk()
alfajogo.title("AlfaJOGO 2.0")
alfajogo.geometry("420x370")
L = Label(alfajogo, text="Bem vindo ao AlfaJOGO 2.0", font="Arial 12", bg="DarkBlue", fg="white")
L.pack(side = TOP, fill=X)
photo = PhotoImage(file="no3.png")
image = Label(alfajogo, image=photo)
image.place(x=40, y=60)

menu = Menu(alfajogo)

alfajogo.config(menu=menu)
subMenu = Menu(menu)

menu.add_cascade(label="Opções", menu=subMenu)
subMenu.add_command(label="deixe seu recado", command=recados)
subMenu.add_command(label="Adicione palavras ao Jogo da Forca", command=adiciona_p)

xiMenu = Menu(menu)
xiMenu['fg'] = 'black'
xiMenu['bg'] = 'silver'
menu.add_cascade(label="visualizar", menu=xiMenu)
xiMenu.add_command(label="ler Recados", command=ler_recados)

exMenu = Menu (menu)
menu.add_cascade(label="extras", menu=exMenu)
exMenu.add_command(label="Sobre o jogo", command=sobre_o)

B1 = Button(alfajogo, text="Alfabeto", bg="red", fg="white", command=alfa)
B1.place(x=30, y=80)
B2 = Button(alfajogo, text="Jogo da forca", bg="black", fg="white", command=forca)
B2.place (x=260, y=80)
B3 = Button(alfajogo, text="Vogais", bg="blue", fg="white", command=vogal)
B3.place(x=20, y=160)
B3 = Button(alfajogo, text="Treine Palavras e frases", bg="yellow", command=palavra)
B3.place(x=80, y=35)
B3 = Button(alfajogo, text="Escreva textos", bg="pink", command=escreve_text)
B3.place(x=290, y=160)

alfajogo.mainloop()