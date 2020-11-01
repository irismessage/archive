#
# Write a script which can connect to the following server
# 'localhost', 10000 over TCP send GET_KEY to download a string.
# The string is compressed with a common algorithm found in many
# websites. Uncompress the string and print it to get the flag.
#

#it might not be base 64
#other options found from google search:
	#gzip
  #http compression
#I'll come back to this tomorrow

#imports
import socket
import base64

#I'm guessing base 64 from the field manual
#here's the function
#turns out I don't need that because the built in module does
#everything
#thanks python
#xkcd.com/353
#def base64_decrypt(ciphertext):
#  plaintext = ''
#  #todo
#  return plaintext

#sock
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect
sock.connect(('localhost', 10000))

#send get key
sock.send("GET_KEY")
#recieve response
response = sock.recv(1024)
print(response)
#decode and print
#was testing if newlines were causing the padding error but now
#I understand
#for part in response.split('\n'):
	#print(part)
print(base64.b32decode(response+"==="))

#wait you don't need to send it back
#send back
#sock.send(base64.b64decode(response))
#recieve
#print(sock.recv(1024))
