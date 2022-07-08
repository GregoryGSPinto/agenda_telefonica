#importando csv
from asyncore import write
import csv
from re import I

#funcao adicionar
def adicionar_dados(i):
    #acessando csv
    with open('dados.csv', 'a+', newline='') as file:
        escrever=csv.writer(file)
        escrever.writerow(i)

##################
##################
####              função ver dados
def ver_dados():
    dados=[]        
    #acessando csv
    with open('dados.csv') as file:
        ler_csv=csv.reader(file)
        for linha in ler_csv:
            dados.append(linha)
    return dados

##################
##################
####                 função remover dados

def remover_dados(i):
    def adicionar_novalista(j):
        #acessando csv
        with open('dados.csv', 'w', newline='') as file:
            escrever=csv.writer(file)
            escrever.writerows(j)
        ver_dados()

    nova_lista=[]
    telefone=i
    with open('dados.csv', 'r') as file:
        ler_csv=csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nova_lista.remove(linha)

    #adicionando nova lista
    adicionar_novalista(nova_lista)

##################
##################
####                  função atualizar dados

def atualizar_dados(i):
    def adicionar_novalista(j):
        #acessando csv
        with open('dados.csv', 'w', newline='') as file:
            escrever=csv.writer(file)
            escrever.writerows(j)
            ver_dados()

    nova_lista=[]
    telefone=i[0]
    with open('dados.csv', 'r') as file:
        ler_csv=csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nome=i[1]
                    sexo=i[2]
                    telefone=i[3]
                    email=i[4]

                    dados=[nome, sexo, telefone, email]

                    #trocando lista por index
                    index=nova_lista.index(linha)
                    nova_lista[index]=dados

        #adicionando nova lista

    adicionar_novalista(nova_lista)

##################
##################
####função pesquisar dados

def pesquisar_dados(i):
    dados=[]        
    telefone=i

        #acessando csv

    with open('dados.csv') as file:
        ler_csv=csv.reader(file)
        for linha in ler_csv:
            for campo in linha:
                if campo == telefone:
                    dados.append(linha)
    return dados


