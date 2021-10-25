import socket
from _thread import *
import sys

"""Server script has to run always and then you can run the client from any network do you want
 Do you want to store the info on harddrive or memory as we have less data we can store it on memory but the question is when the data is large what should we do"""

server = "192.168.0.105"
port   = 5555

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    Socket.bind((server, port))
except socket.error as e:
    str(e)

"""Opens up the 5555 so the server can listen on this port.It needs one optional parameter
if we don't give argument and leave it as it is that mean the server can have unlimited connections"""
Socket.listen(2)

print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])
 
pos = [(0,0),(100,100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            """45,67 -> (45,67) data from client"""
            data = read_pos(conn.recv(2048).decode())
            """ updating current player postion """
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                """ Sending client0 data to the client1"""
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending:  ", reply)
            
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost Connection")
    conn.close()

currentPlayer = 0 
while True:
    """It accepts the incoming connection and save the connection and address variables"""
    conn , addr = Socket.accept()
    print("Connected to:",addr)

    start_new_thread(threaded_client,(conn, currentPlayer))
    currentPlayer += 1
