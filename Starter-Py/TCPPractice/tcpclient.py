import socket

def Main():
    host ='147.26.87.151'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    message = input('Type message -> ')
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        print('Received from server: ', str(data))
        message = input('->')
    s.close()

if __name__ == '__main__':
    Main()