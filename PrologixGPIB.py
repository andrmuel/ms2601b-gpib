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
		print "OUT: "+string
		self.device.write(string)

	def read(self):
		data = []
		time.sleep(0.1)
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
	
	def gpib_send(self, command):
		self.write("%s\n" % command)

	def gpib_send_clr(self):
		self.send_prologix_command("clr")
	
	def gpib_send_loc(self):
		"""
		Enable front panel operation of the currently addressed instrument.
		"""
		self.send_prologix_command("loc")

	def gpib_readline(self):
		self.read()
		self.send_prologix_command("read 10")
		return self.read().strip()

	def command(self, command):
		self.gpib_send(command)
		return self.gpib_readline()