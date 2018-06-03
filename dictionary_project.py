import json
from difflib import get_close_matches

data = json.load(open(r"C:\Users\hp\Desktop\dictionary.json"))

#print(data.keys())



word = input("Enter a word : ").upper()

def translate(word):
    if word in data:
        print(data[word])
    elif len(get_close_matches(word,data.keys())) > 0 :
        inp = input("type Y if the word %s matches your given word %s or N " %(get_close_matches(word,data.keys())[0],word))
        #rec_list = get_close_matches(word,data.keys())
        if inp == 'Y' :
            print(data[get_close_matches(word,data.keys())[0]])
        elif inp == 'N':
            print("word doesn't exist, please double check it")
        else :
            print("we didn't understand your entry")
    else :
        print("word doesn't exist")

translate(word)
