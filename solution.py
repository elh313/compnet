from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket= socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    #recv = clientSocket.recv(1024).decode()


    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    #recv1 = clientSocket.recv(1024).decode()


    # Send MAIL FROM command and print server response.
    # Fill in start
    fromCommand = 'MAIL FROM: <elh313@nyu.edu> \r\n'
    clientSocket.send(fromCommand.encode())
    #recv2 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    RCPTCommand = 'RCPT TO: <elh313@nyu.edu> \r\n'
    clientSocket.send(RCPTCommand.encode())
    #recv3 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    #recv4 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send message data.
    # Fill in start

    clientSocket.send(msg.encode())
    #recv5 = clientSocket.recv(1024).decode()

    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    #recv7 = clientSocket.recv(1024).decode()

    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
