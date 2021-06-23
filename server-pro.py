import socket
import sys
import time

## end of imports ###

### init ###
print("<-------------------------------welcome-------------------------------> \n --> This is the Project made by Batch-06\n -->Team\n1)U.Srija  (O161587)\n2)G.Sujith Kumar(O161565) \n3)G.Sriniketh (O161932)\n 4)v.vishwa (O161595)" )
print("AIM:This project is to create a chat application with a server and users to enable the users to chat with each others.  To develop an instant messaging solution to enable users to seamlessly communicate with each other. The project should be very easy to use enabling even a novice person to it and secured .")
s = socket.socket()
host = socket.gethostname()
print(host)
print(" server will start on host:",host)
port = 8080
s.bind((host,port))
print("")
print(" Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, " Has connected to the server and is now online ...")
print("")
while 1:
            message = str(input(">> "))
            message = message.encode()
            conn.send(message)
            print("message has been sent...")
            print("")
            incoming_message = conn.recv(1024)
            incoming_message = incoming_message.decode()
            print(" Client : ", incoming_message)
            print("")

