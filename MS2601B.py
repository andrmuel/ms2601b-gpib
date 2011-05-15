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

import time

import PrologixGPIB
import code
from IPython.Shell import IPShellEmbed

GPIB_ADDR=1

	
class MS2601B:
	"""
	MS2601B remote control via GPIB.
	"""

	# reference level
	REF_LEVEL_MIN = -100 # TODO only works with dBm
	REF_LEVEL_MAX = 20

	# calibration modes
	CAL_MODES = {"ALL": 0, "FREQ": 1, "LEVEL (1)": 2, "LEVEL (2)": 3}
	CAL_MODES_INV =  dict([(b,a) for (a,b) in CAL_MODES.iteritems()])

	# scales
	SCALE = { "1 dB": 0, "2 dB": 1, "5 dB": 2, "10 dB": 3, "Linear": 4}
	SCALE_INV = dict([(b,a) for (a,b) in SCALE.iteritems()])

	# units
	UNITS = {"dBm": 0, "dBµV": 1, "dBV": 2, "V": 3, "dBµV (emf)": 4, "dBµV/m": 5}
	UNITS_INV = dict([(b,a) for (a,b) in UNITS.iteritems()])

	# resolution bandwidth
	RES_BW = {"30 Hz": 0, "100 Hz": 1, "300 Hz": 2, "1 kHz": 3, "3 kHz": 4, "10 kHz": 5, "30 kHz": 6, "100 kHz": 7, "300 kHz": 8, "1 MHz": 9, "200 Hz": 10, "9 kHz": 11, "120 kHz": 12}
	RES_BW_INV = dict([(b,a) for (a,b) in RES_BW.iteritems()])

	# attenuation
	ATTEN = {"0 dB": 0, "10 dB": 1, "20 dB": 2, "30 dB": 3, "40 dB": 4, "50 dB": 5}
	ATTEN_INV = dict([(b,a) for (a,b) in ATTEN.iteritems()])

	# sweep time
	SWEEP_TIME = {"1000 s": 1e6, "700 s": 7e5, "500 s": 5e5, "300 s": 3e5, "200 s": 2e5, "150 s": 1.5e5, "100 s": 1e5, "70 s": 7e4, "50 s": 5e4, "30 s": 3e4, "20 s": 2e4, "15 s": 1.5e4, "10 s": 1e4, "7 s": 7000, "5 s": 5000, "3 s": 3000, "2 s": 2000, "1.5 s": 1500, "1 s": 1000, "700 ms": 700, "500 ms": 500, "300 ms": 300, "200 ms": 200, "150 ms": 150, "100 ms": 100, "70 ms": 70, "50 ms": 50}
	SWEEP_TIME_INV = dict([(b,a) for (a,b) in SWEEP_TIME.iteritems()])

	# video bandwidth
	VIDEO_BW = {"1 Hz": 0, "10 Hz": 1, "100 Hz": 2, "1 kHz": 3, "10 kHz": 4, "100 kHz": 5, "OFF": 6}
	VIDEO_BW_INV = dict([(b,a) for (a,b) in VIDEO_BW.iteritems()])

	# antennas
	ANTENNAS = {"DIPOLE": 0, "LOG-PERIODIC (1)": 1, "LOG-PERIODIC (2)": 2, "LOOP": 3, "USER": 4, "OFF": 5}
	ANTENNAS_INV = dict([(b,a) for (a,b) in ANTENNAS.iteritems()])

	# trigger types
	TRIGGER_TYPES = {"FREE": 0, "VIDEO": 1, "LINE": 2, "EXT": 3, "SINGLE": 4, "START": 5}
	TRIGGER_TYPES_INV = dict([(b,a) for (a,b) in TRIGGER_TYPES.iteritems()])

	def __init__(self):
		self.gpib = PrologixGPIB.PrologixGPIB(GPIB_ADDR)
		self.ref_level_dirty = True
		self.res_bw_dirty = True
		self.res_bw_auto_dirty = True
		self.atten_dirty = True
		self.atten_auto_dirty = True
		self.sweep_time_dirty = True
		self.sweep_time_auto_dirty = True
		self.video_bw_dirty = True
		self.video_bw_auto_dirty = True
		self.scale_dirty = True
		self.unit_dirty = True
		self.antenna_dirty = True
		self.trigger_dirty = True
		self.correction_data_dirty = True
		self.response_data_dirty = True

	def send(self, command):
		self.gpib.gpib_send(command)

	def recv(self):
		return self.gpib.gpib_readline()

	def command(self, command, read_answer=False):
		return self.gpib.command(command, read_answer)

	def get_int_value(self, command):
		answer = self.command(command+"?", read_answer=True)
		return int(answer.split(" ")[-1])

	def set_int_value(self, command, value):
		self.command("%s %d" % (command, value))

	def get_float_value(self, command):
		answer = self.command(command+"?", read_answer=True)
		return float(answer.split(" ")[-1])

	def set_float_value(self, command, value):
		self.command("%s %1.1f" % (command, value))
	
	def set_initial(self):
		self.send("INI")
		time.sleep(0.5)
		self.ref_level = 0
		self.ref_level_dirty = False
		self.res_bw_auto = True
		self.res_bw_auto_dirty = False
		self.res_bw = "1 MHz"
		self.res_bw_dirty = False
		self.atten_auto = True
		self.atten_auto_dirty = False
		self.atten = "20 dB"
		self.atten_dirty = False
		self.sweep_time_auto = True
		self.sweep_time_auto_dirty = False
		self.sweep_time = "70 ms"
		self.sweep_time_dirty = False
		self.video_bw_auto = True
		self.video_bw_auto_dirty = False
		self.video_bw = "100 kHz"
		self.video_bw_dirty = False
		self.scale = "10 dB"
		self.scale_dirty = False
		self.antenna = "OFF"
		self.antenna_dirty = False
		self.trigger = "FREE"
		self.trigger_dirty = False
		self.correction_data = True
		self.correction_data_dirty = False
		self.response_data = True
		self.response_data_dirty = False

	def get_reference_level(self):
		if self.ref_level_dirty:
			self.ref_level = self.get_float_value("RLV")
			self.ref_level_dirty = False
		return self.ref_level

	def set_reference_level(self, ref_level):
		self.ref_level = ref_level
		self.set_float_value("RLV", ref_level)

	def peak_to_reference_level(self):
		self.send("PRL")
		self.ref_level_dirty = True

	def get_center_frequency(self):
		return self.get_int_value("CNF")
	
	def set_center_frequency(self, center_freq):
		self.set_int_value("CNF", center_freq)

	def get_start_frequency(self):
		return self.get_int_value("STF")

	def set_start_frequency(self, start_freq):
		self.set_int_value("STF", start_freq)

	def get_span(self):
		self.span = self.get_int_value("SPF")
		return self.span

	def set_span(self, span):
		self.span = span
		self.set_int_value("SPF", span)

	def get_resolution_bandwidth_auto(self):
		if self.res_bw_auto_dirty:
			self.res_bw_auto = bool(self.get_int_value("ARB"))
			self.res_bw_auto_dirty = False
		return self.res_bw_auto

	def set_resolution_bandwidth_auto(self, auto):
		self.res_bw_auto = auto
		self.res_bw_auto_dirty = False
		self.res_bw_dirty = True
		self.set_int_value("ARB", int(auto))
		if self.get_sweep_time_auto():
			self.sweep_time_dirty = True

	def get_resolution_bandwidth(self):
		if self.res_bw_dirty:
			self.res_bw = self.RES_BW_INV[self.get_int_value("RBW")]
			self.res_bw_dirty = False
		return self.res_bw

	def set_resolution_bandwidth(self, rbw):
		self.res_bw = rbw
		self.res_bw_dirty = False
		self.res_bw_auto = False
		self.set_int_value("RBW", self.RES_BW[rbw])
		if self.get_sweep_time_auto():
			self.sweep_time_dirty = True

	def get_attenuation_auto(self):
		if self.atten_auto_dirty:
			self.atten_auto = bool(self.get_int_value("AAT"))
			self.atten_auto_dirty = False
		return self.atten_auto

	def set_attenuation_auto(self, auto):
		self.atten_auto = auto
		self.atten_auto_dirty = False
		self.atten_dirty = True
		self.set_int_value("AAT", int(auto))

	def get_attenuation(self):
		if self.atten_dirty:
			self.atten = self.ATTEN_INV[self.get_int_value("ATT")]
			self.atten_dirty = False
		return self.atten

	def set_attenuation(self, atten):
		self.atten = atten
		self.atten_dirty = False
		self.atten_auto = False
		self.set_int_value("ATT", self.ATTEN[atten])

	def get_sweep_time_auto(self):
		if self.sweep_time_auto_dirty:
			self.sweep_time_auto = bool(self.get_int_value("AST"))
			self.sweep_time_auto_dirty = False
		return self.sweep_time_auto

	def set_sweep_time_auto(self, auto):
		self.sweep_time_auto = auto
		self.sweep_time_auto_dirty = False
		self.sweep_time_dirty = True
		self.set_int_value("AST", int(auto))

	def get_sweep_time(self):
		if self.sweep_time_dirty:
			self.sweep_time = self.SWEEP_TIME_INV[self.get_int_value("SWT")]
			self.sweep_time_dirty = False
		return self.sweep_time

	def set_sweep_time(self, rbw):
		self.sweep_time = rbw
		self.sweep_time_dirty = False
		self.sweep_time_auto = False
		self.set_int_value("SWT", self.SWEEP_TIME[rbw])

	def get_video_bandwidth_auto(self):
		if self.video_bw_auto_dirty:
			self.video_bw_auto = bool(self.get_int_value("AVB"))
			self.video_bw_auto_dirty = False
		return self.video_bw_auto

	def set_video_bandwidth_auto(self, auto):
		self.video_bw_auto = auto
		self.video_bw_auto_dirty = False
		self.video_bw_dirty = True
		self.set_int_value("AVB", int(auto))
		if self.get_sweep_time_auto():
			self.sweep_time_dirty = True

	def get_video_bandwidth(self):
		if self.video_bw_dirty:
			self.video_bw = self.VIDEO_BW_INV[self.get_int_value("VBW")]
			self.video_bw_dirty = False
		return self.video_bw

	def set_video_bandwidth(self, rbw):
		self.video_bw = rbw
		self.video_bw_dirty = False
		self.video_bw_auto = False
		self.set_int_value("VBW", self.VIDEO_BW[rbw])
		if self.get_sweep_time_auto():
			self.sweep_time_dirty = True

	def get_uncal_status(self):
		self.uncal = bool(self.get_int_value("UCL"))
		return self.uncal

	def get_scale(self):
		if self.scale_dirty:
			self.scale = self.SCALE_INV[self.get_int_value("SCL")]
			self.scale_dirty = False
		return self.scale
		
	def set_scale(self, scale):
		self.scale = scale
		self.scale_dirty = False
		self.set_int_value("SCL", self.SCALE[scale])

	def get_unit(self):
		if self.unit_dirty:
			self.unit = self.UNITS_INV[self.get_int_value("UNT")]
			self.unit_dirty = False
		return self.unit

	def set_unit(self, unit):
		self.unit = unit
		self.unit_dirty = False
		self.set_int_value("UNT", self.UNITS[unit])
	
	def get_antenna(self):
		if self.antenna_dirty:
			self.antenna = self.ANTENNAS_INV[self.get_int_value("ANT")]
			self.antenna_dirty = False
		return self.antenna

	def set_antenna(self, antenna):
		self.antenna = antenna
		self.antenna_dirty = False
		self.set_int_value("ANT", self.ANTENNAS[antenna])

	def sweep(self):
		self.send("SWP")
	
	def get_trigger(self):
		if self.trigger_dirty:
			self.trigger = self.TRIGGER_TYPES_INV[self.get_int_value("TRG")]
			self.trigger_dirty = False
		return self.trigger

	def set_trigger(self, trigger):
		self.trigger = trigger
		self.trigger_dirty = False
		self.set_int_value("TRG", self.TRIGGER_TYPES[trigger])

	def start_calibration(self, mode=0):
		"""
		Start calibration process.
		
		@param mode: 0 -> ALL, 1 -> FREQ, 2 -> CAL LEVEL (1), 3 -> CAL LEVEL (2)
		"""
		if mode in range(4):
			self.set_int_value("CAL", mode)

	def get_correction_data(self):
		if self.correction_data_dirty:
			self.correction_data = bool(self.get_int_value("CDT"))
			self.correction_data_dirty = False
		return self.correction_data

	def set_correction_data(self, enabled):
		self.correction_data = enabled
		self.correction_data_dirty = False
		self.set_int_value("CDT", int(enabled))

	def get_response_data(self):
		if self.response_data_dirty:
			self.response_data = bool(self.get_int_value("CRE"))
			self.response_data_dirty = False
		return self.response_data

	def set_response_data(self, enabled):
		self.response_data = enabled
		self.response_data_dirty = False
		self.set_int_value("CRE", int(enabled))

if __name__ == "__main__":
	ms2601b = MS2601B()
	# interpreter = code.InteractiveConsole(globals())
	# interpreter.interact("Starting Python console  ...")
	ipshell = IPShellEmbed("", banner="Starting IPython ...", exit_msg="Leaving IPython ...")
	ipshell()
