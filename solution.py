# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to serve...')

        connectionSocket, addr =  serverSocket.accept()# Fill in start      #Fill in end
        try:

            try:
                message =  "200 OK"
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = connectionSocket.recv(1024).decode(f)  #Fill in end

                # Send one HTTP header line into socket.
                # Fill in start
                connectionSocket.send(message)
                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                message = "404 Not Found"
                connectionSocket.send(message)
                connectionSocket.close()

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
