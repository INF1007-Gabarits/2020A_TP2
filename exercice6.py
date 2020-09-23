import json

def createVocabulary():
    #les mails contient la structure de donnée présente dans mail.json
    with open("mails.json") as json_data:
        emails = json.load(json_data)

    #TODO: Affécté à la variable 'result' le résultat final
    result = {}
    with open('results.json', 'w') as fp:
        json.dump(result, fp, indent=4)

if __name__ == '__main__':
    createVocabulary()