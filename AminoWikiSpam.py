import amino
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.GREEN)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminowikispam", font="shadow"))
client = amino.Client()
email = input("Email/Почта: ")
password = input("Password/Пароль: ")
client.login(email=email, password=password)
wikilk = input("Type WikiLink/Введите ссылку на статью: ")
wiki = client.get_from_code(wikilk)
wikiId = wiki.objectId
comId = wiki.path[1:wiki.path.index('/')]
subclient = amino.SubClient(comId=comid ,profile=client.profile)
comment = input("Type a Comment/Введите коммент: ")
while True:
	try:
		sub_client.comment(message=comment, wikiId=wikiId)
		print("Comment Sended/Коммент отправлен")
	except:
		pass
