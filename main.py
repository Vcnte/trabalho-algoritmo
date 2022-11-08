abrirdoc = input("Digite aqui o nome do arquivo: ")
try:
    localizardoc = open(abrirdoc)
except FileNotFoundError:
    print("Arquivo não encontrado")
    exit()
data = localizardoc.read().split()

dicionario = {}
for palavra in data:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

if localizardoc == None:
    print("Não foi possível localizar/abrir o documento.")

else:
    print("1 - Consultar a quantidade de ocorrencias de uma determinada palavra\n"
          "2 - Listar todas as palavras que constam no arquivo, bem como a quantidade de vezes que elas ocorrem, em ordem crescente de ocorrencia\n"
          "3 - Listar todas as palavras que constam no arquivo, bem como a quantidade de vezes que elas ocorrem, em ordem decrescente de ocorrencia\n"
          "4 - Listar todas as palavras que constam no arquivo, bem como a quantidade de vezes que elas ocorrem, em ordem alfabetica\n"
          "5 - Listar todas as palavras que constam no arquivo e que iniciam por um caractere informado pelo usuario, bem como a quantidade de vezes que essas palavras ocorrem, em ordem crescente de ocorrencia\n"
          "6 - Encerrar o programa")
    while True:
        opcaomenu = input("Digite a opção desejada: ")
        if opcaomenu == "1":
            palavraencontrada = input("Digite aqui a palavra a ser encontrada: ")
            if palavraencontrada in data:
                print(dicionario[palavraencontrada])
            else:
                print("Palavra não encontrada, tente novamente.")

        elif opcaomenu == "2":
            dicionario_ordenado = sorted(dicionario.items(), key=lambda x: x[1], reverse=False)

            print(dicionario_ordenado)
        elif opcaomenu == "3":
            dicionario_ordenado = sorted(dicionario.items(), key=lambda x: x[1], reverse=True)

            print(dicionario_ordenado)
        elif opcaomenu == "4":
            dicionario_ordenado = sorted(dicionario.keys())
            print(dicionario_ordenado)
        elif opcaomenu == "5":
            caractere = input("Digite aqui o caractere desejado: ")
            dicionario = {}
            for palavra in data:
                if caractere == palavra[0]:
                    if palavra in dicionario:
                        dicionario[palavra] += 1
                    else:
                        dicionario[palavra] = 1
            dicionario_ordenado = sorted(dicionario.items(), key=lambda x: x[1], reverse=False)
            print(dicionario_ordenado)

        elif opcaomenu == "6":
            print("Finalizando o programa")
            raise SystemExit
        else:
            print("ERRO: Digite uma opção válida.")
