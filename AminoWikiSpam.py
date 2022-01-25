import amino
from colorama import init, Fore
from pyfiglet import figlet_format
init()
print(f"""{Fore.GREEN}
Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(figlet_format("aminowikispam", font="shadow"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
link_info = client.get_from_code(input("-- Wiki link::: ")).json["linkInfoV2"]
com_id = link_info["extensions"]["linkInfo"]["ndcId"]
wiki_id = link_info["extensions"]["linkInfo"]["objectId"]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = input("-- Message::: ")
while True:
		try:
			sub_client.comment(message=message, wikiId=wiki_id)
			print("-- Comment is sent...")
		except Exception as e:
			print(e)
