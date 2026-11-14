import hashlib
from datetime import datetime
import os
import json
import time
from pathlib import Path

os.system("clear")

logo="""
  _______ _ _        _____
 |  _____(_) |      |_   _|
 | |__   _| | ___     | |
 |  __| | | |/ _ \    | |
 | |    | | |  __/    | |
 |_|    |_|_|\___|    |_|

 [ INTEGRITY MONITOR ]
 [ SHA-256 PROTECTION ]
"""

print(logo)


def archiveAdd():
    now = datetime.now()

    arquivos_json=[]
    print("What a name of past?:")
    #AQUI ELE VAI PEGAR O NOME DA PASTA
    pastas = input("> ")

    #MANDA O PATH PEGAR A PASTA
    pasta = Path(pastas)
    #AQUI VAMOSTRAR TODOS OS ARQUIVOS DESTA PASTA
    if pasta.exists() and pasta.is_dir():
        for arquivo in pasta.iterdir():
            if arquivo.is_file():
                with open(arquivo, "r") as a:
                    conteudo = a.read()
                    res = hashlib.sha256(conteudo.encode())
                    hash = res.hexdigest()

                dados_arquivo = {
                    "arquivo": f"{arquivo}",
                    "data": f"{now.day}/{now.month}/{now.year}",
                    "hash": f"{hash}",
                    "horario": f"{now.hour}:{now.minute}:{now.second}"
                }

                arquivos_json.append(dados_arquivo)

                with open("dados.json", "w") as dados:
                    json.dump(arquivos_json, dados, indent=4)
            else:
                print("Archives not found.")
    #FUNÇÃO EM DESENVOLVIMENTO
    def comparador():
        with open("dados.json", "r") as dados:
            arquivos_antigos = json.load(dados)

            for arquivo, hash_antigo in arquivos_antigos.items():

                hash_atual = calcular_hash(arquivo)

                if hash_antigo["hash"] == hash_atual:
                    print(f"{arquivo}: Integrity OK")
                else:
                    print(f"{arquivo}: FILE MODIFIED!")

    comparador()

    def monitoramento():

        hashs=[]

        while True:
            with open("dados.json", "r") as arquivo:
                dados = json.load(arquivo)




#FIM DA FUNÇÃO DE ANALISAR LOGS
archiveAdd()
#JESUS LOVE YOU <3
