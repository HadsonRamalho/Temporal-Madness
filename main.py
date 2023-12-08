import tkinter as tk
from tkinter import ttk

opcoes_frame = None  # Variável global para armazenar a janela de opções

def iniciar_jogo():
    print("Iniciando o jogo!")

def abrir_opcoes():
    global opcoes_frame

    # Desativa o botão de opções para evitar múltiplas instâncias da janela
    opcoes_button.config(state=tk.DISABLED)

    # Esconder o botão principal enquanto as opções estão abertas
    ocultar_elementos_principais()

    # Criar uma nova seção para as opções
    opcoes_frame = ttk.Frame(root, style="TFrame")
    opcoes_frame.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(opcoes_frame, text="Configurações do Jogo", font=("Helvetica", 16))
    label.pack(pady=10)

    voltar_button = ttk.Button(opcoes_frame, text="Voltar", command=voltar_ao_menu_principal, style="TButton")
    voltar_button.pack(pady=10)

def voltar_ao_menu_principal():
    global opcoes_frame

    # Destroi a seção de opções e reativa o botão de opções principal
    opcoes_frame.destroy()
    opcoes_button.config(state=tk.NORMAL)

    # Exibe os elementos principais novamente
    exibir_elementos_principais()

def ocultar_elementos_principais():
    iniciar_button.pack_forget()
    opcoes_button.pack_forget()
    sair_button.pack_forget()

def exibir_elementos_principais():
    iniciar_button.pack(pady=10)
    opcoes_button.pack(pady=10)
    sair_button.pack(pady=10)

def sair():
    print("Saindo do jogo")
    root.destroy()

# Configurando a janela principal
root = tk.Tk()
root.title("Abominações Temporais")

# Carregando uma imagem de fundo
background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Criando um estilo personalizado para os botões e frame
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10, background="#3d1818", foreground="#3d1818", borderwidth=0)
style.configure("TFrame", background="#3d1818", borderwidth=0)

# Criando um rótulo para o título com a nova cor de fundo
titulo_label = tk.Label(root, text="Temporal Madness", font=("Helvetica", 24), background="#3d1818", foreground="#ffffff")
titulo_label.pack(pady=20)

iniciar_button = ttk.Button(root, text="Iniciar Jogo", command=iniciar_jogo, style="TButton")
iniciar_button.pack(pady=10)

opcoes_button = ttk.Button(root, text="Opções", command=abrir_opcoes, style="TButton")
opcoes_button.pack(pady=10)

sair_button = ttk.Button(root, text="Sair", command=sair, style="TButton")
sair_button.pack(pady=10)

# Ajustando a posição dos botões
root.geometry("800x600")

# Iniciando o loop principal da aplicação
root.mainloop()
