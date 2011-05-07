#!/usr/bin/env python
# coding: utf8
#
# Andreas Müller, 2011
# am@0x7.ch
#
# This code may be freely used and distributed under GNU GPL conditions.

"""
MS2601B remote control via GPIB.
"""

import PrologixGPIB
import code
from IPython.Shell import IPShellEmbed

GPIB_ADDR=1

class MS2601B:
	"""
	MS2601B remote control via GPIB.
	"""

	CAL_MODES = {"ALL": 0, "FREQ": 1, "LEVEL (1)": 2, "LEVEL (2)": 3}
	
	def __init__(self):
		self.gpib = PrologixGPIB.PrologixGPIB(GPIB_ADDR)

	def send(self, command):
		self.gpib.gpib_send(command)

	def command(self, command):
		return self.gpib.command(command)

	def get_value(self, command):
		answer = self.command(command+"?")
		return int(answer.split(" ")[-1])

	def set_value(self, command, value):
		self.command("%s %d" % (command, value))

	def get_center_frequency(self):
		"""
		Get center frequency.
		"""
		return self.get_value("CNF")
	
	def set_center_frequency(self, center_freq):
		"""
		Set center frequency.
		
		@param cnf: frequency in Hz
		"""
		self.set_value("CNF", center_freq)

	def get_start_frequency(self):
		return self.get_value("STF")

	def set_start_frequency(self, start_freq):
		self.set_value("STF", start_freq)

	def get_span(self):
		return self.get_value("SPF")

	def set_span(self, span):
		self.set_value("SPF", span)

	def start_calibration(self, mode=0):
		"""
		Start calibration process.
		
		@param mode: 0 -> ALL, 1 -> FREQ, 2 -> CAL LEVEL (1), 3 -> CAL LEVEL (2)
		"""
		if mode in range(4):
			self.set_value("CAL", mode)

if __name__ == "__main__":
	ms2601b = MS2601B()
	# interpreter = code.InteractiveConsole(globals())
	# interpreter.interact("Starting Python console  ...")
	ipshell = IPShellEmbed("", banner="Starting IPython ...", exit_msg="Leaving IPython ...")
	ipshell()
