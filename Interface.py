from tkinter import filedialog
import Cifragem as cfm
import customtkinter as ctk

caminho_arquivo_entrada = None
entrada_destino = None
entrada_chave = None

def definindo_aparencia():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")


def criando_janela_programa():
    app = ctk.CTk()
    app.title('Trabalho Final - AES')
    app.geometry('800x450')  #aumentei um pouco para melhor visualização
    return app


def seletor_arquivo(entrada_destino_widget):
    global caminho_arquivo_entrada
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo para cifrar ou decifrar",
        filetypes=[("Todos os arquivos", "*.*")]
    )
    if caminho:
        entrada_destino_widget.delete(0, "end")
        entrada_destino_widget.insert(0, caminho)
        caminho_arquivo_entrada = caminho


def efetuar_cifragem():
    global caminho_arquivo_entrada, entrada_destino, entrada_chave

    caminho_arquivo_saida = entrada_destino.get().strip()
    chave = entrada_chave.get().strip()

    if not caminho_arquivo_entrada or not caminho_arquivo_saida or not chave:
        print("Selecione um arquivo, informe um nome de destino e a chave.")
        return

    #adicionando a extensao se n tiver
    if "." not in caminho_arquivo_saida:
        caminho_arquivo_saida += ".enc"

    cfm.cifragem(caminho_arquivo_entrada, caminho_arquivo_saida, chave)


def efetuar_decifragem():
    global caminho_arquivo_entrada, entrada_destino, entrada_chave

    caminho_arquivo_saida = entrada_destino.get().strip()
    chave = entrada_chave.get().strip()

    if not caminho_arquivo_entrada or not caminho_arquivo_saida or not chave:
        print("Selecione um arquivo, informe um nome de destino e a chave.")
        return

    #adicionando a extensao se n tiver
    if "." not in caminho_arquivo_saida:
        caminho_arquivo_saida += ".dec"

    cfm.decifragem(caminho_arquivo_entrada, caminho_arquivo_saida, chave)


def chave_cifragem_decifragem(app):
    entrada_chave_widget = ctk.CTkEntry(
        master=app,
        placeholder_text="Informe a chave de 16 bytes",
        width=500,
        height=40
    )
    entrada_chave_widget.pack(pady=(50, 30))
    return entrada_chave_widget


def cifrar_decifrar(app):
    frame_botoes = ctk.CTkFrame(master=app, fg_color="transparent")
    frame_botoes.pack(pady=10)

    cifragem_btn = ctk.CTkButton(
        master=frame_botoes,
        text="Cifragem (AES)",
        fg_color="white",
        hover_color="grey",
        text_color="black",
        width=150,
        command=lambda: efetuar_cifragem()
    )
    cifragem_btn.pack(side="left", pady=20, padx=15)

    decifrar_btn = ctk.CTkButton(
        master=frame_botoes,
        text="Decifragem (AES)",
        fg_color="white",
        hover_color="grey",
        text_color="black",
        width=150,
        command=lambda: efetuar_decifragem()
    )
    decifrar_btn.pack(side="left", pady=20, padx=15)


def escolher_arquivo(app):
    #campo pro caminho do arquivo de destino
    entrada_destino_widget = ctk.CTkEntry(
        master=app,
        placeholder_text="Caminho/Nome do arquivo de destino",
        width=500,
        height=40
    )
    entrada_destino_widget.pack(pady=(30, 10))

    #btn_arquivo - serve para selecionar arquivo de entrada
    btn_arquivo = ctk.CTkButton(
        master=app,
        text="Escolher arquivo de entrada",
        fg_color="white",
        hover_color="grey",
        text_color="black",
        width=300,
        command=lambda: seletor_arquivo(entrada_destino_widget)
    )
    btn_arquivo.pack(pady=20)

    return entrada_destino_widget


#bloco principal de execução
definindo_aparencia()
app = criando_janela_programa()
entrada_destino = escolher_arquivo(app)
entrada_chave = chave_cifragem_decifragem(app)
cifrar_decifrar(app)
app.mainloop()
