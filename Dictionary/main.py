import json
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        reply = input("Do you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if reply == "Y" or reply == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif reply == "N" or reply == "n":
            return "The word doesn't exist, Please check the word"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist."

word = input("Enter the word to search: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)