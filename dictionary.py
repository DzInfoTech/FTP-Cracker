import socket, sys, time


def check(host, uname, pwd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 21))

    print("Connecting...\n")
    time.sleep(.1)
    data = s.recv(10240).decode("utf-8", "ignore")
    print("1 ", data)

    print("Sending username "+uname+'\r\n')
    s.send(str.encode('USER '+uname+'\r\n'))
    time.sleep(.1)
    data = s.recv(10240).decode("utf-8", "ignore")
    print('2 response: ', data)

    print("Sending password "+pwd+'\r\n')
    s.send(str.encode('PASS '+pwd+'\r\n'))
    time.sleep(.1)
    data = s.recv(10240).decode("utf-8", "ignore")
    print('3 response: ', data)

    print("Sending QUIT\n")
    s.send(str.encode('QUIT\r\n'))
    time.sleep(.1)
    print('QUIT: ', s.recv(10240).decode("utf-8", "ignore"))

    s.close()
    return data


host = str(sys.argv[1])
unames = ['dlpuser@dlptest.com', 'demo', 'hh']
pwds = ['hZ3Xr8alJPl8TtE', 'password', '123']

for uname in unames:
    for pwd in pwds:
        data = check(host, uname, pwd)
        print(data[:3])
        if data[:3] == "230":
            print("Succesful: ", (uname, pwd))
            sys.exit(0)
