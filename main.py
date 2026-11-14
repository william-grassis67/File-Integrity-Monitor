import hashlib
from datetime import datetime
import os
import json
import time

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

	print("What a name of archive?:")
	archive = input("> ")

	with open(archive, "r") as arqv:
		conteudo = arqv.read()
		res = hashlib.sha256(conteudo.encode())
		hash_arquivo_original = res.hexdigest()

	now=datetime.now()

	dados_criacao = {
		"arquivo": archive,
		"data": f"{now.day}/{now.month}/{now.year}",
		"horario": f"{now.hour}:{now.minute}",
		"hash": hash_arquivo_original,
	}


	with open("dados.json", "w") as arquivo:
		json.dump(dados_criacao, arquivo, indent=4)

	print("Hash foi gravado")


	def analisarJson():

		logs=[]

		while True:
			with open("dados.json", "r") as arquivo:
				dados = json.load(arquivo)
				hash_arquivo = dados["hash"]
				time.sleep(1)
				if hash_arquivo != hash_arquivo_original:
					print("OUVE MUDANÇA DO ARQUIVO")
					dados_logs = {
						"arquivo": archive,
						"data": f"{now.day}/{now.month}/{now.year}",
						"hora": f"{now.hour}:{now.minute}"
					}

					logs.append(dados_logs)

					with open("logs.json", "w") as logs_archive:
						json.dump(logs, logs_archive, indent=4)
				else:
					print("ANALISANDO ARQUIVO...")

	analisarJson()

#FIM DA FUNÇÃO DE ANALISAR LOGS
archiveAdd()
#JESUS LOVE YOU <3
