import socket 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
urlDigitada=input("Digite: ")
s.connect((urlDigitada, 80))
s.sendall(b"GET / HTTP/1.1\r\nHost:Banrisul.com.br\r\nAccept:text/html\r\n\r\n")
print(str(s.recv(4096), 'utf-8'))
