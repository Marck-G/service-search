import socket

def pscan(target, port, timeout = 0.1):
	"""
		Try a tcp connection over the selected port to the host
	"""
	
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(timeout)	
		conn = s.connect((target, port))
		return True
	except:
		return False

