import socket

port = 80
urlDigitada = input("Digite:")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((urlDigitada,port))
s.send(b"GET /\r\n")
print(str(s.recv(4096),'utf-8'))
s.close()

