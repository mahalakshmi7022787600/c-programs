#Python 2.x program for Speech Recognition 

import speech_recognition as sr 


r = sr.Recognizer() 


print ("Say Something")
#litens for the user's input 

		
try: 
	text = r.recognize_google(audio) 
	print ("you said: "+ text) 
	
	#error occurs when google could not understand what was said 
	
except sr.UnknownValueError: 
	print("Google Speech Recognition could not understand audio") 
	
except sr.RequestError as e: 
	print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
