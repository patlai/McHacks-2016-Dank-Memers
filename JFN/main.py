from Interpreter import *
from AudioFile import *
import json

#initializes the SongSelector & interpreter
interpreter = Interpreter()

#ask user what their name is
#depending on what the user says, save the data in the file according to their name
#afte te user says their name, ask what (exercises) they did today

words = interpreter.getWords()
a = 100
b= 20
bench = 315

data = {
	'abc' : b,
	'bench' : b,
	'hello' : (a+b)
}
other = {
	'bench' : bench
}

filename = words[0]

f = open((filename+'.html'),'w')
words = interpreter.getWords()
stats = {
	'' + words[0] : 'a'
}
f.write(json.dumps(stats))

#g = open("user1.txt",'w')
#g.write(json.dumps(other))