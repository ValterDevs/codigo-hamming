codigo_original = input("Digite o código de bits: ")

lista_de_digitos = [int(digito) for digito in codigo_original]

k = 1

print(f'codigo recebido {lista_de_digitos}')

while (2**k) < (k+len(lista_de_digitos)+1):
    k += 1
    



print(f'Serão precisos {k} bits de verificação')

if(len(lista_de_digitos) == 4):
    if( ((lista_de_digitos[0] + lista_de_digitos[1] + lista_de_digitos[3])%2) != 0):
        lista_de_digitos.insert(0, 1)
    else:
        lista_de_digitos.insert(0, 0)

    if( ((lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4])%2) != 0):
        lista_de_digitos.insert(1, 1)
    else:
        lista_de_digitos.insert(1, 0)

    if( ((lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[5])%2) != 0):
        lista_de_digitos.insert(3, 1)
    else:
        lista_de_digitos.insert(3, 0)
elif(len(lista_de_digitos) == 5):
    if( ((lista_de_digitos[0] + lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4])%2) != 0):
        lista_de_digitos.insert(0, 1)
    else:
        lista_de_digitos.insert(0, 0)

    if( ((lista_de_digitos[1] + lista_de_digitos[4] + lista_de_digitos[5])%2) != 0):
        lista_de_digitos.insert(1, 1)
    else:
        lista_de_digitos.insert(1, 0)

    if( ((lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[5])%2) != 0):
        lista_de_digitos.insert(3, 1)
    else:
        lista_de_digitos.insert(3, 0)

    if( ((lista_de_digitos[7])%2) != 0):
        lista_de_digitos.insert(7, 1)
    else:
        lista_de_digitos.insert(7, 0)

elif(len(lista_de_digitos) == 6):
    if( ((lista_de_digitos[0] + lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4])%2) != 0):
        lista_de_digitos.insert(0, 1)
    else:
        lista_de_digitos.insert(0, 0)

    if( ((lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[-1])%2) != 0):
        lista_de_digitos.insert(1, 1)
    else:
        lista_de_digitos.insert(1, 0)



    if( ((lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[5])%2) != 0):
        lista_de_digitos.insert(3, 1)
    else:
        lista_de_digitos.insert(3, 0)


    if( ((lista_de_digitos[7] + lista_de_digitos[8])%2) != 0):
        lista_de_digitos.insert(7, 1)
    else:
        lista_de_digitos.insert(7, 0)



elif(len(lista_de_digitos) == 7):
    if( ((lista_de_digitos[0] + lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[-1])%2) != 0):
        lista_de_digitos.insert(0, 1)
    else:
        lista_de_digitos.insert(0, 0)
    if( ((lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[-2] + lista_de_digitos[-1])%2) != 0):
        lista_de_digitos.insert(1, 1)
    else:
        lista_de_digitos.insert(1, 0)

    if( ((lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[5])%2) != 0):
        lista_de_digitos.insert(3, 1)
    else:
        lista_de_digitos.insert(3, 0)

    if( ((lista_de_digitos[-3] + lista_de_digitos[-2] + lista_de_digitos[-1])%2) != 0):
        lista_de_digitos.insert(7, 1)
    else:
        lista_de_digitos.insert(7, 0)


###CORREÇÃO DO CÓDIGO

print(f'Esse é o codigo de hamming {lista_de_digitos}')

codigo_recebido = input("Digite o código de bits que você recebeu para corrigir: ")

lista_bits_recebida = [int(digito) for digito in codigo_recebido]

posicao = 0

if(len(lista_de_digitos) == 7):
    if( ((lista_bits_recebida[0] + lista_bits_recebida[2] + lista_bits_recebida[4] + lista_bits_recebida[6] + lista_bits_recebida[8])%2) != 0):
        posicao += 1

    if( ((lista_bits_recebida[1] + lista_bits_recebida[2] + lista_bits_recebida[5] + lista_bits_recebida[6])%2) != 0):
        posicao += 2

    if( ((lista_bits_recebida[3] + lista_bits_recebida[4] + lista_bits_recebida[5]+ lista_bits_recebida[6])%2) != 0):
        posicao += 4
if(len(lista_de_digitos) == 9):
    if( ((lista_bits_recebida[0] + lista_bits_recebida[2] + lista_bits_recebida[4] + lista_bits_recebida[6] + lista_bits_recebida[8])%2) != 0):
        posicao += 1

    if( ((lista_bits_recebida[1] + lista_bits_recebida[2] + lista_bits_recebida[5] + lista_bits_recebida[6])%2) != 0):
        posicao += 2

    if( ((lista_bits_recebida[3] + lista_bits_recebida[4] + lista_bits_recebida[5]+ lista_bits_recebida[6])%2) != 0):
        posicao += 4
    if( ((lista_bits_recebida[7] + lista_bits_recebida[8])%2) != 0):
        posicao += 8
if(len(lista_de_digitos) == 10):
    if( ((lista_bits_recebida[0] + lista_bits_recebida[2] + lista_bits_recebida[4] + lista_bits_recebida[6] + lista_bits_recebida[8])%2) != 0):
        posicao += 1

    if( ((lista_bits_recebida[1] + lista_bits_recebida[2] + lista_bits_recebida[5] + lista_bits_recebida[6] + lista_bits_recebida[9])%2) != 0):
        posicao += 2

    if( ((lista_bits_recebida[3] + lista_bits_recebida[4] + lista_bits_recebida[5]+ lista_bits_recebida[6])%2) != 0):
        posicao += 4
    if( ((lista_bits_recebida[7] + lista_bits_recebida[8] + lista_bits_recebida[9])%2) != 0):
        posicao += 8


if(lista_bits_recebida[posicao-1] == 1):
    lista_bits_recebida[posicao-1] = 0
else:
    lista_bits_recebida[posicao-1] = 1


print(f'Esse é o codigo recebido corrigido: {lista_bits_recebida}')