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
def remover_padding_PKCS7(dados):
    tamanho_bloco = 16
    ultimo_byte = dados[-1]
    if ultimo_byte < 1 or ultimo_byte > tamanho_bloco:
        raise ValueError("padding invalido")
    return dados[:-ultimo_byte]

def decifragem(caminho_arquivo_entrada,caminho_arquivo_saida):
    dados_binarios = ler_arquivo(caminho_arquivo_entrada)
    remover_padding_PKCS7(dados_binarios)

