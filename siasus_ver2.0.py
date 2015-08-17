#!/usr/bin/env python
#-*-coding: utf-8-*-

"""
######################################################################
# Script para fazer Download da última versão as tabelas do BDSIASUS #
#                             VERSÂO 2.0                             #
######################################################################
"""	

import urllib
import re
import urllib2, datetime
from datetime import date

url = 'ftp://arpoador.datasus.gov.br/siasus/sia/'
url2 ='ftp://arpoador.datasus.gov.br/siasus/bpa/'  
hj = date.today()
m = str(hj.month - 1)
y = str(hj.year)



def ping(url):
	try: 
		urllib2.urlopen(url)
		erro = 0
	except:
		erro = 1
	return erro
	
erro = ping(url)

#print html // checkpoint

if erro == 0:
	page = urllib2.urlopen(url)
	html = page.readlines()
	#checkppoint
	#print html 
	remove = [z.strip() for z in html]
	bdsia = str(remove[91]) # trocar para buscar o arquivo correto sempre 
	ver = bdsia[-16:]
	print "Buscando versao: "+ver
	print "Arquivo encontrado!"
	print "Baixando o arquivo "+ver+" ..."	
	file = url+ver
	#print ver// checkpoint
	down = urllib.urlretrieve(file,ver)
	print file
	print "Concluido"
else : 
	print "Página "+url+ " não encontrada, verifique sua conexão de rede"


