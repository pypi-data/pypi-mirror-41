# Load mixer and exit functions
from pygame import mixer 
from sys import exit

def play_it(path):

	try:
		mixer.init()
		mixer.music.load(path)
		mixer.music.play()
		print('Press Ctrl+C to stop')
		while True:
			pass

	# Ctrl+C to stop playing
	except KeyboardInterrupt:
		exit(0)

	# error reporting code
	except Exception as error:
		print('Error: ' + repr(error))