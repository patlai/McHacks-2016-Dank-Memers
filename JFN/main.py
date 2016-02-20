from Interpreter import *
from SongPlayer import *
from SongSelector import *

#initializes the SongSelector & interpreter
player = SongPlayer()
selector = SongSelector(player)
interpreter = Interpreter()

words = interpreter.getWords()
for i in range(len(words)):
    if (words[i] == "play" and words[i+1] == "way" and words[i+2] == "up"):
        print("Playing Way Up")
        player.playSong("Way Up")
            


