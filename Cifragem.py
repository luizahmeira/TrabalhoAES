'''
O AES (Advanced Encryption Standard)
é um algoritmo de criptografia simétrica. Ele funciona em um processo de várias rodadas,
que incluem operações como SubBytes, ShiftRows, MixColumns e AddRoundKey
AQUI TA CHEIO DE PRINTS PRA AVALIAR OQ TA SENDO FEITO, DEPOIS TIRAMOS OS PRINTS OK? -luiza
'''

#sbox - nossa tabela de substituição
S_BOX = (
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
)

#sbox inversa - para decifragem
INV_S_BOX = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
)


#constantes de rodada
RCON = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1b, 0x36
)

#realização de multiplicação por x (0x02) em GF(2^8)
def xtempo(a):
    return ((a << 1) ^ 0x1b) & 0xff if a & 0x80 else (a << 1) & 0xff

def multiplicar_por_02(a):
    return xtempo(a)

def multiplicar_por_03(a):
    return multiplicar_por_02(a) ^ a

def multiplicar_por_09(a):
    return xtempo(xtempo(xtempo(a))) ^ a

def multiplicar_por_0b(a):
    return xtempo(xtempo(xtempo(a))) ^ xtempo(a) ^ a

def multiplicar_por_0d(a):
    return xtempo(xtempo(xtempo(a))) ^ xtempo(xtempo(a)) ^ a

def multiplicar_por_0e(a):
    return xtempo(xtempo(xtempo(a))) ^ xtempo(xtempo(a)) ^ xtempo(a)

'''expansão de chave'''

