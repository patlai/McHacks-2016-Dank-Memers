from Interpreter import *
import time

#initializes the SongSelector & interpreter
interpreter = Interpreter()

words = interpreter.getWords()
for word in words:
	if(word == 'today'):
		print(time.strftime("%d/%m/%y: "))
	try:
		 if(1 <int(word) < 500):
			print(word)
	except ValueError:
		pass
	if(word == 'sets'):
		print(' sets of ')
	if(word == 'bench press' or 'pullps' or 'hello'):
		print(word)

            


