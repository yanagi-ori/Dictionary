import json
from difflib import get_close_matches

prefs = json.load(open("user_settings.json"))
if prefs["cur"] == '':
    lng = input("Choose ru or en language: ")
    prefs["cur"] = lng
    with open('user_settings.json', 'w') as f:
        f.write(json.dumps(prefs))
    data = json.load(open(prefs[lng]))
else:
    data = json.load(open(prefs[prefs["cur"]]))


def retrive_definition(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y, n] " % get_close_matches(word, data.keys())[0])
        if action.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif action.lower() == 'n':
            if len(get_close_matches(word, data.keys())[1:]) == 0:
                return "The word doesn't exist, yet."
            else:
                print(len(get_close_matches(word, data.keys())))
                print("Please, look for some other variants and type its number to choose "
                      "or n if there is no searched word")
                for i in range(1, len(get_close_matches(word, data.keys()))):
                    print(i, '-', get_close_matches(word, data.keys())[i])
                return data[get_close_matches(word, data.keys())[int(input())]]
        else:
            return "We don't understand your entry. Apologies."

    else:
        return "This word doesn't exist"


word_user = input("Enter a word: ")
output = retrive_definition(word_user)
if isinstance(output, list):
    for item in output:
        print("-", item)
else:
    print("-", output)

input()