def key_expansion(chave_bytes):
    """vai gerar 11 chaves de rodada para o AES-128"""
    key_bytes = list(chave_bytes)
    W = [key_bytes[i*4 : (i+1)*4] for i in range(4)]

    for i in range(4, 44):
        temp = list(W[i-1])

        if i % 4 == 0:

            temp = temp[1:] + temp[:1] #rotword

            temp = [S_BOX[b] for b in temp] #subword

            rcon_value = RCON[i // 4] #rcon
            temp[0] = temp[0] ^ rcon_value

        W.append([W[i-4][j] ^ temp[j] for j in range(4)])

    round_keys = []
    for i in range(11):
        round_key = []
        for j in range(4):
            round_key.extend(W[i*4 + j])
        round_keys.append(round_key)

    return round_keys


'''arquivos e formatação'''

#le arquivos binarios
def ler_arquivo(caminho_arquivo_entrada):
    with open(caminho_arquivo_entrada, "rb") as f:
        dados_binarios = f.read()
    print(f"Dados binários lidos ({len(dados_binarios)} bytes)")
    return dados_binarios

#escreve os dados no arquivo de destino binario
def escrever_arquivo(caminho_arquivo_saida,dados):
    with open(caminho_arquivo_saida, "wb") as f:
        f.write(dados)
    print(f"Dados escritos em {caminho_arquivo_saida}.")

#aplica o PKCS#7 para os blocos de 16 bytes
def aplicar_padding_PKCS7(dados):
    tamanho_bloco = 16
    faltando = tamanho_bloco - (len(dados) % tamanho_bloco)
    if faltando == 0:
        faltando = tamanho_bloco
    padding = bytes([faltando] * faltando)
    dados_com_padding = dados + padding
    print(f"Padding feito, novo tamanho: {len(dados_com_padding)}")
    return dados_com_padding

#divide os dados em blocos de 16 bytes
def dividir_blocos(dados):
    tamanho_bloco = 16
    lista_blocos = []
    for i in range(0, len(dados), tamanho_bloco):
        bloco = dados[i:i + tamanho_bloco]
        lista_blocos.append(bloco)
    return lista_blocos

#cria matriz de estado 4x4 de um bloco de 16 bytes
def matriz_4x4(bloco):
    state = [[0] * 4 for _ in range(4)]
    for i in range(16):
        state[i % 4][i // 4] = bloco[i]
    #print("State gerado:" + state)
    return state

#remove o padding
def remover_padding_PKCS7(dados):
    tamanho_bloco = 16
    if not dados:
        raise ValueError("Dados vazios para remover padding")

    ultimo_byte = dados[-1]

    #validar o padding
    if ultimo_byte < 1 or ultimo_byte > tamanho_bloco or ultimo_byte > len(dados):
        raise ValueError("Padding inválido ou corrompido")

    #verifica se os bytes de padding correspondem ao valor do último byte
    if not all(b == ultimo_byte for b in dados[-ultimo_byte:]):
         raise ValueError("Padding inválido ou corrompido")

    return dados[:-ultimo_byte]

'''cifragem'''

#transformação de cifragem
def subBytes(state):
    for r in range(4):
        for c in range(4):
            state[r][c] = S_BOX[state[r][c]]
    return state

def shiftRows(state):
    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]
    return state

def mixColumns(state):
    novo_state = [[0] * 4 for _ in range(4)]
    for c in range(4):
        a0, a1, a2, a3 = state[0][c], state[1][c], state[2][c], state[3][c]
        novo_state[0][c] = multiplicar_por_02(a0) ^ multiplicar_por_03(a1) ^ a2 ^ a3
        novo_state[1][c] = a0 ^ multiplicar_por_02(a1) ^ multiplicar_por_03(a2) ^ a3
        novo_state[2][c] = a0 ^ a1 ^ multiplicar_por_02(a2) ^ multiplicar_por_03(a3)
        novo_state[3][c] = multiplicar_por_03(a0) ^ a1 ^ a2 ^ multiplicar_por_02(a3)
    return novo_state

def addRoundKey(state, round_key):
    for r in range(4):
        for c in range(4):
            state[r][c] = state[r][c] ^ round_key[r + 4*c]
    return state


def cifragem(caminho_arquivo_entrada, caminho_arquivo_saida, chave):
    print(f"\nIniciando a cifragem")

    #preparar a chave e gerar chaves de rodada
    try:
        chave_bytes = bytes([int(b) for b in chave.split(',')])
    except ValueError:
        print("A chave deve ser dada em bytes decimais separados por vírgula")
        return

    if len(chave_bytes) != 16:
        print(f"O AES-128 precisa de uma chave de 16 bytes, mas foram dados {len(chave_bytes)} bytes")
        return

    round_keys = key_expansion(chave_bytes)

    #leitura padding e divisão
    dados_binarios = ler_arquivo(caminho_arquivo_entrada)
    dados_com_padding = aplicar_padding_PKCS7(dados_binarios)
    lista_blocos = dividir_blocos(dados_com_padding)

    dados_cifrados = b""

    #loop de cifragem (modo ECB)
    for bloco in lista_blocos:
        state = matriz_4x4(bloco)

        state = addRoundKey(state, round_keys[0]) #rodada 0: AddRoundKey

        for i in range(1, 10): #rodadas 1 a 9 (Completas)
            state = subBytes(state)
            state = shiftRows(state)
            state = mixColumns(state)
            state = addRoundKey(state, round_keys[i])

        state = subBytes(state) #rodada 10 (Final)
        state = shiftRows(state)
        state = addRoundKey(state, round_keys[10])

        #converte state (4x4) de volta para bloco (16 bytes)
        bloco_cifrado = bytes([state[r][c] for c in range(4) for r in range(4)])
        dados_cifrados += bloco_cifrado

    #escritaa
    escrever_arquivo(caminho_arquivo_saida, dados_cifrados)
    print(f"Cifragem Concluída. Arquivo salvo em: {caminho_arquivo_saida}")


'''decifragem'''

#transformações de decifrage
def invSubBytes(state):
    for r in range(4):
        for c in range(4):
            state[r][c] = INV_S_BOX[state[r][c]]
    return state

def invShiftRows(state):
    state[1] = state[1][-1:] + state[1][:-1]
    state[2] = state[2][-2:] + state[2][:-2]
    state[3] = state[3][-3:] + state[3][:-3]
    return state

def invMixColumns(state):
    novo_state = [[0] * 4 for _ in range(4)]
    for c in range(4):
        a0, a1, a2, a3 = state[0][c], state[1][c], state[2][c], state[3][c]
        novo_state[0][c] = multiplicar_por_0e(a0) ^ multiplicar_por_0b(a1) ^ multiplicar_por_0d(a2) ^ multiplicar_por_09(a3)
        novo_state[1][c] = multiplicar_por_09(a0) ^ multiplicar_por_0e(a1) ^ multiplicar_por_0b(a2) ^ multiplicar_por_0d(a3)
        novo_state[2][c] = multiplicar_por_0d(a0) ^ multiplicar_por_09(a1) ^ multiplicar_por_0e(a2) ^ multiplicar_por_0b(a3)
        novo_state[3][c] = multiplicar_por_0b(a0) ^ multiplicar_por_0d(a1) ^ multiplicar_por_09(a2) ^ multiplicar_por_0e(a3)
    return novo_state


def decifragem(caminho_arquivo_entrada, caminho_arquivo_saida, chave):
    print(f"Iniciando a decifragem")

    #preparar a chave e gerar chaves de rodada
    try:
        chave_bytes = bytes([int(b) for b in chave.split(',')])
    except ValueError:
        print("A chave deve ser fornecida em bytes decimais separados por vírgula.")
        return

    if len(chave_bytes) != 16:
        print(f"O AES-128 aceita uma chave de 16 bytes, mas foram dados {len(chave_bytes)} bytes")
        return

    round_keys = key_expansion(chave_bytes)

    #leitura e divisão
    dados_binarios = ler_arquivo(caminho_arquivo_entrada)
    if len(dados_binarios) % 16 != 0:
        print("O arquivo cifrado parece estar corrompido")
        return

    lista_blocos_cifrados = dividir_blocos(dados_binarios)
    dados_decifrados = b""

    #loop d edecifragem modo cbc
    for bloco_cifrado in lista_blocos_cifrados:
        state = matriz_4x4(bloco_cifrado)

        #rodada final inversa, faz a última round key, depois invshiftrow e invsubbytes
        state = addRoundKey(state, round_keys[10])
        state = invShiftRows(state)
        state = invSubBytes(state)

        #addroundkey, ivmixcolumns, invshiftrow, invsubbytes)
        for i in range(9, 0, -1):
            state = addRoundKey(state, round_keys[i])
            state = invMixColumns(state)
            state = invShiftRows(state)
            state = invSubBytes(state)

        #addroundkey
        state = addRoundKey(state, round_keys[0])

        # converte state (4x4) de volta para bloco (16 bytes)
        bloco_decifrado = bytes([state[r][c] for c in range(4) for r in range(4)])
        dados_decifrados += bloco_decifrado

    #remoção de padding e escrita
    try:
        dados_sem_padding = remover_padding_PKCS7(dados_decifrados)
        escrever_arquivo(caminho_arquivo_saida, dados_sem_padding)
        print(f"Decifragem finalizada! Arquivo salvo em: {caminho_arquivo_saida}")
    except ValueError as e:
        print(f"Erro ao remover padding: {e}")

