#!/usr/bin/env python
#-*- coding: utf-8
# Developer: Mehmet KARCI - www.mkrc.net - mk@mkrc.net
import os
import re
import subprocess
dir = "/home/"
pattern = {'.php':"#c3284d#\n(.*)\n#/c3284d#", '.html':"<!--c3284d-->(.*)<!--/c3284d-->", '.htm':"<!--c3284d-->(.*)<!--/c3284d-->", '.js':"/\*c3284d\*/\n(.*)\n/\*/c3284d\*/", '.tpl':"<!--c3284d-->(.*)<!--/c3284d-->"}

ps = subprocess.Popen(['grep', '-ril', 'c3284d', dir], stdout=subprocess.PIPE)
output = ps.communicate()[0]
for line in output.splitlines():
	fileName, fileExtension = os.path.splitext(line) #find file extension
	if fileExtension in pattern:
		yeni = open(line)
		content = yeni.read()
		yeni.close()
		ara = re.search(pattern[fileExtension], content) #find virus code via pattern
		if ara:
			yaz = open(line, "w")
			degistir = content.replace(ara.group(),"")
			yaz.write(degistir)
			yaz.close()
			print "Cleaned: ", line 
	else:
		baseName = os.path.basename(line)
		if(len(baseName)==1): 
			os.remove(line)
			print "Deleted: ", line
