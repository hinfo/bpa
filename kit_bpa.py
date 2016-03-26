#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Script para download arquivo kit bpa
# Author: H. Antunes
# Ano: 2016
# Revisao: 2.0 
#

import urllib, urllib2

url = "ftp://arpoador.datasus.gov.br/siasus/sia/"

try:
	site = urllib2.urlopen(url)
	versoes = []
	for linha in site:
		if linha.find("exe")!= -1:
			tmp = linha.split()
			versao = tmp[3]
			versoes.append(versao)
	#print versoes[-2]
	text = versoes[-2]
	arq = url + text
	print "Baixando  ...%s" % text
	download =  urllib.urlretrieve(arq, text)
	print "Download concluido"
	print "Arquivo %s salvo no diretorio atual." % text
	site.close()

		
except:
	print 35*"x"
	print '---ERRO NA ABERTURA DA PAGINA---'
	print 35*"x"
	

print ""
print '\t----- FIM -----'

