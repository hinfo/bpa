#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Script para download arquivo bpa magnético
# Author: H. Antunes
# Ano: 2016
# Revisao: 1.0 
#

import urllib
url = "ftp://arpoador.datasus.gov.br/siasus/BPA/"

pagina = urllib.urlopen(url)

for linha in pagina:
	if linha.find("exe")!= -1:
		tmp = linha.split()
		nome = tmp[3]
		#print nome
	
pagina.close()
arq = url+nome
print "Baixando arquivo %s." %nome
download = urllib.urlretrieve(arq,nome)
print "Download Concluído"
