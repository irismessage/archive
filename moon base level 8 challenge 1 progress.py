#
# Connect over TCP to the following server 'localhost', 10000
# Initiate communication with GET to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#

#I'm going to come back to this one later

#final level
#megalovania time

#imports
import socket

#loop clamp / overflow function
#(There's probably a proper name for it)
def overflow(num, lim):
  while num > lim:
    num -= lim
  return num

#Caesar cipher cracker function
#I got the GCHQ puzzle book for christmas so I don't have to look
#these up
#hopefully
def et_tu_brute(ciphertext, key):
  #overflow key
  key = overflow(key, 26)
  #init plaintext string
  plaintext = ''
  #iterate through ciphertext applying offset
  for character in ciphertext:
    plaintext += chr(ord(character) + key)
  #return
  return plaintext
#test
print(et_tu_brute('hi', 20))
#scok
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#you know the drill
sock.connect(('localhost', 10000))

#send get
sock.send("GET")
#get messages
response = sock.recv(1024)
print(response)

#split response
sentences = response.split('\n')
#cut out the junk
sentences = sentences[1:4]
print(sentences)
#do each sentence
for sentence in sentences:
  #can't be bothered with language analysis
  #FineI'llDoItMyself.mp4
  #actually it seems like input doesn't work for some reason
  for i in range(27):
		print(et_tu_brute(sentence, i))
    #raw input ew why do they use python 2
    #there's probably a perfectly valid reason though
		#if raw_input("Good enough for you?\n") == 'y':
			#break
  
  #replace sentence with cracked one
  sentence = et_tu_brute(sentence, i)
  
#send cracked sentences
sock.send('\n'.join(sentences))
#recieve
print(sock.recv(1024))
