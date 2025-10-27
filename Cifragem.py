'''
O AES (Advanced Encryption Standard)
é um algoritmo de criptografia simétrica. Ele funciona em um processo de várias rodadas,
que incluem operações como SubBytes, ShiftRows, MixColumns e AddRoundKey
AQUI TA CHEIO DE PRINTS PRA AVALIAR OQ TA SENDO FEITO, DEPOIS TIRAMOS OS PRINTS OK? -luiza
'''

'''primeiro a gente precisa acessar o arquivo, e como o professor pediu ali nas questões vamos ler ele em binario'''
def ler_arquivo(caminho_arquivo_entrada):
    with open(caminho_arquivo_entrada, "rb") as f: #o rb significa read binary
        dados_binarios = f.read()
        print(dados_binarios)
    return dados_binarios

'''já colocando o metodo q vai escrever nossos dados cifrados no arquivo de destino'''
def escrever_arquivo(caminho_arquivo_saida,dados_cifrados):
    with open(caminho_arquivo_saida, "wb") as f:
        f.write(dados_cifrados)

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

'''agora precisamos dividir os dados em blocos de 16 bytes após fazer o padding para ent fazer a matriz 4x4'''
def dividir_blocos(dados):
    tamanho_bloco = 16
    lista_blocos = []
    for i in range(0, len(dados), tamanho_bloco):
        bloco = dados[i:i + tamanho_bloco]
        lista_blocos.append(bloco)
    return lista_blocos

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

def cifragem(caminho_arquivo_entrada,caminho_arquivo_saida,chave):
    print(f"caminho de entrada: {caminho_arquivo_entrada}")
    print(f"caminho de saída: {caminho_arquivo_saida}")
    dados_binarios = ler_arquivo(caminho_arquivo_entrada)
    dados_com_padding = aplicar_padding_PKCS7(dados_binarios)
    lista_blocos = dividir_blocos(dados_com_padding)
    print(lista_blocos)

