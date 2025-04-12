#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib.request as request
import urllib.error as error

DATA_SUS_URL = "ftp://arpoador.datasus.gov.br/"
SIA_URL = "".join([DATA_SUS_URL, "siasus/sia/"])

if __name__ == "__main__":
	try:
		site = request.urlopen(SIA_URL)
		versoes = []
		for linha in site:
			decoded_linha = linha.decode("utf-8")
			if "exe" in decoded_linha:
				tmp = decoded_linha.split()
				versao = tmp[3]
				versoes.append(versao)
		text = versoes[-2]
		arq = SIA_URL + text
		print(f"Baixando  ...{text}")
		download = request.urlretrieve(arq, text)
		print("Download concluido")
		print(f"Arquivo {text} salvo no diretorio atual.")
		site.close()

		
	except error.URLError as e:
		print(35*"x")
		print("---ERRO NA ABERTURA DA PAGINA---")
		print(f"Erro: {e}")
		print(35*"x")
	
	print()
	print("\t----- FIM -----")
