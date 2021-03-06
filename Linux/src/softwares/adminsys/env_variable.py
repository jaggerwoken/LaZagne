#!/usr/bin/env python
import os
from config.header import Header
from config.write_output import  print_debug, print_output

class Env_variable():

	def retrieve_password(self):
		values = {}
		pwdFound = []
		
		# print the title
		Header().title_debug('Environnement variables')
		
		# --------- http_proxy --------
		tmp = ''
		if 'http_proxy' in os.environ:
			tmp = 'http_proxy'
		elif 'HTTP_Proxy' in os.environ:
			tmp = 'HTTP_Proxy'
		
		if tmp:
			values["Variable"] = tmp
			values["Password"] = os.environ[tmp]
			pwdFound.append(values)
			
		# --------- https_proxy --------
		tmp = ''
		if 'https_proxy' in os.environ:
			tmp = 'https_proxy'
		elif 'HTTPS_Proxy' in os.environ:
			tmp = 'HTTPS_Proxy'
		
		if tmp:
			values["Variable"] = tmp
			values["Password"] = os.environ[tmp]
			pwdFound.append(values)
		
		tab = ['passwd', 'pwd', 'pass', 'password']
		for i in os.environ:
			for t in tab:
				if (t.upper() in i.upper()) and (i.upper() != 'PWD') and (i.upper() != 'OLDPWD'):
					values["Variable"] = i
					values["Password"] = os.environ[i]
		pwdFound.append(values)
		
		# write credentials into a text file
		if len(values) != 0:
			# print the results
			print_output('Environnement variables', pwdFound)
		
		else:
			print_debug('INFO', 'No passwords stored in the environment variables.')
		