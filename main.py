from cProfile import label
from cgi import test
from cgitb import text
from ctypes.wintypes import HDC
from logging import PlaceHolder
from tkinter.tix import COLUMN, Tree
from tkinter import ttk
from tkinter.ttk import*
from tkinter import*
from tkinter import messagebox
from turtle import left, width
from dados import*

from setuptools import Command

# cores -----------------------------
co0 = "#f0f3f5"  # Preta
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#feffff"  # branca
co3 = "#38576b"  # preta / black
co4 = "#403d3d"   # letra
co5 = "#6f9fbd"  # azul
co6 = "#ef5350"   # vermelha
co7 = "#93cd95"   # verde

#criando janela-------------------
janela = Tk ()
janela.title("")
janela.geometry('500x450')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style=Style(janela)
style.theme_use('clam')

#Frames

frame_cima = Frame(janela,width=500,height=50,bg=co3, relief='flat')
frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width=500,height=170,bg=co1, relief='flat')
frame_baixo.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

frame_tabela = Frame(janela,width=500,height=300,bg=co2, relief='flat')
frame_tabela.grid(row=2,column=0,columnspan=2,padx=10,pady=1, sticky=NW)

#configurando frame cima

l_nome=Label(frame_cima, text='Agenda Telefonica', anchor=NE, font=('times 20 bold'), bg=co3, fg=co1)
l_nome.place(x=130, y=5)

l_linha=Label(frame_cima, text='', width=500, anchor=NE, font=('arial 1'), bg=co2, fg=co1)
l_linha.place(x=0, y=45)

global tree
#configurando frame tabela


def mostrar_dados():

    global tree
    #creating a treeview with dual scrollbars
    dados_h=['Nome','Sexo', 'Telefone', 'Email' ]
        
    dados=ver_dados()

    tree=ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_h, show='headings')

    #Vertical Scrollbar
    vsb=ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview)

    #horizontal scrollbar
    hsb=ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    #tree cabeçalho
    tree.heading(0,text='Nome', anchor=NW)
    tree.heading(1,text='Sexo', anchor=NW)
    tree.heading(2,text='Telefone', anchor=NW)
    tree.heading(3,text='E-mail', anchor=NW)

    #tree corpo
    tree.column(0, width=120,anchor='nw')
    tree.column(1, width=50,anchor='nw')
    tree.column(2, width=100,anchor='nw')
    tree.column(0, width=120,anchor='nw')

    for item in dados:
        tree.insert('', 'end', value=item)

mostrar_dados()

################################função inserir

def inserir():
    nome = e_nome.get()
    sexo = c_sexo.get()
    telefone = e_tel.get()
    email = e_email.get()

    dados=[nome, sexo, telefone, email]

    if nome == '' or sexo == '' or telefone == '' or email == '':
        messagebox.showwarning('Dados', 'Por favor preencha todos os campos!!!')
    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados', 'Os dados foram adiciononados com sucesso!!!')

        e_nome.delete(0, 'end')
        c_sexo.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')

        mostrar_dados()

def atualizar():
    try:
        treev_dados=tree.focus()
        treev_dicionario=tree.item(treev_dados)
        tree_lista=treev_dicionario['values']

        nome = tree_lista[0]
        sexo = tree_lista[1]
        telefone =str (tree_lista[2])
        email = tree_lista[3]

        e_nome.insert(0,nome)
        c_sexo.insert(0,sexo)
        e_tel.insert(0,telefone)
        e_email.insert(0,email)


        def confirmar():
            nome = e_nome.get()
            sexo = c_sexo.get()
            telefone_novo = e_tel.get()
            email = e_email.get()

            dados=[telefone, nome, sexo, telefone_novo, email]

            print(dados)

            atualizar_dados(dados)

            messagebox.showinfo('Dados', 'Os dados foram atualizados com sucesso!!!')

            e_nome.delete(0, 'end')
            c_sexo.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_email.delete(0, 'end')

            b_confirmar.destroy()

            mostrar_dados()

        b_confirmar=Button(frame_baixo,command=confirmar, text='Confirmar',width=20, font=('Ivy 8 bold'), bg=co7, fg=co4, relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=300, y=50)
    except:
        messagebox.showwarning('Dados', 'Por favor selecione um contato para atualização!!!')

def remover():
    try:
        treev_dados=tree.focus()
        treev_dicionario=tree.item(treev_dados)
        tree_lista=treev_dicionario['values']

        telefone=str(tree_lista[2])

        remover_dados(telefone)

        messagebox.showinfo('Dados', 'O telefone foi deletado com sucesso!!!')

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        mostrar_dados()

    except:
        messagebox.showwarning('Dados', 'Por favor selecione um contato para Remover!!!')

def procurar():
    telefone = e_procurar.get()

    dados = pesquisar_dados(telefone)

    tree.delete(*tree.get_children())

    for item in dados:
        tree.insert('', 'end', values=item)
        
    e_procurar.delete(0, 'end')

##############################configurando frame baixo

l_nome=Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome=Entry(frame_baixo, width=25, justify='left', relief=FLAT, font=('',10), highlightthickness=1)
e_nome.place(x=65, y=20)

l_sexo=Label(frame_baixo, text='Sexo *', anchor=NW, relief=FLAT, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=10, y=50)
c_sexo=Combobox(frame_baixo, width=27)
c_sexo['value']=('F','M')
c_sexo.place(x=65, y=50)

l_tel=Label(frame_baixo, text='Contato*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_tel.place(x=10, y=80)
e_tel=Entry(frame_baixo, width=25, justify='left', relief=FLAT, font=('',10), highlightthickness=1)
e_tel.place(x=65, y=80)

l_email=Label(frame_baixo, text='Email *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=10, y=110)
e_email=Entry(frame_baixo, width=25, justify='left', relief=FLAT, font=('',10), highlightthickness=1)
e_email.place(x=65, y=110)

b_procurar=Button(frame_baixo,command=procurar, text='Procurar',width=20 ,font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_procurar.place(x=300, y=50)
e_procurar=Entry(frame_baixo, width=18, justify='left', relief=FLAT, font=('',11), highlightthickness=1)
e_procurar.place(x=300, y=20)

b_ver=Button(frame_baixo,command=mostrar_dados, text='Ver Dados',width=20 ,font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_ver.place(x=300, y=80)

b_adicionar=Button(frame_baixo,command=inserir, text='Adicionar',width=20, font=('Ivy 8 bold'), bg=co7, fg=co4, relief=RAISED, overrelief=RIDGE)
b_adicionar.place(x=85, y=140)

b_atualizar=Button(frame_baixo,command=atualizar, text='Atualizar',width=20, font=('Ivy 8 bold'), bg=co0, fg=co4, relief=RAISED, overrelief=RIDGE)
b_atualizar.place(x=300, y=110)

b_deletar=Button(frame_baixo,command=remover, text='Deletar',width=20, font=('Ivy 8 bold'), bg=co6, fg=co4, relief=RAISED, overrelief=RIDGE)
b_deletar.place(x=300, y=140)



janela.mainloop()
