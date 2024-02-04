import getpass
import telnetlib
import configparser

f = open("devices.txt")

configParser = configparser.RawConfigParser()   
configFilePath = r'/devices.cfg'
configParser.read(configFilePath)

for IP in f:

    user = input("Enter your remote account: ")
    password = getpass.getpass()

    IP = IP.strip()
    HOST = IP
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")
    readOut = tn.read_all()
    saveOut = open(HOST, "w")
    saveOut.write(readOut.decode("ascii"))
    saveOut.write("n")
    saveOut.close()
    
    print(tn.read_all().decode('ascii'))