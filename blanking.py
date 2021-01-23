import requests, os, time, json

header = """
  ____  _             _    _
 |  _ \| |           | |  (_)
 | |_) | | __ _ _ __ | | ___ _ __   __ _
 |  _ <| |/ _` | '_ \| |/ / | '_ \ / _` |
 | |_) | | (_| | | | |   <| | | | | (_| |
 |____/|_|\__,_|_| |_|_|\_\_|_| |_|\__, |
                                    __/ |
                                   |___/
"""

def deleteallmessages():
    headers = {
        "authorization": auth_token,
        "accept-language": "fr"
    }
    userid = requests.get("https://discordapp.com/api/v8/users/@me", headers=headers).json()["id"]
    r = requests.get("https://discordapp.com/api/v8/users/@me/channels", headers=headers).json()
    for dm in r:
        dm_id = dm["id"]
        dm_name = dm["recipients"][0]["username"]
        r2 = requests.get(f"https://discordapp.com/api/v8/channels/{dm_id}/messages", headers=headers).json()
        for message in r2:
            message_id = message["id"]
            message_author = message["author"]["id"]
            message_content = message["content"]
            if message_author == str(userid):
                r3 = requests.delete(f"https://discordapp.com/api/v8/channels/{dm_id}/messages/{message_id}", headers=headers)
                if r3.status_code == 204:
                    print(f"Message supprimé dans les DM de {dm_name} : {message_content}")
                elif r3.status_code == 429:
                    time1 = r3.json()["retry_after"]
                    print(f"Rate limite atteinte, prochaine suppression dans {time1}s")
                    time.sleep(int(r3.json()["retry_after"])+0.5)
                else:
                    print("Erreur discord, prochain essai dans 1 seconde")
                    time.sleep(1)
                time.sleep(0.2)


while True:
    os.system("cls")
    print(header)
    try:
        auth_token = str(input("Entrez votre token : "))
        headers = {
            "authorization": auth_token,
            "accept-language": "fr"
        }
        r = requests.get("https://discord.com/api/v8/users/@me/relationships", headers=headers)
        if r.status_code == 200:
            break
        else:
            print("Token invalide...")
            time.sleep(2)
            continue
    except:
        print("\nErreur, veuillez recommencer...")
        time.sleep(1)

while True:
    os.system("cls")
    print(header)
    print("[1] Delete All Messages\n")
    try:
        menuchoice = int(input("Votre choix : "))
        break
    except:
        print("\nErreur, veuillez entrez un choix correct...")
        time.sleep(2)

if menuchoice == 1:
    deleteallmessages()

# fesse
