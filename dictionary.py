import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
	word=word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word,data.keys()))>0:
			nw=input("Did You Mean %s instead of %s?Press Y for Yes and N for No."%(get_close_matches(word,data.keys())[0],word))
			if nw=="Y":
				return data[get_close_matches(word,data.keys())[0]]
			elif nw=="N":
				print("Word Not Found")
			else:
				print("Wrong Choice")
	else:
		print("Word Not Found")

temp=input("Enter the word to be searched:\n")
op=translate(temp)
if type(op)==list:
	for item in op:
		print(item)
else:
	print(op)
