# arduinoRead.py


import socket
import serial
#set this port to the port arduino is connected
ARDUINO =  "COM7"

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.connect(("127.0.0.1", 26232))
	ser =  serial.Serial(ARDUINO, timeout=1)
	prevVal = None
	while 1:
		# Read the serial value
		ser.flushInput()
		serialValue = ser.readline().strip()
		# Catch any bad serial data:
		try:
			if serialValue != prevVal:
				# Print the value if it differs from the prevVal:
				server.send((serialValue))
				prevVal = serialValue
		except ValueError:
			pass

if __name__ == '__main__':
	main()