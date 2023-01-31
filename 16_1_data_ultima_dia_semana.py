import tkinter as tk
from tkinter import messagebox
from datetime import date
from datetime import timedelta

#Cria uma instância
janela = tk.Tk()

#Adiciona um título
janela.title("bem vindo ao Tkinter")
janela.geometry('700x300') #largura x altura

#Adiciona um label
label = tk.Label(janela, text="Teste de botão", font=("Arial Bold",18))
label.grid(column=0,row=0)

#Criar botão
#botao = tk.Button(janela, text='Sair', height=1, width=15, command=janela.destroy)
#botao.grid(column=0, row=100)
#botao.pack()


def mostrar():
    diasemana=['segunda','terça','quarta','quinta','sexta','sábado','domingo']
    for i,x in enumerate(diasemana):
       
        if x == str_nome.get():
            indice = i
            hoje=date.today()
            diferenca=(hoje.weekday()-indice)%7
            ultimo_dia_semana=hoje-timedelta(days=diferenca)
            #n = str_nome.get()
            tk.messagebox.showinfo('Mensagem',f'Última data de {str_nome.get()}:{ultimo_dia_semana}')


str_nome = tk.Label(janela, text="Último data de ").place(x=30,y=50)

str_nome = tk.StringVar()

Entrada = tk.Entry(janela, textvariable = str_nome).place(x=120, y=50)
botao_enviar = tk.Button(janela, text="Enviar", command=mostrar).place(x=120,y=170)
botao_sair = tk.Button(janela, text='Sair', command=janela.destroy).place(x=200, y=170)


#inicia GUI
janela.mainloop()





