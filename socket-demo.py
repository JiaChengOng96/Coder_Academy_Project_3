#socket demo
import socket
import sys
import random

HOST = '127.0.0.1'
#HOST = '0.0.0.0'    # Symbolic name meaining all available interfaces 
PORT = 50007        # Arbitarary non-privilaged port
s = None

# Ask the kernel for a newly-initialised (unbound) socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Force the socket to continue after crashing
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Assign a port number to the socket and specify the network interface
# (Note, HOST refers to an interface of THIS machine, not a remote one)
s.bind((HOST, PORT))

# Ask the kernel to accept incoming connections and queue them
s.listen()

#return_value = s.value()
#s2 = return_value[0]
#address = return_value[1]

# waiting for a connetion
# when one is made, put the new socket into s2
(conn_sock, address) = s.accept()

print(conn_sock)
print(address)

correct = "\nCongrats... Continue...\n"
wrong = "\nBzz.... wrong guess... try again....\n"

helloText = """Welcome to the hangman game!!!!
This is the guessing game -- try your best to answer it
"""

correctTextSoFar = "\nSo far you have guest: "

goodbyeText = "\nYou have completed the whole game... try again later..\n\n"
lostText = "\nYou have lost the game.... try again later..\n\n"

word = ["hello", "code", "sucks", "python", "letter", "whoami", "apple", "javascript", "language", "packing", "reverse", "shell", "academy"]

index = random.randint(0,len(word))

question = word[index]

if len(question) <= 6:
    lives = 5
else:
    lives = 7

questionLong = "the word for you is: " + ("_ "*len(question)) + "\n\nYour Choice is:  "

encodedCor = str.encode(correct)
encodedWrong = str.encode(wrong)
encodedStr = str.encode(helloText)
encodedQues = str.encode(questionLong)

conn_sock.send(encodedStr)
conn_sock.send(encodedQues)

currentGuess = ["_ "] * len(question)

while True:
    # wait for a packet from the client
    # puts the contents into 'data'
    data = conn_sock.recv(1024)
    if len(data) == 0:
        break

    temp = data.decode().rstrip().lower()
    print("User type: " + temp)

    if temp in question:
        conn_sock.send(encodedCor)
        indices = [i for i, x in enumerate(question) if x == temp]
        for b in indices:
            currentGuess[b] = temp + " "
    else:
        lives -= 1
        livesLeft = "\nYou have only " + str(lives) + " lives left"
        conn_sock.send(encodedWrong)

    conn_sock.send(str.encode(livesLeft))
    conn_sock.send(str.encode(correctTextSoFar))
    conn_sock.send(str.encode(''.join(currentGuess)))
    conn_sock.send(str.encode("\n"))
    if "_ " not in currentGuess:
        conn_sock.send(str.encode(goodbyeText))
        break
    if lives == 0:
        conn_sock.send(str.encode(lostText))
        conn_sock.send(str.encode(question))
        break
    conn_sock.send(str.encode("\nNext guess: "))
                
conn_sock.close()
s.close()

print("Bye")