import socket

ClientSocket = socket.socket()
host = '192.168.56.101'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
print("\nONLINE CALCULATOR CONSIST OF DEGREES/RADIANS/SINE ONLY\n\n")

while True:
    
    mfunc=input("Enter 1 for Convert Radians to Degrees / 2 for Convert Degrees to Radians / 3 for Returns Sine Number. Enter (exit) to terminate: ")    
    if(mfunc=='1'):
        result=input("Enter number:")
    elif(mfunc=='2'):
        result=input("Enter number:") 
    elif(mfunc=='3'):
        result=input("Enter number:")        
    elif(mfunc=='exit'):
        break
    
    message=mfunc+" "+result
    ClientSocket.send(str.encode(message))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()
