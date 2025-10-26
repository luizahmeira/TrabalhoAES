from tkinter import filedialog

import customtkinter as ctk

def definindo_aparencia():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

def criando_janela_programa():
    app = ctk.CTk()
    app.title('Trabalho Final')
    app.geometry('800x400')
    return app

def seletor_arquivo(entrada_destino):
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo para cifrar ou decifrar",
        filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
    )
    if caminho:
        entrada_destino.delete(0, "end")
        entrada_destino.insert(0, caminho)

def botao_clicado():
    print("ainda falta fazer os metodos")

def chave_cifragem_decifragem(app):
    entrada_chave = ctk.CTkEntry(
        master=app,
        placeholder_text="Informe a chave de cifragem e decifragem aqui...",
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
        command=botao_clicado
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

definindo_aparencia()
app = criando_janela_programa()
escolher_arquivo(app)
chave_cifragem_decifragem(app)
cifrar_decifrar(app)
app.mainloop()
