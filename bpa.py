#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

if __name__ == "__main__":

    DATA_SUS_URL = "ftp://arpoador.datasus.gov.br/"
    BPA_URL = "".join([DATA_SUS_URL, "siasus/BPA/"])

    try:
        pagina = urllib.request.urlopen(BPA_URL)

        for linha in pagina:
            linha = linha.decode('utf-8')
            if "exe" in linha:
                tmp = linha.split()
                nome = tmp[3]

        pagina.close()
        arq = BPA_URL + nome
        print(f"Baixando arquivo {nome}")
        urllib.request.urlretrieve(arq, nome)
        print("Download Concluído")
 
    except Exception as e:
        print(f"Erro: {e}")
