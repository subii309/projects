import json
from difflib import get_close_matches
data=json.load(open(r"C:\Users\hp\Desktop\dic.json"))
word=input("Enter a word : ").upper()



def translet(word):
      if word in data:
          print(data[word])
      elif len(get_close_matches(word,data.keys()))>0:
           inp = input("Type Y if the word  %s matches your given word %s or N : " % (get_close_matches(word,data.keys())[0],word))
           if inp=='Y':
              print(data[get_close_matches(word,data.keys())[0]])
           elif inp== 'N':
              print("word dosent find please recheck word")
        
           else:
              print("we dosnt understand your entry")
      
    
      else:
         print("word dosent exist...")
translet(word)         
