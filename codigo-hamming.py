codigo_original = input("Digite o código de bits: ")

lista_de_digitos = [int(digito) for digito in codigo_original]

k = 1

print(f'codigo recebido {lista_de_digitos}')

while (2**k) < (k+len(lista_de_digitos)+1):
    k += 1

print(f'Serão precisos {k} bits de verificação')

if(len(lista_de_digitos) == 4 or len(lista_de_digitos) == 5):
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


print(f"Aqui está o código corrigido: {lista_de_digitos}")