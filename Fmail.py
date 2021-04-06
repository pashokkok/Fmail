from colorama import init 
from colorama import Fore, Back, Style

print(Fore.MAGENTA)

print('╭━━━╮╱╱╱╱╱╱╭╮')
print('┃╭━━╯╱╱╱╱╱╱┃┃')
print('┃╰━━┳╮╭┳━━┳┫┃╮')
print('┃╭━━┫╰╯┃╭╮┣┫┃╮')
print('┃┃╱╱┃┃┃┃╭╮┃┃╰╮')
print('╰╯╱╱╰┻┻┻╯╰┻┻━╯')

print('Зарегестрируйтесь!, или войдите Makstandart, Nagibator_lohov')

reg1 = input('Login -- ')
reg2 = input('Password -- ')

if reg1 != "Makstandart" and reg1 != "Nagibator_lohov":
	print('Неверный логин или пароль!!!')
	exit()

if reg1 == "Makstandart" :
	print('Здраствуйте Makstandart')
	sms1 = input('введите сообщение: ')
	if sms1 == sms1 :
		print(sms1)
input()

if reg1 == "Nagibator_lohov" :
	print('Здраствуйте Nagibator_lohov')
	sms1 = input('введите сообщение: ')
	if sms1 == sms1 :
		print(sms1)
input()

