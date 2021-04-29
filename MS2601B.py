#!/usr/bin/env python
# coding: utf-8
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
import IPython

GPIB_ADDR = 1


class MS2601B:
	"""
	MS2601B remote control via GPIB.
	"""

	# line terminator
	TERMINATORS = {"LF": 0, "CR": 1, "CR/LF": 2}
	TERMINATORS_INV = dict([(b, a) for (a, b) in TERMINATORS.items()])

	# number of points in spectrum data
	SPECTRUM_DATA_POINTS = 501

	# reference level
	REF_LEVEL_MIN = -100  # TODO only works with dBm
	REF_LEVEL_MAX = 20

	# frequency
	SPAN_FREQ_MIN = 0
	SPAN_FREQ_MAX = 2200000000
	MIN_FREQ = 0
	MAX_FREQ = 2200000000

	# marker
	MARKER = {"Normal": 0, "Delta": 1, "Off": 2}
	MARKER_INV = dict([(b, a) for (a, b) in MARKER.items()])

	# marker width
	MARKER_WIDTH = {"Narrow": 0, "Spot": 1, "Wide": 2, "Dip. Narrow": 3, "Dip. Wide": 4}
	MARKER_WIDTH_INV = dict([(b, a) for (a, b) in MARKER_WIDTH.items()])

	# marker search
	MARKER_SEARCH = {
		"Peak": 0,
		"Next peak": 1,
		"Minimum": 2,
		"Left peak": 3,
		"Center peak": 4,
		"Right peak": 5,
		"Left minimum": 6,
		"Center minimum": 7,
		"Right minimum": 8
	}

	# calibration modes
	CAL_MODES = {"ALL": 0, "FREQ": 1, "LEVEL (1)": 2, "LEVEL (2)": 3}
	CAL_MODES_INV = dict([(b, a) for (a, b) in CAL_MODES.items()])

	# scales
	SCALE = {"1 dB": 0, "2 dB": 1, "5 dB": 2, "10 dB": 3, "Linear": 4}
	SCALE_INV = dict([(b, a) for (a, b) in SCALE.items()])

	# units
	UNITS = {'dBm': 0, 'dBµV': 1, 'dBV': 2, 'V': 3, 'dBµV (emf)': 4, 'dBµV/m': 5}
	UNITS_INV = dict([(b, a) for (a, b) in UNITS.items()])

	# reference line
	REF_LINE = {"Top": 0, "Middle": 1, "Bottom": 2}
	REF_LINE_INV = dict([(b, a) for (a, b) in REF_LINE.items()])

	# resolution bandwidth
	RES_BW = {
		"30 Hz": 0,
		"100 Hz": 1,
		"300 Hz": 2,
		"1 kHz": 3,
		"3 kHz": 4,
		"10 kHz": 5,
		"30 kHz": 6,
		"100 kHz": 7,
		"300 kHz": 8,
		"1 MHz": 9,
		"200 Hz": 10,
		"9 kHz": 11,
		"120 kHz": 12
	}
	RES_BW_INV = dict([(b, a) for (a, b) in RES_BW.items()])

	# attenuation
	ATTEN = {"0 dB": 0, "10 dB": 1, "20 dB": 2, "30 dB": 3, "40 dB": 4, "50 dB": 5}
	ATTEN_INV = dict([(b, a) for (a, b) in ATTEN.items()])

	# sweep time
	SWEEP_TIME = {
		"1000 s": 1e6,
		"700 s": 7e5,
		"500 s": 5e5,
		"300 s": 3e5,
		"200 s": 2e5,
		"150 s": 1.5e5,
		"100 s": 1e5,
		"70 s": 7e4,
		"50 s": 5e4,
		"30 s": 3e4,
		"20 s": 2e4,
		"15 s": 1.5e4,
		"10 s": 1e4,
		"7 s": 7000,
		"5 s": 5000,
		"3 s": 3000,
		"2 s": 2000,
		"1.5 s": 1500,
		"1 s": 1000,
		"700 ms": 700,
		"500 ms": 500,
		"300 ms": 300,
		"200 ms": 200,
		"150 ms": 150,
		"100 ms": 100,
		"70 ms": 70,
		"50 ms": 50
	}
	SWEEP_TIME_INV = dict([(b, a) for (a, b) in SWEEP_TIME.items()])

	# video bandwidth
	VIDEO_BW = {"1 Hz": 0, "10 Hz": 1, "100 Hz": 2, "1 kHz": 3, "10 kHz": 4, "100 kHz": 5, "OFF": 6}
	VIDEO_BW_INV = dict([(b, a) for (a, b) in VIDEO_BW.items()])

	# antennas
	ANTENNAS = {"DIPOLE": 0, "LOG-PERIODIC (1)": 1, "LOG-PERIODIC (2)": 2, "LOOP": 3, "USER": 4, "OFF": 5}
	ANTENNAS_INV = dict([(b, a) for (a, b) in ANTENNAS.items()])

	# trigger types
	TRIGGER_TYPES = {"FREE": 0, "VIDEO": 1, "LINE": 2, "EXT": 3, "SINGLE": 4, "START": 5}
	TRIGGER_TYPES_INV = dict([(b, a) for (a, b) in TRIGGER_TYPES.items()])

	# frequency counter resolutions
	FREQ_COUNT_RES = {"1 Hz": 0, "10 Hz": 1, "100 Hz": 2}
	FREQ_COUNT_RES_INV = dict([(b, a) for (a, b) in FREQ_COUNT_RES.items()])

	# write modes
	WRITE_MODES = {"Normal": 0, "Max hold": 1, "Average": 2, "Min hold": 3, "Cumulative": 4, "Overwrite": 5}
	WRITE_MODES_INV = dict([(b, a) for (a, b) in WRITE_MODES.items()])

	# average rates
	AVERAGE_RATES = {"4": 0, "8": 1, "16": 2, "32": 3, "128": 4}
	AVERAGE_RATES_INV = dict([(b, a) for (a, b) in AVERAGE_RATES.items()])

	# A - B mode
	A_MINUS_B_MODES = {"Off": 0, u"A-B → A": 1, u"A-SA → A": 2, u"B-SB → B": 3}
	A_MINUS_B_MODES_INV = dict([(b, a) for (a, b) in A_MINUS_B_MODES.items()])

	# det modes
	DET_MODES = {"Peak": 0, "Sample": 1, "Dip": 2}
	DET_MODES_INV = dict([(b, a) for (a, b) in DET_MODES.items()])

	def __init__(self):
		self.gpib = PrologixGPIB.PrologixGPIB(GPIB_ADDR)
		self.set_all_values_dirty()

	def set_all_values_dirty(self):
		self.binary_dirty = True
		self.center_freq_dirty = True
		self.start_freq_dirty = True
		self.span_dirty = True
		self.zone_sweep_dirty = True
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
		self.freq_count_enabled_dirty = True
		self.freq_count_resolution_dirty = True
		self.a_read_dirty = True
		self.a_write_dirty = True
		self.a_write_mode_dirty = True
		self.b_read_dirty = True
		self.b_write_dirty = True
		self.b_write_mode_dirty = True
		self.average_rate_dirty = True
		self.a_minus_b_mode_dirty = True
		self.det_mode_dirty = True
		self.reference_line_dirty = True
		self.quasi_peak_dirty = True

	def send(self, command):
		self.gpib.gpib_send(command)

	def recv(self):
		return self.gpib.gpib_readline()

	def command(self, command, read_answer=False):
		return self.gpib.command(command, read_answer)

	def get_int_value(self, command):
		answer = self.command(command + "?", read_answer=True)
		return int(answer.split(" ")[-1])

	def set_int_value(self, command, value):
		self.command("%s %d" % (command, value))

	def get_float_value(self, command):
		answer = self.command(command + "?", read_answer=True)
		return float(answer.split(" ")[-1])

	def set_float_value(self, command, value):
		self.command("%s %1.1f" % (command, value))

	def set_terminator(self, terminator):
		assert terminator in list(self.TERMINATORS.keys())
		self.set_int_value("TRM", self.TERMINATORS[terminator])

	def set_initial(self):
		self.send("INI")
		time.sleep(0.5)
		self.binary = False
		self.binary_dirty = False
		self.center_freq = self.MAX_FREQ / 2
		self.center_freq_dirty = False
		self.start_freq = self.MIN_FREQ
		self.start_freq_dirty = False
		self.span = self.SPAN_FREQ_MAX
		self.span_dirty = False
		self.zone_sweep = False
		self.zone_sweep_dirty = False
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
		self.freq_count_enabled = False
		self.freq_count_enabled_dirty = False
		self.freq_count_resolution = "10 Hz"
		self.freq_count_resolution_dirty = False
		self.a_read = True
		self.a_read_dirty = False
		self.a_write = 1
		self.a_write_dirty = False
		self.a_write_mode = "NORMAL"
		self.a_write_mode_dirty = False
		self.b_read = False
		self.b_read_dirty = False
		self.b_write = 0
		self.b_write_dirty = False
		self.b_write_mode = "NORMAL"
		self.b_write_mode_dirty = False
		self.average_rate = "8"
		self.average_rate_dirty = False
		self.a_minus_b_mode = "Off"
		self.a_minus_b_mode_dirty = False
		self.det_mode = "Peak"
		self.det_mode_dirty = False
		self.reference_line = "Middle"
		self.reference_line_dirty = False
		self.quasi_peak = False
		self.quasi_peak_dirty = False

	def get_spectrum_data(self, channel, start_address=0, count=SPECTRUM_DATA_POINTS, binary=False):
		channel = channel.upper()
		assert start_address >= 0 and start_address <= 500
		assert start_address + count - 1 <= 500
		assert channel == "A" or channel == "B"
		if channel == "A":
			self.set_channel_a_write(0)
		else:
			self.set_channel_b_write(0)
		self.set_binary(binary)
		self.send("XM%c? %d,%d" % (channel, start_address, count))
		if not binary:
			# note: for some reason, we get additional newlines (every second
			# line), so currently we get twice the expected data points and
			# ignore all empty (newline only) lines
			data = self.gpib.gpib_readlines(count * 2)
			data = [line.decode('ascii') for line in data]
			values = [float(value.strip().replace(" ", "")) for value in data if value.strip() != '']
		else:
			values = []
		return values

	def get_binary(self):
		if self.binary_dirty:
			self.binary = bool(self.get_int_value("BIN"))
			self.binary_dirty = False
		return self.binary

	def set_binary(self, binary):
		self.binary = binary
		self.binary_dirty = False
		self.set_int_value("BIN", int(binary))

	#
	# level
	#

	def get_reference_level(self):
		if self.ref_level_dirty:
			self.ref_level = self.get_float_value("RLV")
			self.ref_level_dirty = False
		return self.ref_level

	def set_reference_level(self, ref_level):
		self.ref_level = ref_level
		self.atten_dirty = True
		self.set_float_value("RLV", ref_level)

	def peak_to_reference_level(self):
		self.send("PRL")
		self.ref_level_dirty = True

	#
	# frequency
	#

	def get_center_frequency(self):
		if self.center_freq_dirty:
			self.center_freq = self.get_int_value("CNF")
			self.center_freq_dirty = False
		return self.center_freq

	def set_center_frequency(self, center_freq):
		assert center_freq >= self.MIN_FREQ and center_freq <= self.MAX_FREQ
		self.center_freq = center_freq
		self.center_freq_dirty = False
		self.start_freq_dirty = True
		self.span_dirty = True
		self.set_int_value("CNF", center_freq)

	def peak_to_center_frequency(self):
		self.send("PCF")
		self.center_freq_dirty = True
		self.start_freq_dirty = True
		self.span_dirty = True

	def get_start_frequency(self):
		if self.start_freq_dirty:
			self.start_freq = self.get_int_value("STF")
			self.start_freq_dirty = False
		return self.start_freq

	def set_start_frequency(self, start_freq):
		assert start_freq >= self.MIN_FREQ and start_freq <= self.MAX_FREQ
		self.start_freq = start_freq
		self.start_freq_dirty = False
		self.center_freq_dirty = True
		self.span_dirty = True
		self.set_int_value("STF", start_freq)

	def get_stop_frequency(self):
		return self.get_start_frequency() + self.get_span()

	def set_stop_frequency(self, stop_freq):
		assert stop_freq >= self.MIN_FREQ and stop_freq <= self.MAX_FREQ
		start_freq = self.get_start_frequency()
		assert stop_freq >= start_freq
		span = stop_freq - start_freq
		self.set_span(span)
		self.set_start_frequency(start_freq)

	def get_span(self):
		if self.span_dirty:
			self.span = self.get_int_value("SPF")
			self.span_dirty = False
		return self.span

	def set_span(self, span):
		assert span >= self.SPAN_FREQ_MIN and span <= self.SPAN_FREQ_MAX
		self.span = span
		self.span_dirty = False
		self.center_freq_dirty = True
		self.start_freq_dirty = True
		self.set_int_value("SPF", span)

	#
	# marker
	#

	def get_marker(self):
		return self.MARKER_INV[self.get_int_value("MKR")]

	def set_marker(self, marker):
		self.set_int_value("MKR", self.MARKER[marker])

	def marker_to_cf(self):
		self.set_int_value("MKR", 3)

	def marker_to_ref(self):
		self.set_int_value("MKR", 4)

	def get_marker_width(self):
		return self.MARKER_WIDTH_INV[self.get_int_value("MKW")]

	def set_marker_width(self, width):
		self.set_int_value("MKW", self.MARKER_WIDTH[width])

	def marker_search(self, search_mode):
		self.set_int_value("MKS", self.MARKER_SEARCH[search_mode])

	# zone sweep

	def get_zone_sweep(self):
		if self.zone_sweep_dirty:
			self.zone_sweep = bool(self.get_int_value("PSW"))
			self.zone_sweep_dirty = False
		return self.zone_sweep

	def set_zone_sweep(self, enabled):
		self.zone_sweep = enabled
		self.zone_sweep_dirty = False
		self.set_int_value("PSW", int(enabled))

	#
	# resolution bandwidth
	#

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

	#
	# attenuation
	#

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

	#
	# sweep time
	#

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

	#
	# video bandwidth
	#

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

	#
	# uncal
	#

	def get_uncal_status(self):
		self.uncal = bool(self.get_int_value("UCL"))
		return self.uncal

	#
	# scale
	#

	def get_scale(self):
		if self.scale_dirty:
			self.scale = self.SCALE_INV[self.get_int_value("SCL")]
			self.scale_dirty = False
		return self.scale

	def set_scale(self, scale):
		self.scale = scale
		self.scale_dirty = False
		self.set_int_value("SCL", self.SCALE[scale])

	#
	# unit
	#

	def get_unit(self):
		if self.unit_dirty:
			self.unit = self.UNITS_INV[self.get_int_value("UNT")]
			self.unit_dirty = False
		return self.unit

	def set_unit(self, unit):
		self.unit = unit
		self.unit_dirty = False
		self.set_int_value("UNT", self.UNITS[unit])

	#
	# reference line
	#

	def get_reference_line(self):
		if self.reference_line_dirty:
			self.reference_line = self.REF_LINE_INV[self.get_int_value("RLN")]
			self.reference_line_dirty = False
		return self.reference_line

	def set_reference_line(self, position):
		self.reference_line = position
		self.reference_line_dirty = False
		self.set_int_value("RLN", self.REF_LINE[position])

	#
	# antenna
	#

	def get_antenna(self):
		if self.antenna_dirty:
			self.antenna = self.ANTENNAS_INV[self.get_int_value("ANT")]
			self.antenna_dirty = False
		return self.antenna

	def set_antenna(self, antenna):
		self.antenna = antenna
		self.antenna_dirty = False
		self.set_int_value("ANT", self.ANTENNAS[antenna])

	#
	# trigger / sweep
	#

	def get_trigger(self):
		if self.trigger_dirty:
			self.trigger = self.TRIGGER_TYPES_INV[self.get_int_value("TRG")]
			self.trigger_dirty = False
		return self.trigger

	def set_trigger(self, trigger):
		self.trigger = trigger
		self.trigger_dirty = False
		self.set_int_value("TRG", self.TRIGGER_TYPES[trigger])

	def sweep(self):
		self.send("SWP")

	#
	# calibration
	#

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

	#
	# frequency counter
	#

	def get_frequency_count_enabled(self):
		if self.freq_count_enabled_dirty:
			self.freq_count_enabled = bool(self.get_int_value("MKC"))
			self.freq_count_enabled_dirty = False
		return self.freq_count_enabled

	def set_frequency_count_enabled(self, enabled):
		self.freq_count_enabled = enabled
		self.freq_count_enabled_dirty = False
		self.set_int_value("MKC", int(enabled))

	def get_frequency_count_resolution(self):
		if self.freq_count_resolution_dirty:
			self.freq_count_resolution = self.FREQ_COUNT_RES_INV[self.get_int_value("CRE")]
			self.freq_count_resolution_dirty = False
		return self.freq_count_resolution

	def set_frequency_count_resolution(self, resolution):
		self.set_int_value("CRE", self.FREQ_COUNT_RES[resolution])
		self.freq_count_resolution = resolution
		self.freq_count_enabled_dirty = False

	#
	# trace
	#

	# channel a

	def get_channel_a_read(self):
		if self.a_read_dirty:
			self.a_read = bool(self.get_int_value("ARD"))
			self.a_read_dirty = False
		return self.a_read

	def set_channel_a_read(self, enabled):
		self.a_read = enabled
		self.a_read_dirty = False
		self.a_write_dirty = True
		self.set_int_value("ARD", int(enabled))

	def get_channel_a_write(self):
		if self.a_write_dirty:
			self.a_write = self.get_int_value("AWR")
			self.a_write_dirty = False
		return self.a_write

	def set_channel_a_write(self, mode):
		self.a_write = mode
		self.a_write_dirty = False
		self.a_read_dirty = True
		self.set_int_value("AWR", mode)

	def get_channel_a_write_mode(self):
		if self.a_write_mode_dirty:
			self.a_write_mode = self.WRITE_MODES_INV[self.get_int_value("AMD")]
			self.a_write_mode_dirty = False
		return self.a_write_mode

	def set_channel_a_write_mode(self, mode):
		self.a_write_mode = mode
		self.a_write_mode_dirty = False
		self.set_int_value("AMD", self.WRITE_MODES[mode])

	# channel b

	def get_channel_b_read(self):
		if self.b_read_dirty:
			self.b_read = bool(self.get_int_value("BRD"))
			self.b_read_dirty = False
		return self.b_read

	def set_channel_b_read(self, enabled):
		self.b_read = enabled
		self.b_read_dirty = False
		self.b_write_dirty = True
		self.set_int_value("BRD", int(enabled))

	def get_channel_b_write(self):
		if self.b_write_dirty:
			self.b_write = self.get_int_value("BWR")
			self.b_write_dirty = False
		return self.b_write

	def set_channel_b_write(self, mode):
		self.b_write = mode
		self.b_write_dirty = False
		self.b_read_dirty = True
		self.set_int_value("BWR", mode)

	def get_channel_b_write_mode(self):
		if self.b_write_mode_dirty:
			self.b_write_mode = self.WRITE_MODES_INV[self.get_int_value("BMD")]
			self.b_write_mode_dirty = False
		return self.b_write_mode

	def set_channel_b_write_mode(self, mode):
		self.b_write_mode = mode
		self.b_write_mode_dirty = False
		self.set_int_value("BMD", self.WRITE_MODES[mode])

	# average rate

	def get_average_rate(self):
		if self.average_rate_dirty:
			self.average_rate = self.AVERAGE_RATES_INV[self.get_int_value("AVR")]
			self.average_rate_dirty = False
		return self.average_rate

	def set_average_rate(self, rate):
		self.average_rate = rate
		self.average_rate_dirty = False
		self.set_int_value("AVR", self.AVERAGE_RATES[rate])

	# A to B

	def a_to_b(self):
		self.send("ATB")

	# A - B mode

	def get_a_minus_b_mode(self):
		if self.a_minus_b_mode_dirty:
			self.a_minus_b_mode = self.A_MINUS_B_MODES_INV[self.get_int_value("AMB")]
			self.a_minus_b_mode_dirty = False
		return self.a_minus_b_mode

	def set_a_minus_b_mode(self, mode):
		self.a_minus_b_mode = mode
		self.a_minus_b_mode_dirty = False
		self.set_int_value("AMB", self.A_MINUS_B_MODES[mode])

	# det mode

	def get_det_mode(self):
		if self.det_mode_dirty:
			self.det_mode = self.DET_MODES_INV[self.get_int_value("DET")]
			self.det_mode_dirty = False
		return self.det_mode

	def set_det_mode(self, mode):
		self.det_mode = mode
		self.det_mode_dirty = False
		self.set_int_value("DET", self.DET_MODES[mode])

	#
	# quasi-peak detection
	#

	def get_quasi_peak_enabled(self):
		if self.quasi_peak_dirty:
			self.quasi_peak = bool(self.get_int_value("QPD"))
			self.quasi_peak_dirty = False
		return self.quasi_peak

	def set_quasi_peak_enabled(self, enabled):
		self.quasi_peak = enabled
		self.quasi_peak_dirty = True  # setting may fail
		self.set_int_value("QPD", int(enabled))

	#
	# list
	#

	def set_list(self, reg):
		assert reg >= 0 and reg <= 2
		self.set_int_value("LST", reg)


if __name__ == "__main__":
	ms2601b = MS2601B()
	IPython.embed()
