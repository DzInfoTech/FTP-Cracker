import socket,sys

def check(host,uname,pwd):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((host,22))
		print "yays"
		data=s.recv(1024)
		print "1",data
		s.send('USER '+uname+'\r\n')
		data=s.recv(1024)
		print 2,data
		s.send('PASS '+pwd+'\r\n')
		data=s.recv(3)
		print 3,data
		s.send('QUIT\r\n')
		s.close()
		return data

host=str(sys.argv[1])
unames=['dlpuser@dlptest.com','demo']
pwds=['hZ3Xr8alJPl8TtE','password']
for uname in unames:
	for pwd in pwds:
		data = check(host,uname,pwd)
		if attempt=="230":
			print "Succesful: ",(uname,pwd)
			sys.exit(0)
