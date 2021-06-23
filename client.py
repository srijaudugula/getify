import socket

#input("Please enter the hostname of the server : ")
s = socket.socket()
print("<-------------------------------welcome-------------------------------> \n --> This is the Project made by Batch-06\n -->Team\n1)U.Srija  (O161587)\n2)G.Sujith Kumar(O161565) \n3)G.Sriniketh (O161932)\n 4)v.vishwa (O161595)" )
print("AIM:This project is to create a chat application with a server and users to enable the users to chat with each others.  To develop an instant messaging solution to enable users to seamlessly communicate with each other. The project should be very easy to use enabling even a novice person to it and secured .")
print("<----------------------------------------------------->")
print ("connecting plz wait")
host = "DESKTOP-7RF8DAK"
port = 8080
s.connect((host,port))
print(" Connected to chat server")
print("Enter Your name")
name = str(input(">> "))
name = name.encode()
s.send(name)
print("name has been sent...")
opp = s.recv(1024)
opp = opp.decode()
print(" Client : ", opp)
while 1:
            incoming_message = s.recv(1024)
            incoming_message = incoming_message.decode()
            print(opp,":", incoming_message)
            print("")
            message = str(input(">> "))
            message = message.encode()
            s.send(message)
            print("message has been sent...")
            print("")

