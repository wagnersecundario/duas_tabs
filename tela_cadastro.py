from carro import Carro
from trem import Trem
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#função de criação de objetos

lista=[]

def cadastroVeiculo():
    marca=entryMarca.get()
    modelo=entryModelo.get()
    ano=entryAno.get()
    tipo=varTipo.get()
    portas=entryNPortas.get()
    print(modelo)
    erro=0
    
    if tipo=='Carro' or tipo=='Trem':
        if portas=='':
            messagebox.showinfo('Erro', 'Todos os itens devem ser preenchidos!')
            erro=1
        if erro==0:
            c=Carro(marca, modelo, ano, portas)
            salvar(c)
            messagebox.showinfo('Cadastro', f'{tipo} cadastrado com sucesso!')
    else: 
        t=Trem(marca, modelo, ano, portas)
        salvar(t)
    lista.append(t)

def salvar(obj):
    lista.append(obj)

def atualizaListbox():
    listbox.delete(0, tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())

janela = tk.Tk()
janela.title('Cadastro de Veículos')
janela.geometry('400x200')

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky='nsew')

tab1 = ttk.Frame(janelinha)
for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1, text='Cadastro')
janelinha.add(tab2, text='Lista')

label1=tk.Label(tab1, text='Marca:', font=('',10))
label1.grid(row=0, column=0, sticky='w', padx=10)
entryMarca=tk.Entry(tab1, font=('', 10))
entryMarca.grid(row=0,column=1, sticky='nsew', padx=10, pady=2)

label2=tk.Label(tab1, text='Modelo:', font=('',10))
label2.grid(row=1, column=0, sticky='w', padx=10)
entryModelo=tk.Entry(tab1, font=('', 10))
entryModelo.grid(row=1,column=1, sticky='nsew', padx=10, pady=2)

label3=tk.Label(tab1, text='Ano:', font=('',10))
label3.grid(row=2, column=0, sticky='w', padx=10)
entryAno=tk.Entry(tab1, font=('', 10))
entryAno.grid(row=2,column=1, sticky='nsew', padx=10, pady=2)

label4=tk.Label(tab1, text='Portas/Vagões:', font=('',10))
label4.grid(row=3, column=0, sticky='w', padx=10)
entryNPortas=tk.Entry(tab1, font=('', 10))
entryNPortas.grid(row=3,column=1, sticky='nsew', padx=10, pady=2)

tk.Label(tab1, text='Tipo', font=('', 10)).grid(row=4, column=0, sticky='w', padx=10)
varTipo = tk.StringVar(value='Carro')
tk.Radiobutton(tab1, text='Carro', font=('', 10), variable=varTipo, value='Carro').grid(row=4, column=1, sticky='w', padx=10)
tk.Radiobutton(tab1, text='Trem', font=('', 10), variable=varTipo, value='Trem').grid(row=4, column=1, sticky='e', padx=10)

tk.Button(tab1, text='Cadastrar', font=('', 10), command=cadastroVeiculo).grid(row=5,columnspan=2)

listbox=tk.Listbox(tab2)
listbox.config(font=('', 10))
listbox.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
tk.Button(tab2, text='Atualizar', font=('', 10), command=atualizaListbox).grid(row=1, column=0)

janela.mainloop() 