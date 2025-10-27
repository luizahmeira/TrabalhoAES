from tkinter import filedialog
from openpyxl.descriptors import NoneSet
import Cifragem as cfm
import customtkinter as ctk

caminho_arquivo = None

def definindo_aparencia():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

def criando_janela_programa():
    app = ctk.CTk()
    app.title('Trabalho Final')
    app.geometry('800x400')
    return app

def seletor_arquivo(entrada_destino):
    global caminho_arquivo_entrada
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo para cifrar ou decifrar",
        filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
    )
    if caminho:
        entrada_destino.delete(0, "end")
        entrada_destino.insert(0, caminho)

    caminho_arquivo_entrada = caminho

def botao_clicado():
    print("ainda falta fazer os metodos")

def efetuar_cifragem():
    caminho_arquivo_saida = entrada_destino.get()
    if not caminho_arquivo_saida:
        print("Não foi informado um caminho de destino")
        return
    cfm.cifragem(caminho_arquivo_entrada,caminho_arquivo_saida)

def chave_cifragem_decifragem(app):
    entrada_chave = ctk.CTkEntry(
        master=app,
        placeholder_text="Informe a chave de cifragem ou decifragem aqui...",
        width=400,
        height=40
    )
    entrada_chave.pack(pady=(50, 30))

def cifrar_decifrar(app):
    frame_botoes = ctk.CTkFrame(master=app, fg_color="transparent")
    frame_botoes.pack(pady=10)

    cifragem = ctk.CTkButton(
        master=frame_botoes,
        text="Cifragem",
        fg_color="white",
        hover_color="grey",
        text_color="black",
        width=150,
        command=lambda: efetuar_cifragem()
    )
    cifragem.pack(side="left",pady=20)

    decifrar = ctk.CTkButton(
        master=frame_botoes,
        text="Decifragem",
        fg_color="white",
        hover_color="grey",
        text_color="black",
        width=150,
        command = botao_clicado
    )
    decifrar.pack(side="left",pady=20)

def escolher_arquivo(app):
    entrada_destino = ctk.CTkEntry(
        master=app,
        placeholder_text="Nome do arquivo de destino (sem extensão)...",
        width=400,
        height=40
    )

    btn_arquivo = ctk.CTkButton(
        master=app,
        text="Escolher arquivo",
        fg_color="white",
        hover_color="grey",
        text_color="black",
        width=150,
        command=lambda: seletor_arquivo(entrada_destino)
    )
    btn_arquivo.pack(pady=20)
    entrada_destino.pack(pady=(30, 10))

    return entrada_destino

definindo_aparencia()
app = criando_janela_programa()
entrada_destino = escolher_arquivo(app)
chave_cifragem_decifragem(app)
cifrar_decifrar(app)
app.mainloop()
