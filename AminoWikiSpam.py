import amino
import asyncio
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.GREEN)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminowikispam", font="shadow"))

async def main():
	client = amino.Client()
	email = input("Email >> ")
	password = input("Password >> ")
	await client.login(email=email, password=password)
	wikilink = input("Wiki Link >> ")
	wiki_info = await client.get_from_code(wikilink)
	wikiId = wiki_info.objectId
	communityid = wiki_info.path[1:wiki_info.path.index('/')]
	sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
	comment = input("Comment >> ")
	while True:
		try:
			await sub_client.comment(message=comment, wikiId=wikiId)
			print("Comment Sended")
		except:
			pass

asyncio.get_event_loop().run_until_complete(main())
