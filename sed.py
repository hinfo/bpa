#!/usr/bin/env python
#-*-coding:UTF-8-*-
import re
import urllib2, urllib 
import datetime
from datetime import date

url = "ftp://arpoador.datasus.gov.br/siasus/sia/"
hj = date.today()
m = str(hj.month -1)
y = str(hj.year)
target = "BDSIA"+y+"0"+m+"b.exe"

"""
site = urllib2.urlopen(url)
f1 = site.readlines()
ver = re.compile(text)
"""
print "Buscando versão "+target

try:
	site = urllib2.urlopen(url)
	f1 = site.readlines()
	ver = re.compile(target)
	for line in f1:
		file1 = ver.findall(line)
		if file1 != []:
			version = str(file1)
			print version[2:-2]
			text = version[2:-2]
			erro = 0
		
	
			
		
except:
	print 35*"x"
	print '---ERRO NA ABERTURA DA PAGINA---'
	print 35*"x"
	erro = 1
	


#print erro #//checkpoint
if erro == 1:
	print "Arquivo nao encontrado"
else:
	versao = url+text
	print "Baixando  "+text+" ..."
	download =  urllib.urlretrieve(versao, text)
	print "Download concluido"
	print "Arquivo "+text+" salvo no diretorio atual."
	

print ""
print '\t----- FIM -----'






