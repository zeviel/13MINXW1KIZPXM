import AminoLab
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.GREEN)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminowikispam", font="shadow"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
comment = input("Comment >> ")
wiki_info = client.get_from_link(input("Wiki Link >> "))
wiki_id = wiki_info.object_Id; ndc_Id = wiki_info.ndc_Id
while True:
		try:
			client.submit_comment(ndc_Id=ndc_Id, message=comment, wiki_Id=wiki_id)
			print("Sended Comment")
		except Exception as e:	print(e)
