#!/usr/bin/env python
# coding: utf8
#
# Andreas Müller, 2011
# am@0x7.ch
#
# This code may be freely used and distributed under GNU GPL conditions.

"""
Controller for Prologix GPIB USB interface.
"""

import termios
import fcntl
import os
import time

DEVICE = "/dev/ttyUSB0"

class PrologixGPIB:
	"""
	Class to control the Prologix GPIB USB interface.
	"""
	
	def __init__(self, addr=1):
		# open device
		self.device = open(DEVICE, "a+")
		# configure tty settings
		ttyattr = termios.tcgetattr(self.device)
		ttyattr[2] = ttyattr[2] | termios.PARENB | termios.CS8	#cfloag
		ttyattr[4] = termios.B9600	#ispeed
		ttyattr[5] = termios.B9600	#ospeed
		termios.tcsetattr(self.device,termios.TCSANOW,ttyattr)
		# make device read non-blocking
		fd = self.device.fileno()
		fl = fcntl.fcntl(fd, fcntl.F_GETFL)
		fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
		# initialize Prologix USB controller
		self.set_prologix_auto_mode(False)
		self.set_gpib_addr(addr)
		self.send_prologix_command("ifc")
	
	def close(self):
		self.device.close()

	def write(self, string):
		print ">>> "+string,
		self.device.write(string)

	def read(self):
		data = []
		try:
			while True:
				data.append(self.device.readline())
		except:
			pass
		return "".join(data)

	def send_prologix_command(self, command):
		self.write("++%s\n" % command)

	def get_prologix_version(self):
		self.send_prologix_command("ver")
		return self.read()

	def get_prologix_help(self):
		self.send_prologix_command("help")
		return self.read()

	def set_prologix_auto_mode(self, enabled):
		self.send_prologix_command("auto %d" % int(enabled))

	def set_gpib_mode(self, controller):
		"""
		Set GPIB mode.
		
		@param controller: False -> device mode, True -> controller mode
		"""
		self.send_prologix_command("mode %d" % int(controller))

	def set_gpib_addr(self, addr):
		self.send_prologix_command("addr %d" % addr)

	def set_gpib_eoi(self, enabled):
		self.send_prologix_command("eoi %d" % int(enabled))

	def set_loc(self):
		"""
		Enable front panel operation of the currently addressed instrument.
		"""
		self.send_prologix_command("loc")
	
	def gpib_send(self, command):
		self.write("%s\n" % command)

	def gpib_send_clr(self):
		self.send_prologix_command("clr")
	

	def gpib_readline(self):
		self.read()
		self.send_prologix_command("read 10")
		time.sleep(0.1)
		i = 0
		while True:
			line = self.read().strip()
			if len(line) > 0:
				print "<<< "+line
				return line
			elif i<10:
				time.sleep(0.1)
				i += 1
			else:
				return ""

	def gpib_readlines(self, count): # FIXME broken ..
		self.read()
		data = []
		time.sleep(0.1)
		self.send_prologix_command("read")
		time.sleep(0.1)
		i = 0
		while i<count:
			try:
				data.append(self.device.readline())
				time.sleep(0.01)
				i += 1
			except:
				time.sleep(0.1)
				pass
		print "receiving loose data ..."
		for i in xrange(10):
			time.sleep(1)
			x = self.read()
			print "got %d bytes ..." % len(x)
		return data

	def command(self, command, read_answer=False):
		self.gpib_send(command)
		if read_answer:
			return self.gpib_readline()
