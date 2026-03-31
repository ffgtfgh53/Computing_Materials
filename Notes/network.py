import socket		

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		

port = 12345			
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	
s.bind(('', port))	

s.listen(5)	# 0 backlog conn
while True:
    c, addr = s.accept()
    c.send("Hi\n".encode())
    print(addr)
    while True:
        data = c.recv(4096)
        data = data.decode()

        processed_data = data.rstrip()
        print(processed_data)

        if processed_data == "exit":
            c.send("Ok, closing connection...\x04".encode())
            c.shutdown(socket.SHUT_RDWR)
            c.close()
            break
        try:
            c.send("Hello, message received\n".encode())
        except BrokenPipeError:
            c.close()
            print("Broken pipe")
            break

s.close()
del(s) #so s will not hang around in ipykernel