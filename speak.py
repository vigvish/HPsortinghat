from sys import argv
import subprocess

import urllib
import socket


""" Transcribe the sentence """
sentence = argv[1]
#sentence = sentence.replace(" ", "%20")
print sentence
sentence = urllib.quote(sentence)
print sentence
command = "curl http://localhost:8082/api/v1/tts.json/play/Daniel/" + sentence + " > /Users/neelcm/pi_share/stream.mp3"
print command
subprocess.call(command, shell=True)


""" Speak on the pi """
UDP_IP = "10.0.1.21"
UDP_PORT = 5004
MESSAGE = argv[2] + "," + argv[3] + "," + argv[4]

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))