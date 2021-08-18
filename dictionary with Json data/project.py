import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word,i):
    if word in data:
        return data[word]
    word = word.lower()
    if word in data:
        return data[word]
    if word.capitalize() in data:
        return data[word.capitalize()]
    elif(len(get_close_matches(word,data.keys())) > 0):
        select = input("Do you mean: %s ? Y/N: " % (get_close_matches(word,data.keys())[i]))
        if select == 'Y' or select == 'y':
            return data[get_close_matches(word,data.keys())[i]]
        elif(select == 'N' or select == 'n'):
            if (i< len(get_close_matches(word,data.keys()))-1):
                translate(word,i+1)
            else:
                return "there's no more words"
        else:
            return "We do not understand that"
    else:
        print("fask")
        return "Seems the word not exits, please try again"

word = input("Enter the words: ")

if(word == ""):
    print("You have not enter anything yet.")

output = translate(word,0)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
