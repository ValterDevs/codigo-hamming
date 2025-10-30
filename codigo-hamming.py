codigo_original = input("Digite o código de bits: ")

lista_de_digitos = [int(digito) for digito in codigo_original]

k = 1

print(f'codigo recebido {lista_de_digitos}')

while (2**k) < (k+len(lista_de_digitos)+1):
    k += 1
    
bits_paridade_original = []

bits_paridade_recebida = []


print(f'Serão precisos {k} bits de verificação')

if(len(lista_de_digitos) == 4 or len(lista_de_digitos) == 5):
    if( ((lista_de_digitos[0] + lista_de_digitos[1] + lista_de_digitos[3])%2) != 0):
        lista_de_digitos.insert(0, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(0, 0)
        bits_paridade_original.append(0)

    if( ((lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4])%2) != 0):
        lista_de_digitos.insert(1, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(1, 0)
        bits_paridade_original.append(0)

    if( ((lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[5])%2) != 0):
        lista_de_digitos.insert(3, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(3, 0)
        bits_paridade_original.append(0)


elif(len(lista_de_digitos) == 6):
    if( ((lista_de_digitos[0] + lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4])%2) != 0):
        lista_de_digitos.insert(0, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(0, 0)
        bits_paridade_original.append(0)

    if( ((lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[-1])%2) != 0):
        lista_de_digitos.insert(1, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(1, 0)
        bits_paridade_original.append(0) 


    if( ((lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[5])%2) != 0):
        lista_de_digitos.insert(3, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(3, 0)
        bits_paridade_original.append(0)


    if( ((lista_de_digitos[7] + lista_de_digitos[8])%2) != 0):
        lista_de_digitos.insert(7, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(7, 0)
        bits_paridade_original.append(0)


elif(len(lista_de_digitos) == 7):
    if( ((lista_de_digitos[0] + lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[-1])%2) != 0):
        lista_de_digitos.insert(0, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(0, 0)
        bits_paridade_original.append(0)

    if( ((lista_de_digitos[1] + lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[-2] + lista_de_digitos[-1])%2) != 0):
        lista_de_digitos.insert(1, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(1, 0)
        bits_paridade_original.append(0)

    if( ((lista_de_digitos[3] + lista_de_digitos[4] + lista_de_digitos[5])%2) != 0):
        lista_de_digitos.insert(3, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(3, 0)
        bits_paridade_original.append(0)

    if( ((lista_de_digitos[-3] + lista_de_digitos[-2] + lista_de_digitos[-1])%2) != 0):
        lista_de_digitos.insert(7, 1)
        bits_paridade_original.append(1)
    else:
        lista_de_digitos.insert(7, 0)
        bits_paridade_original.append(0)


###CORREÇÃO DO CÓDIGO

print(f'Esse é o codigo de hamming {lista_de_digitos}')

codigo_recebido = input("Digite o código de bits que você recebeu para corrigir: ")

lista_bits_recebida = [int(digito) for digito in codigo_recebido]


if(k == 3):
    bits_paridade_recebida.append(lista_de_digitos[0])
    bits_paridade_recebida.append(lista_bits_recebida[1])
    bits_paridade_recebida.append(lista_bits_recebida[3])

if(k == 4): 
    bits_paridade_recebida.append(lista_bits_recebida[0])
    bits_paridade_recebida.append(lista_bits_recebida[1])
    bits_paridade_recebida.append(lista_bits_recebida[3])
    bits_paridade_recebida.append(lista_bits_recebida[7])
    
posicao_bit_errado = 0
    
for i in range(len(bits_paridade_original)):
    if(bits_paridade_original[i] == bits_paridade_original[i]):
        posicao_bit_errado += 0 * (2**i)
    else:
        posicao_bit_errado += 1 * (2**i)
        

print(bits_paridade_original)
print(bits_paridade_recebida)

print(f'A posição do bit errado é {posicao_bit_errado}')

if(codigo_recebido[posicao_bit_errado] == 1):
    codigo_recebido[posicao_bit_errado] = 0
elif(codigo_recebido[posicao_bit_errado] == 0):
    codigo_recebido[posicao_bit_errado] = 1

print(f'Esse é o codigo recebido corrigido: {codigo_recebido}')
