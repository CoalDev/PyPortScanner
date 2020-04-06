import socket
import subprocess
import sys
from datetime import datetime as time

class portScanner:
    def __init__(self, IP, startPort, endPort):
        self.IP = IP
        self.startPort = startPort
        self.endPort = endPort

    def setIP(self, IP):
        self.IP = IP
    
    def setStartPort(self, startPort):
        self.startPort = startPort

    def setEndPort(self, endPort):
        self.endPort = endPort
    
    def getIP(self):
        return self.IP
    
    def getStartPort(self):
        return self.startPort
    
    def getEndPort(self):
        return self.endPort
    
    def scan(self, startTimer=True, clearTerminal=False):
        if clearTerminal:
            subprocess.call('cls', shell=True)
        
        print('-'*20)
        print('Please wait, scanning remote host: ' + str(self.IP))
        print('-'*20)

        if startTimer:
            self.startTime = time.now()
        
        try:
            for port in range(self.startPort, self.endPort):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.3)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                result = sock.connect_ex((self.IP, port))
                if result == 0:
                    print("Port " + str(port) + ": Open")
                sock.close()
        except KeyboardInterrupt:
            print("You pressed Ctrl+C")
            sys.exit()
        
        except socket.gaierror:
            print("Hostname could not be resolved. Exiting")
            sys.exit()
        
        except socket.error:
            print("Couldn't connect to server")
            sys.exit()
        
        if startTimer:
            self.stopTime = time.now()

            self.totalTime = self.stopTime - self.startTime

            print("Scanning completed in: " + str(self.totalTime))