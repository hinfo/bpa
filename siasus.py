#!/usr/bin/env python
import urllib2, urllib 
import datetime
from datetime import date

url = "ftp://arpoador.datasus.gov.br/siasus/sia/"
hj = date.today()
m = str(hj.month)
y = str(hj.year)
text = "BDSIA"+y+"0"+m+"a.exe"

count = 0
versao = url+text

try:
	site = urllib2.urlopen(url)
	f1 = site.readlines()
	for line in f1:
		if text in line:
			count = count+1 
			print line

except:
	print 35*"x"
	print '---ERRO NA ABERTURA DA PAGINA---'
	print 35*"x"


#print count #//checkpoint
if count == 0:
	print "Arquivo nao encontrado"
else:
	print "Baixando  "+text+" ..."
	download =  urllib.urlretrieve(versao, text)
	print "Download concluido"
	print "Arquivo "+text+" salvo no diretorio atual."
	
print ""
print '\t----- FIM -----'






