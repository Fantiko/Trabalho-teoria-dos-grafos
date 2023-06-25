def ler_matriz(numero_pessoas, arquivo):
    matriz = []
    for pessoas in range(numero_pessoas):
        linha = arquivo.readline().rstrip("\n")
        lista = list(linha)
        lista = [1 if valor == "V" else 0 for valor in lista]
        matriz.append(lista)
    return matriz


def aviso():
    return "os cKaio estavam bebados"


def contagem(matriz, numero_pessoas):
    familia = 0
    familias = []
    aux = [0] * numero_pessoas
    pulou = 0
    for i in range(numero_pessoas):
        if not matriz[i][i]:  # confere se ele é parente dele mesmo
            escreveoutput(aviso())
            exit()

        for pessoa in range(numero_pessoas):  # para cada pessoa na linha atual
            if matriz[i][pessoa] == 0:  # se nao tem parentesco
                continue

            if aux[pessoa] != 0:  # ja passei naquela linha?
                pulou = 1
                continue  # ja

            if matriz[i] == matriz[pessoa]:  # a linha que eu to é igual a linha que tenho parentesco?
                if aux[pessoa] == 0:
                    familia += 1
                aux[pessoa] += 1
                #  print(pessoa)
                pulou = 0

            else:
                escreveoutput(aviso())
                exit()

        if pulou == 0:
            familias.append(familia)
            familia = 0
        #  print(aux)

    return len(familias), familias


def escreveoutput(quantidade, tamanhos=[]):
    with open("output.txt", "w") as f:
        f.write(quantidade.__str__() + "\n")
        for elemento in tamanhos:
            f.write(str(elemento) + " ")


def main():
    with open("input.txt", 'r') as arquivo:
        numero_pessoas = int(arquivo.readline())
        #  print(numero_pessoas)
        quantidade, tamanhos = contagem(ler_matriz(numero_pessoas, arquivo), numero_pessoas)
        escreveoutput(quantidade, tamanhos)


if __name__ == "__main__":
    main()
