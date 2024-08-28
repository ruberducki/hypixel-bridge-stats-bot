#by ruberducki
import requests

APIKEY = ''

username = ''
uuid = ''

#defining a function to 
def getinfo(call):
    r = requests.get(call)
    return r.json()

#this can be removed and you can just input the apikey into the variable this is just if you dont know how to code and dont want to mess with it
APIKEY = input('Input API key')

while True:

    username = input('Input user')

    if username != '':
    
        try:
            #calling mojang api to get the uuid of a username
            uuidurl = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
            response = requests.get(uuidurl)
            uuid = response.json()['id']
        except:
            #prints error message
            print('Username does not exist (Potential error with mojang api)')
            uuid = ''

        if uuid != '':
            
            hyapiurl = f'https://api.hypixel.net/player?key={APIKEY}&uuid={uuid}'

            #sends a request to the hyapi to get  stats
            data = getinfo(hyapiurl)

            division = ''

            #checks the players division with embeds (im bad at coding)
            try:
                if data["player"]["stats"]["Duels"]["bridge_godlike_title_prestige"] != 0:
                    division = 'Godlike ' + str(data["player"]["stats"]["Duels"]["bridge_godlike_title_prestige"])
            except:
                try:
                    if data["player"]["stats"]["Duels"]["bridge_grandmaster_title_prestige"] != 0:
                        division = 'Grandmaster ' + str(data["player"]["stats"]["Duels"]["bridge_grandmaster_title_prestige"])
                except:
                    try:
                        if data["player"]["stats"]["Duels"]["bridge_legend_title_prestige"] != 0:
                            division = 'Legend ' + str(data["player"]["stats"]["Duels"]["bridge_legend_title_prestige"])
                    except:
                        try:
                            if data["player"]["stats"]["Duels"]["bridge_master_title_prestige"] != 0:
                                division = 'Master ' + str(data["player"]["stats"]["Duels"]["bridge_master_title_prestige"])
                        except:
                            try:
                                if data["player"]["stats"]["Duels"]["bridge_diamond_title_prestige"] != 0:
                                    division = 'Diamond ' + str(data["player"]["stats"]["Duels"]['bridge_diamond_title_prestige'])
                            except:
                                try:
                                    if data["player"]["stats"]["Duels"]["bridge_gold_title_prestige"] != 0:
                                        division = 'Gold ' + str(data["player"]["stats"]["Duels"]["bridge_gold_tile_prestige"])
                                except:
                                    try:
                                        if data["player"]["stats"]["Duels"]["bridge_iron_title_prestige"] != 0:
                                            division = 'Iron ' + str(data["player"]["stats"]["Duels"]["bridge_iron_title_prestige"])
                                    except:
                                        try:
                                            if data["player"]["stats"]["Duels"]["bridge_rookie_title_perstige"] != 0:
                                                division = 'Rookie ' + str(data["player"]["stats"]["Duels"]["bridge_rookie_title_prestige"])
                                        except:
                                            division = 'No division'
            #checks amount of wins
            try:
                wins = data["player"]["stats"]["Duels"]["bridge_doubles_wins"] + data["player"]["stats"]["Duels"]["bridge_3v3v3v3_wins"] + data["player"]["stats"]["Duels"]["bridge_four_wins"] + data["player"]["stats"]["Duels"]["bridge_duel_wins"]
            except:
                try:
                    wins = data["player"]["stats"]["Duels"]["bridge_doubles_wins"] + data["player"]["stats"]["Duels"]["bridge_duel_wins"]
                except:
                    try:
                        wins = data["player"]["stats"]["Duels"]["bridge_duel_wins"]
                    except:
                        wins = data["player"]["stats"]["Duels"]["bridge_doubles_wins"]

            #checks amount of losses
            try:
                losses = data["player"]["stats"]["Duels"]["bridge_doubles_losses"] + data["player"]["stats"]["Duels"]["bridge_3v3v3v3_losses"] + data["player"]["stats"]["Duels"]["bridge_four_losses"] + data["player"]["stats"]["Duels"]["bridge_duel_losses"]
            except:
                try:
                    losses = data["player"]["stats"]["Duels"]["bridge_doubles_losses"] + data["player"]["stats"]["Duels"]["bridge_duel_losses"]
                except:
                    try:
                        losses = data["player"]["stats"]["Duels"]["bridge_duel_losses"]
                    except:
                        losses = losses = data["player"]["stats"]["Duels"]["bridge_doubles_losses"]

            #calculates wlr
            wlr = round(wins/losses, 2)

            #prints data
            print('Bridge division: ' + division)
            print('Wins: ' + str(wins))
            print('Losses: ' + str(losses))
            print('WLR: ' + str(wlr))
            print('\n')