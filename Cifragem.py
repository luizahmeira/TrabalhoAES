'''
O AES (Advanced Encryption Standard)
é um algoritmo de criptografia simétrica. Ele funciona em um processo de várias rodadas,
que incluem operações como SubBytes, ShiftRows, MixColumns e AddRoundKey
AQUI TA CHEIO DE PRINTS PRA AVALIAR OQ TA SENDO FEITO, DEPOIS TIRAMOS OS PRINTS OK? -luiza
'''

'''primeiro a gente precisa acessar o arquivo, e como o professor pediu ali nas questões vamos ler ele em binario'''
def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "rb") as f: #o rb significa read binary
        dados_binarios = f.read()
        print(dados_binarios)
    return dados_binarios

'''antes de fazer a cifragem precisamos fazer o padding dos dados, usando o AES que é aquela separação de blocos de 16 bytes'''
def aplicar_padding_PKCS7(dados):
    print(len(dados))
    tamanho_bloco = 16
    faltando = tamanho_bloco - (len(dados) % tamanho_bloco)
    if faltando == 0:
        faltando = tamanho_bloco
    padding = bytes([faltando] * faltando)
    dados_com_padding = dados + padding
    print(len(dados_com_padding))
    print(dados_com_padding)
    return dados_com_padding

'''Substitui cada byte por outro usando uma tabela não linear'''
def subBytes():
    return 0

'''Desloca cada linha do state para a esquerda'''
def shiftRows():
    return 0

'''Mistura os bytes de cada coluna usando operações em GF(2⁸)'''
def mixColumns():
    return 0

'''Faz XOR do estado com parte da chave expandida'''
def addRoundKey():
    return 0

def cifragem(caminho_arquivo):
    dados_binarios = ler_arquivo(caminho_arquivo)
    aplicar_padding_PKCS7(dados_binarios)

