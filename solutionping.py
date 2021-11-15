import time
 import select
 import binascii
 # Should use stdev
 from statistics import stdev, mean

 ICMP_ECHO_REQUEST = 8


 def checksum(string):
     csum = 0
     countTo = (len(string) // 2) * 2
     count = 0
 @@ -33,48 +37,15 @@ def checksum(string):
     answer = answer >> 8 | (answer << 8 & 0xff00)
     return answer


 def receiveOnePing(mySocket, ID, timeout, destAddr):
     timeLeft = timeout

     while 1:
         startedSelect = time.time()
         whatReady = select.select([mySocket], [], [], timeLeft)
         howLongInSelect = (time.time() - startedSelect)
         if whatReady[0] == []:  # Timeout
             return "Request timed out."

         timeReceived = time.time()
         recPacket, addr = mySocket.recvfrom(1024)

         # Fill in start

         # reverse it. packet = header + data so we're gonna separate the two here
         # Fetch the ICMP header from the IP packet
         header = recPacket[20:28]
         type, code, thisChecksum, msgID, seq = struct.unpack("bbHHh", header)

         if type == 0 and msgID == ID:
             return timeReceived - startedSelect

         # Fill in end
         timeLeft = timeLeft - howLongInSelect
         if timeLeft <= 0:
             return "Request timed out."


 def sendOnePing(mySocket, destAddr, ID):
     # Header is type (8), code (8), checksum (16), id (16), sequence (16)

     myChecksum = 0
     # Make a dummy header with a 0 checksum
     # struct -- Interpret strings as packed binary data
     header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
     data = struct.pack("d", time.time())
     # Calculate the checksum on the data and the dummy header.
     myChecksum = checksum(header + data)

     # Get the right checksum, and put in the header

     if sys.platform == 'darwin':
         # Convert 16-bit integers from host to network  byte order
 @@ -83,51 +54,115 @@ def sendOnePing(mySocket, destAddr, ID):
         myChecksum = htons(myChecksum)

     header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
     packet = header + data

     mySocket.sendto(packet, (destAddr, 1))  # AF_INET address must be tuple, not str

     # Both LISTS and TUPLES consist of a number of objects
     # which can be referenced by their position number within the object.


 def doOnePing(destAddr, timeout):
     icmp = getprotobyname("icmp")

     # SOCK_RAW is a powerful socket type. For more details:   http://sockraw.org/papers/sock_raw
     mySocket = socket(AF_INET, SOCK_RAW, icmp)

     myID = os.getpid() & 0xFFFF  # Return the current process i
     sendOnePing(mySocket, destAddr, myID)
     delay = receiveOnePing(mySocket, myID, timeout, destAddr)
     mySocket.close()
     return delay


 def ping(host, timeout=1):
     # timeout=1 means: If one second goes by without a reply from the server,
     # the client assumes that either the client's ping or the server's pong is lost
     dest = gethostbyname(host)
     print("Pinging " + dest + " using Python:")
     print("")
     # Calculate vars values and return them
     delayList = []
     vars = [str(0), str(0.0), str(0), str(0.0)]
     # Send ping requests to a server separated by approximately one second
     for i in range(0, 4):
         delay = doOnePing(dest, timeout) * 1000
         delayList.append(delay)
         print(delay)
         time.sleep(1)  # one second

     packet_min = min(delayList)
     packet_max = max(delayList)
     packet_avg = mean(delayList)
     stdev_var = stdev(delayList)
     vars = [str(round(packet_min, 2)) , str(round(packet_avg, 2)), str(round(packet_max, 2)), str(round(stdev_var, 2))]

     return vars


 if __name__ == '__main__':
     ping("google.co.il")
