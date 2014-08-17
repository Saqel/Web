# -*-coding: utf-8 -*-

import os
import sys
import cgi
import re
location = os.getcwd()

file = open('%s/check-data.html' % location, 'r')
HTML = file.read()
file.close()

def checPhone(phone):
	return re.match('[+][0-9]{1,3}[-][0-9]{3}[-][0-9]{3}[-][0-9]{2}[-][0-9]{2}', phone) is not None 
	
def checkEmail(email):
	return re.match('', email) is not None

def checkFirstName(firstName):
	return re.match('', firsName) is not None

def checkSecondName(secondName):
	return re.match('', seconName) is not None
	
index = 0
form = cgi.FieldStorage()
names = ('firstName', 'secondName', 'phoneNumber', 'email', 'birthday', 'comment')
forReplace = ('$FIRST$', '$SECOND$', '$PHONE$', '$EMAIL$', '$BIRTHDAY$', '$TEXTAREA$')
for name in names:
	'''
	if name[0]:
	        if checkFirstName(firstName) == True:
	                continue
	        else:
	                break
	if name[2]:
		if checkPhone(phone) == True:
			continue
		else:
			break
	'''
	Field = name[0].upper() + name[1:]
	Field = cgi.escape(form['%s' % name].value)
	HTML = HTML.replace('%s' % forReplace[index], Field)
	index += 1


"""
Вручную перебор изменение

FirstName = cgi.escape(form['firstName'].value)  # Через регулярные выражения проверить соответствие ввода
SecondName = cgi.escape(form['secondName'].value)	# Имени и фамилии(чтобы не было неправильного ввода: цифр/знаков и т.д.)
PhoneNumber = cgi.escape(form['phoneNumber'].value)	# Проверить, телефон ли введён(через регулярные выражения)

Email = cgi.escape(form['email'].value)	# Проверить e-mail ли введён(через регулярные выражения!) 
										# и назначить на него ссылку для отправки сообщения


Birthday = cgi.escape(form['birthday'].value) # Изменить представление даты

#Marial = cgi.escape(form['marial'].value)  # Проверить выбранное значение и вставить его.

Comment = cgi.escape(form['comment'].value) 
HTML = HTML.replace('$FIRST$', FirstName)
HTML = HTML.replace('$SECOND$', SecondName)
HTML = HTML.replace('$PHONE$', PhoneNumber)
HTML = HTML.replace('$EMAIL$', Email)
HTML = HTML.replace('$BIRTHDAY$', Birthday)
#HTML = HTML.replace('$MARIAL$', Marial)
HTML = HTML.replace('$TEXTAREA$', Comment)
"""

print('Content-type: text/html\n')
print(HTML)
