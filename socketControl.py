import serial
import socket
import select

if __name__ == '__main__':
	ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
	ser.flush()

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.68.102',5050))

	print('passed')

	while 1:
		msg = s.recv(1024)

		msg = msg.decode("utf-8")
		print(msg)
		msg = msg + "\n"
		ser.write(msg.encode("utf-8"))