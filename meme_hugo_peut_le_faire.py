import twint
import json
"""
INSTALLER TWINT : pip3 install twint
Pour lancer une récolte : changer le keyword
lancer la commande sur son terminal (dans le dossier du code) : python3 meme_hugo_peut_le_faire.py
Dans le dossier, un fichier json apparait :)
"""
KEYWORD = '"poêle à granulés"'
FILE_NAME = KEYWORD + ".json"
def load_json(path):
    with open(path) as file:
        data = json.load(file)
    return data
def save_json(tweets,file_name=FILE_NAME):
    with open(file_name, "w+") as outfile:
        json.dump(tweets, outfile,ensure_ascii=False)
    return file_name
def scrap(keyword, limit=200):
    c = twint.Config()
    c.Search = keyword
    c.Limit = limit
    c.Store_object = True
    c.Lang = "fr"
    twint.run.Search(c)
    out_json = save_json([x.__dict__ for x in twint.output.tweets_list])
    return out_json

scrap(KEYWORD)
