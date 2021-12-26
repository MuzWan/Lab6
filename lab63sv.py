import socket
import sys
import time
import math
import errno
from multiprocessing import Process



def calcDeg(i):
    print("\nCalculate for Degrees:",i)
    i=float(i)
    answer=math.degrees(i)
    print("\nAnswer:",answer)
    return answer


def calcRad(i):
    print("\nCalculate for Radians:",i)
    i=float(i)
    answer=math.radians(i)
    print("\nAnswer:",answer)
    return answer

    
def calcSin(i):
    print("\nCalculate for Sine of degrees:",i)
    i=float(i)
    answer=math.sin(i)
    print("\nAnswer:",answer)
    return answer    
    

def process_start(s_sock):
    s_sock.send(str.encode('Welcome to Online Calculator Server'))
    
    while True:
        data = s_sock.recv(2048)
        data=data.decode('utf-8')
        
        try:
            mfunc,result=data.split(" ",2)
        except:
            print("Cannot receive data")
            break
        
        
        if(mfunc=='1'):
            answer=calcDeg(result)
        elif(mfunc=='2'):
            answer=calcRad(result)
        elif(mfunc=='3'):
            answer=calSin(result)
        elif(mfunc=='exit'):
            break
        equal="\nAnswer:%s\n"% str(answer)
        s_sock.sendall(str.encode(equal))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("Listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:        
            print('an exception occurred!')
            print(e)
            sys.exit(1)
    finally:
           s.close()
