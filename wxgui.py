#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sat May  7 23:46:58 2011

import MS2601B
from MenuIDs import *
import wx

# begin wxGlade: extracode
# end wxGlade

class MainFrame(wx.Frame):

	def __init__(self, *args, **kwds):
		# begin wxGlade: MainFrame.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.notebook = wx.Notebook(self, -1, style=0)
		self.notebook_console = wx.Panel(self.notebook, -1)
		self.notebook_main = wx.Panel(self.notebook, -1)
		self.main_settings_panel = wx.Panel(self.notebook_main, -1, style=wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
		self.frequency_ref_level_panel = wx.Panel(self.notebook_main, -1, style=wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
		
		# Menu Bar
		self.menubar = wx.MenuBar()
		wxglade_tmp_menu = wx.Menu()
		wxglade_tmp_menu.Append(MENU_INITIAL, "Initial settings", "", wx.ITEM_NORMAL)
		wxglade_tmp_menu.Append(MENU_LOCAL, "Local control", "", wx.ITEM_NORMAL)
		self.menubar.Append(wxglade_tmp_menu, "Device")
		wxglade_tmp_menu = wx.Menu()
		wxglade_tmp_menu.Append(MENU_SCALE_1DB, "Log 1dB", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_SCALE_2DB, "Log 2dB", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_SCALE_5DB, "Log 5dB", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_SCALE_10DB, "Log 10dB", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_SCALE_LIN, "Lin", "", wx.ITEM_RADIO)
		self.menubar.Append(wxglade_tmp_menu, "Scale")
		wxglade_tmp_menu = wx.Menu()
		wxglade_tmp_menu.Append(MENU_UNIT_DBM, "dBm", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_UNIT_DBUV, u"dBµV", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_UNIT_DBV, "dBV", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_UNIT_V, "V", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_UNIT_DBUV_EMF, u"dBµV (emf)", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_UNIT_DBUV_M, u"dBµV/m", "", wx.ITEM_RADIO)
		self.menubar.Append(wxglade_tmp_menu, "Unit")
		wxglade_tmp_menu = wx.Menu()
		wxglade_tmp_menu.Append(MENU_TRIGGER_FREE, "Free", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_TRIGGER_VIDEO, "Video", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_TRIGGER_LINE, "Line", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_TRIGGER_EXT, "External", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_TRIGGER_SINGLE, "Single", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_TRIGGER_START, "Restart", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.AppendSeparator()
		wxglade_tmp_menu.Append(MENU_TRIGGER_SWEEP, "Sweep", "", wx.ITEM_NORMAL)
		self.menubar.Append(wxglade_tmp_menu, "Trigger")
		wxglade_tmp_menu = wx.Menu()
		wxglade_tmp_menu.Append(MENU_CALIBRATION_ALL, "All", "", wx.ITEM_NORMAL)
		wxglade_tmp_menu.Append(MENU_CALIBRATION_LEVEL_1, "Level (1)", "", wx.ITEM_NORMAL)
		wxglade_tmp_menu.Append(MENU_CALIBRATION_LEVEL_2, "Level (2)", "", wx.ITEM_NORMAL)
		wxglade_tmp_menu.Append(MENU_CALIBRATION_FREQUENCY, "Frequency", "", wx.ITEM_NORMAL)
		wxglade_tmp_menu.AppendSeparator()
		wxglade_tmp_menu.Append(MENU_CALIBRATION_CORRECTION_DATA, "Correction data", "", wx.ITEM_CHECK)
		wxglade_tmp_menu.Append(MENU_CALIBRATION_RESPONSE_DATA, "Response data", "", wx.ITEM_CHECK)
		self.menubar.Append(wxglade_tmp_menu, "Calibration")
		wxglade_tmp_menu = wx.Menu()
		wxglade_tmp_menu.Append(MENU_ANTENNA_OFF, "Off", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_ANTENNA_DIPOLE, "Dipole", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_ANTENNA_LOGPER_1, "Logarithmic periodic (1)", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_ANTENNA_LOGPER_2, "Logarithmic periodic (2)", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_ANTENNA_LOOP, "Loop", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_ANTENNA_USER, "User", "", wx.ITEM_RADIO)
		self.menubar.Append(wxglade_tmp_menu, "Antenna")
		self.SetMenuBar(self.menubar)
		# Menu Bar end
		self.statusbar = self.CreateStatusBar(1, 0)
		self.ref_level_label = wx.StaticText(self.frequency_ref_level_panel, -1, "Reference level")
		self.ref_level_spin_ctrl = wx.SpinCtrl(self.frequency_ref_level_panel, -1, "", min=0, max=100)
		self.peak_to_ref_level_button = wx.Button(self.frequency_ref_level_panel, -1, u"Peak → reference level")
		self.frequency_label = wx.StaticText(self.frequency_ref_level_panel, -1, "Frequency")
		self.center_frequency_label = wx.StaticText(self.frequency_ref_level_panel, -1, "Center frequency")
		self.placeholder_panel_1 = wx.Panel(self.frequency_ref_level_panel, -1)
		self.center_freq_spin_ctrl = wx.SpinCtrl(self.frequency_ref_level_panel, -1, "", min=0, max=100)
		self.peak_to_cf_button = wx.Button(self.frequency_ref_level_panel, -1, u"Peak → center frequency")
		self.span_label = wx.StaticText(self.frequency_ref_level_panel, -1, "Span")
		self.placeholder_panel_2 = wx.Panel(self.frequency_ref_level_panel, -1)
		self.span_spin_ctrl = wx.SpinCtrl(self.frequency_ref_level_panel, -1, "", min=0, max=100)
		self.zero_span_button = wx.Button(self.frequency_ref_level_panel, -1, "Zero span")
		self.start_frequency_label = wx.StaticText(self.frequency_ref_level_panel, -1, "Start frequency")
		self.stop_frequency_label = wx.StaticText(self.frequency_ref_level_panel, -1, "Stop frequency")
		self.start_freq_spin_ctrl = wx.SpinCtrl(self.frequency_ref_level_panel, -1, "", min=0, max=100)
		self.stop_freq_spin_ctrl = wx.SpinCtrl(self.frequency_ref_level_panel, -1, "", min=0, max=100)
		self.res_bw_label = wx.StaticText(self.main_settings_panel, -1, "Resolution bandwidth")
		self.res_bw_auto = wx.RadioBox(self.main_settings_panel, -1, "Auto/Manual", choices=["Auto", "Manual"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
		self.res_bw_select = wx.ComboBox(self.main_settings_panel, -1, choices=["1 MHz", "300 kHz", "100 kHz", "30 kHz", "10 kHz", "3 kHz", "1 kHz", "300 Hz", "100 Hz", "30 Hz"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
		self.atten_label = wx.StaticText(self.main_settings_panel, -1, "Attenuation")
		self.atten_auto = wx.RadioBox(self.main_settings_panel, -1, "Auto/Manual", choices=["Auto", "Manual"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
		self.atten_select = wx.ComboBox(self.main_settings_panel, -1, choices=["50 dB", "40 dB", "30 dB", "20 dB", "10 dB", "0 dB"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
		self.sweep_time_label = wx.StaticText(self.main_settings_panel, -1, "Sweep time")
		self.sweep_time_auto = wx.RadioBox(self.main_settings_panel, -1, "Auto/Manual", choices=["Auto", "Manual"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
		self.sweep_time_select = wx.ComboBox(self.main_settings_panel, -1, choices=["1000 s", "700 s", "500 s", "300 s", "200 s", "150 s", "100 s", "70 s", "50 s", "30 s", "20 s", "15 s", "10 s", "7 s", "5 s", "3 s", "2 s", "1.5 s", "1 s", "700 ms", "500 ms", "300 ms", "200 ms", "150 ms", "100 ms", "70 ms", "50 ms"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
		self.video_bw_label = wx.StaticText(self.main_settings_panel, -1, "Video bandwidth")
		self.video_bw_auto = wx.RadioBox(self.main_settings_panel, -1, "Auto/Manual", choices=["Auto", "Manual"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
		self.video_bw_select = wx.ComboBox(self.main_settings_panel, -1, choices=["-OFF-", "100 kHz", "10 kHz", "1 kHz", "100 Hz", "10 Hz", "1 Hz"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
		self.uncal_label = wx.StaticText(self.main_settings_panel, -1, "Uncalibrated")
		self.panel_1 = wx.Panel(self.notebook_main, -1)
		self.console_output_text_ctrl = wx.TextCtrl(self.notebook_console, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
		self.console_input_text_ctrl = wx.TextCtrl(self.notebook_console, -1, "", style=wx.TE_PROCESS_ENTER)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_MENU, self.menu_handler_initial, id=MENU_INITIAL)
		self.Bind(wx.EVT_MENU, self.menu_handler_local, id=MENU_LOCAL)
		self.Bind(wx.EVT_MENU, self.menu_handler_scale, id=MENU_SCALE_1DB)
		self.Bind(wx.EVT_MENU, self.menu_handler_scale, id=MENU_SCALE_2DB)
		self.Bind(wx.EVT_MENU, self.menu_handler_scale, id=MENU_SCALE_5DB)
		self.Bind(wx.EVT_MENU, self.menu_handler_scale, id=MENU_SCALE_10DB)
		self.Bind(wx.EVT_MENU, self.menu_handler_scale, id=MENU_SCALE_LIN)
		self.Bind(wx.EVT_MENU, self.menu_handler_unit, id=MENU_UNIT_DBM)
		self.Bind(wx.EVT_MENU, self.menu_handler_unit, id=MENU_UNIT_DBUV)
		self.Bind(wx.EVT_MENU, self.menu_handler_unit, id=MENU_UNIT_DBV)
		self.Bind(wx.EVT_MENU, self.menu_handler_unit, id=MENU_UNIT_V)
		self.Bind(wx.EVT_MENU, self.menu_handler_unit, id=MENU_UNIT_DBUV_EMF)
		self.Bind(wx.EVT_MENU, self.menu_handler_unit, id=MENU_UNIT_DBUV_M)
		self.Bind(wx.EVT_MENU, self.menu_handler_trigger, id=MENU_TRIGGER_FREE)
		self.Bind(wx.EVT_MENU, self.menu_handler_trigger, id=MENU_TRIGGER_VIDEO)
		self.Bind(wx.EVT_MENU, self.menu_handler_trigger, id=MENU_TRIGGER_LINE)
		self.Bind(wx.EVT_MENU, self.menu_handler_trigger, id=MENU_TRIGGER_EXT)
		self.Bind(wx.EVT_MENU, self.menu_handler_trigger, id=MENU_TRIGGER_SINGLE)
		self.Bind(wx.EVT_MENU, self.menu_handler_trigger, id=MENU_TRIGGER_START)
		self.Bind(wx.EVT_MENU, self.menu_handler_trigger_sweep, id=MENU_TRIGGER_SWEEP)
		self.Bind(wx.EVT_MENU, self.menu_handler_calibrate_all, id=MENU_CALIBRATION_ALL)
		self.Bind(wx.EVT_MENU, self.menu_handler_calibrate_level_1, id=MENU_CALIBRATION_LEVEL_1)
		self.Bind(wx.EVT_MENU, self.menu_handler_calibrate_level_2, id=MENU_CALIBRATION_LEVEL_2)
		self.Bind(wx.EVT_MENU, self.menu_handler_calibrate_frequency, id=MENU_CALIBRATION_FREQUENCY)
		self.Bind(wx.EVT_MENU, self.menu_handler_calibration_correction_data, id=MENU_CALIBRATION_CORRECTION_DATA)
		self.Bind(wx.EVT_MENU, self.menu_handler_calibration_response_data, id=MENU_CALIBRATION_RESPONSE_DATA)
		self.Bind(wx.EVT_MENU, self.menu_handler_antenna, id=MENU_ANTENNA_OFF)
		self.Bind(wx.EVT_MENU, self.menu_handler_antenna, id=MENU_ANTENNA_DIPOLE)
		self.Bind(wx.EVT_MENU, self.menu_handler_antenna, id=MENU_ANTENNA_LOGPER_1)
		self.Bind(wx.EVT_MENU, self.menu_handler_antenna, id=MENU_ANTENNA_LOGPER_2)
		self.Bind(wx.EVT_MENU, self.menu_handler_antenna, id=MENU_ANTENNA_LOOP)
		self.Bind(wx.EVT_MENU, self.menu_handler_antenna, id=MENU_ANTENNA_USER)
		self.Bind(wx.EVT_SPINCTRL, self.spinctrl_handler_ref_level, self.ref_level_spin_ctrl)
		self.Bind(wx.EVT_BUTTON, self.button_handler_peak_to_ref_level, self.peak_to_ref_level_button)
		self.Bind(wx.EVT_SPINCTRL, self.spinctrl_handler_center_freq, self.center_freq_spin_ctrl)
		self.Bind(wx.EVT_BUTTON, self.button_handler_peak_to_center_freq, self.peak_to_cf_button)
		self.Bind(wx.EVT_SPINCTRL, self.spinctrl_handler_span, self.span_spin_ctrl)
		self.Bind(wx.EVT_BUTTON, self.button_handler_zero_span, self.zero_span_button)
		self.Bind(wx.EVT_SPINCTRL, self.spinctrl_handler_start_freq, self.start_freq_spin_ctrl)
		self.Bind(wx.EVT_SPINCTRL, self.spinctrl_handler_stop_freq, self.stop_freq_spin_ctrl)
		self.Bind(wx.EVT_RADIOBOX, self.res_bw_auto_handler, self.res_bw_auto)
		self.Bind(wx.EVT_COMBOBOX, self.res_bw_select_handler, self.res_bw_select)
		self.Bind(wx.EVT_RADIOBOX, self.atten_auto_handler, self.atten_auto)
		self.Bind(wx.EVT_COMBOBOX, self.atten_select_handler, self.atten_select)
		self.Bind(wx.EVT_RADIOBOX, self.sweep_time_auto_handler, self.sweep_time_auto)
		self.Bind(wx.EVT_COMBOBOX, self.sweep_time_select_handler, self.sweep_time_select)
		self.Bind(wx.EVT_RADIOBOX, self.video_bw_auto_handler, self.video_bw_auto)
		self.Bind(wx.EVT_COMBOBOX, self.video_bw_select_handler, self.video_bw_select)
		self.Bind(wx.EVT_TEXT_ENTER, self.console_input_enter_event, self.console_input_text_ctrl)
		# end wxGlade
		
		# create MS2601B instance
		self.ms2601b = MS2601B.MS2601B()
		# update reference level value
		self.ref_level_spin_ctrl.SetRange(self.ms2601b.REF_LEVEL_MIN, self.ms2601b.REF_LEVEL_MAX)
		self.update_reference_level()
		# update main settings with actual values
		self.update_res_bw_atten_sweep_time_video_bw()
		# set scale menu correctly
		self.SCALE_TO_MENUITEM_ID = {"1 dB": MENU_SCALE_1DB, "2 dB": MENU_SCALE_2DB, "5 dB": MENU_SCALE_5DB, "10 dB": MENU_SCALE_10DB, "Linear": MENU_SCALE_LIN }
		self.MENUITEM_ID_TO_SCALE = dict([(b,a) for (a,b) in self.SCALE_TO_MENUITEM_ID.iteritems()])
		self.update_scale_menu()
		# set unit menu correctly
		self.UNIT_TO_MENUITEM_ID = {"dBm": MENU_UNIT_DBM, "dBµV": MENU_UNIT_DBUV, "dBV": MENU_UNIT_DBV, "V": MENU_UNIT_V, "dBµV (emf)": MENU_UNIT_DBUV_EMF, "dBµV/m": MENU_UNIT_DBUV_M}
		self.MENUITEM_ID_TO_UNIT = dict([(b,a) for (a,b) in self.UNIT_TO_MENUITEM_ID.iteritems()])
		self.update_unit_menu()
		# set antenna menu correctly
		self.ANTENNA_TO_MENUITEM_ID = {"DIPOLE": MENU_ANTENNA_DIPOLE, "LOG-PERIODIC (1)": MENU_ANTENNA_LOGPER_1, "LOG-PERIODIC (2)": MENU_ANTENNA_LOGPER_2, "LOOP": MENU_ANTENNA_LOOP, "USER": MENU_ANTENNA_USER, "OFF": MENU_ANTENNA_OFF}
		self.MENUITEM_ID_TO_ANTENNA = dict([(b,a) for (a,b) in self.ANTENNA_TO_MENUITEM_ID.iteritems()])
		self.update_antenna_menu()
		# set up trigger menu correctly
		self.TRIGGER_TYPE_TO_MENUITEM_ID = {"FREE": MENU_TRIGGER_FREE, "VIDEO": MENU_TRIGGER_VIDEO, "LINE": MENU_TRIGGER_LINE, "EXT": MENU_TRIGGER_EXT, "SINGLE": MENU_TRIGGER_SINGLE, "START": MENU_TRIGGER_START}
		self.MENUITEM_ID_TO_TRIGGER_TYPE = dict([(b,a) for (a,b) in self.TRIGGER_TYPE_TO_MENUITEM_ID.iteritems()])
		self.update_trigger_menu()
		# set up calibration menu correctly
		self.update_calibration_menu()

	def __set_properties(self):
		# begin wxGlade: MainFrame.__set_properties
		self.SetTitle("MS2601B GPIB control")
		self.statusbar.SetStatusWidths([-1])
		# statusbar fields
		statusbar_fields = [""]
		for i in range(len(statusbar_fields)):
		    self.statusbar.SetStatusText(statusbar_fields[i], i)
		self.ref_level_label.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.ref_level_spin_ctrl.SetMinSize((100, 27))
		self.frequency_label.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.center_freq_spin_ctrl.SetMinSize((100, 27))
		self.span_spin_ctrl.SetMinSize((100, 27))
		self.start_freq_spin_ctrl.SetMinSize((100, 27))
		self.stop_freq_spin_ctrl.SetMinSize((100, 27))
		self.res_bw_label.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.res_bw_auto.SetSelection(0)
		self.res_bw_select.SetSelection(-1)
		self.atten_label.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.atten_auto.SetSelection(0)
		self.atten_select.SetSelection(-1)
		self.sweep_time_label.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.sweep_time_auto.SetSelection(0)
		self.sweep_time_select.SetSelection(-1)
		self.video_bw_label.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.video_bw_auto.SetSelection(0)
		self.video_bw_select.SetSelection(-1)
		self.uncal_label.SetForegroundColour(wx.Colour(255, 0, 0))
		self.uncal_label.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MainFrame.__do_layout
		sizer = wx.BoxSizer(wx.VERTICAL)
		console_sizer = wx.FlexGridSizer(2, 1, 0, 0)
		main_sizer = wx.FlexGridSizer(2, 2, 0, 0)
		main_settings_sizer = wx.FlexGridSizer(5, 1, 0, 0)
		video_bw_sizer = wx.FlexGridSizer(2, 1, 0, 0)
		video_bw_subsizer = wx.FlexGridSizer(1, 2, 0, 0)
		sweep_time_sizer = wx.FlexGridSizer(2, 1, 0, 0)
		sweep_time_subsizer = wx.FlexGridSizer(1, 2, 0, 0)
		atten_sizer = wx.FlexGridSizer(2, 1, 0, 0)
		atten_subsizer = wx.FlexGridSizer(1, 2, 0, 0)
		res_bw_sizer = wx.FlexGridSizer(2, 1, 0, 0)
		res_bw_subsizer = wx.FlexGridSizer(1, 2, 0, 0)
		frequency_ref_level_sizer = wx.FlexGridSizer(2, 1, 0, 0)
		frequency_sizer = wx.FlexGridSizer(2, 1, 0, 0)
		frequency_input_sizer = wx.FlexGridSizer(6, 2, 0, 0)
		ref_level_sizer = wx.FlexGridSizer(2, 1, 0, 0)
		ref_level_input_sizer = wx.FlexGridSizer(1, 2, 0, 0)
		ref_level_sizer.Add(self.ref_level_label, 0, 0, 0)
		ref_level_input_sizer.Add(self.ref_level_spin_ctrl, 0, 0, 0)
		ref_level_input_sizer.Add(self.peak_to_ref_level_button, 0, 0, 0)
		ref_level_input_sizer.AddGrowableRow(0)
		ref_level_input_sizer.AddGrowableCol(0)
		ref_level_input_sizer.AddGrowableCol(1)
		ref_level_sizer.Add(ref_level_input_sizer, 1, wx.EXPAND, 0)
		ref_level_sizer.AddGrowableRow(1)
		ref_level_sizer.AddGrowableCol(0)
		frequency_ref_level_sizer.Add(ref_level_sizer, 1, wx.ALL|wx.EXPAND, 2)
		frequency_sizer.Add(self.frequency_label, 0, 0, 0)
		frequency_input_sizer.Add(self.center_frequency_label, 0, 0, 0)
		frequency_input_sizer.Add(self.placeholder_panel_1, 1, wx.EXPAND, 0)
		frequency_input_sizer.Add(self.center_freq_spin_ctrl, 0, 0, 0)
		frequency_input_sizer.Add(self.peak_to_cf_button, 0, 0, 0)
		frequency_input_sizer.Add(self.span_label, 0, 0, 0)
		frequency_input_sizer.Add(self.placeholder_panel_2, 1, wx.EXPAND, 0)
		frequency_input_sizer.Add(self.span_spin_ctrl, 0, 0, 0)
		frequency_input_sizer.Add(self.zero_span_button, 0, 0, 0)
		frequency_input_sizer.Add(self.start_frequency_label, 0, 0, 0)
		frequency_input_sizer.Add(self.stop_frequency_label, 0, 0, 0)
		frequency_input_sizer.Add(self.start_freq_spin_ctrl, 0, 0, 0)
		frequency_input_sizer.Add(self.stop_freq_spin_ctrl, 0, 0, 0)
		frequency_input_sizer.AddGrowableRow(1)
		frequency_input_sizer.AddGrowableRow(3)
		frequency_input_sizer.AddGrowableRow(5)
		frequency_input_sizer.AddGrowableCol(0)
		frequency_input_sizer.AddGrowableCol(1)
		frequency_sizer.Add(frequency_input_sizer, 1, wx.EXPAND, 2)
		frequency_sizer.AddGrowableRow(1)
		frequency_sizer.AddGrowableCol(0)
		frequency_ref_level_sizer.Add(frequency_sizer, 1, wx.ALL|wx.EXPAND, 2)
		self.frequency_ref_level_panel.SetSizer(frequency_ref_level_sizer)
		frequency_ref_level_sizer.AddGrowableRow(0)
		frequency_ref_level_sizer.AddGrowableRow(1)
		frequency_ref_level_sizer.AddGrowableCol(0)
		main_sizer.Add(self.frequency_ref_level_panel, 1, wx.ALL, 6)
		res_bw_sizer.Add(self.res_bw_label, 0, 0, 0)
		res_bw_subsizer.Add(self.res_bw_auto, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		res_bw_subsizer.Add(self.res_bw_select, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		res_bw_subsizer.AddGrowableRow(0)
		res_bw_subsizer.AddGrowableCol(0)
		res_bw_subsizer.AddGrowableCol(1)
		res_bw_sizer.Add(res_bw_subsizer, 1, wx.EXPAND, 2)
		res_bw_sizer.AddGrowableRow(1)
		res_bw_sizer.AddGrowableCol(0)
		main_settings_sizer.Add(res_bw_sizer, 1, wx.ALL|wx.EXPAND, 2)
		atten_sizer.Add(self.atten_label, 0, 0, 0)
		atten_subsizer.Add(self.atten_auto, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		atten_subsizer.Add(self.atten_select, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		atten_subsizer.AddGrowableRow(0)
		atten_subsizer.AddGrowableCol(0)
		atten_subsizer.AddGrowableCol(1)
		atten_sizer.Add(atten_subsizer, 1, wx.EXPAND, 0)
		atten_sizer.AddGrowableRow(1)
		atten_sizer.AddGrowableCol(0)
		main_settings_sizer.Add(atten_sizer, 1, wx.ALL|wx.EXPAND, 2)
		sweep_time_sizer.Add(self.sweep_time_label, 0, 0, 0)
		sweep_time_subsizer.Add(self.sweep_time_auto, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sweep_time_subsizer.Add(self.sweep_time_select, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sweep_time_subsizer.AddGrowableRow(0)
		sweep_time_subsizer.AddGrowableCol(0)
		sweep_time_subsizer.AddGrowableCol(1)
		sweep_time_sizer.Add(sweep_time_subsizer, 1, wx.EXPAND, 0)
		sweep_time_sizer.AddGrowableRow(1)
		sweep_time_sizer.AddGrowableCol(0)
		main_settings_sizer.Add(sweep_time_sizer, 1, wx.ALL|wx.EXPAND, 2)
		video_bw_sizer.Add(self.video_bw_label, 0, 0, 0)
		video_bw_subsizer.Add(self.video_bw_auto, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		video_bw_subsizer.Add(self.video_bw_select, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		video_bw_subsizer.AddGrowableRow(0)
		video_bw_subsizer.AddGrowableCol(0)
		video_bw_subsizer.AddGrowableCol(1)
		video_bw_sizer.Add(video_bw_subsizer, 1, wx.EXPAND, 0)
		video_bw_sizer.AddGrowableRow(1)
		video_bw_sizer.AddGrowableCol(0)
		main_settings_sizer.Add(video_bw_sizer, 1, wx.ALL|wx.EXPAND, 2)
		main_settings_sizer.Add(self.uncal_label, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
		self.main_settings_panel.SetSizer(main_settings_sizer)
		main_settings_sizer.AddGrowableRow(0)
		main_settings_sizer.AddGrowableRow(1)
		main_settings_sizer.AddGrowableRow(2)
		main_settings_sizer.AddGrowableRow(3)
		main_settings_sizer.AddGrowableRow(4)
		main_settings_sizer.AddGrowableCol(0)
		main_sizer.Add(self.main_settings_panel, 1, wx.RIGHT|wx.TOP|wx.BOTTOM|wx.EXPAND, 6)
		main_sizer.Add(self.panel_1, 1, wx.EXPAND, 0)
		self.notebook_main.SetSizer(main_sizer)
		main_sizer.AddGrowableRow(0)
		main_sizer.AddGrowableRow(1)
		main_sizer.AddGrowableCol(0)
		main_sizer.AddGrowableCol(1)
		console_sizer.Add(self.console_output_text_ctrl, 0, wx.EXPAND, 0)
		console_sizer.Add(self.console_input_text_ctrl, 0, wx.EXPAND, 0)
		self.notebook_console.SetSizer(console_sizer)
		console_sizer.AddGrowableRow(0)
		console_sizer.AddGrowableCol(0)
		self.notebook.AddPage(self.notebook_main, "Main Control")
		self.notebook.AddPage(self.notebook_console, "Console")
		sizer.Add(self.notebook, 1, wx.EXPAND, 0)
		self.SetSizer(sizer)
		sizer.Fit(self)
		self.Layout()
		# end wxGlade

	def menu_handler_calibrate_all(self, event): # wxGlade: MainFrame.<event_handler>
		self.statusbar.SetStatusText("Starting calibration: ALL")
		self.ms2601b.start_calibration(self.ms2601b.CAL_MODES["ALL"])

	def menu_handler_calibrate_frequency(self, event): # wxGlade: MainFrame.<event_handler>
		self.statusbar.SetStatusText("Starting calibration: FREQ")
		self.ms2601b.start_calibration(self.ms2601b.CAL_MODES["FREQ"])

	def menu_handler_calibrate_level_1(self, event): # wxGlade: MainFrame.<event_handler>
		self.statusbar.SetStatusText("Starting calibration: LEVEL (1)")
		self.ms2601b.start_calibration(self.ms2601b.CAL_MODES["LEVEL (1)"])

	def menu_handler_calibrate_level_2(self, event): # wxGlade: MainFrame.<event_handler>
		self.statusbar.SetStatusText("Starting calibration: LEVEL (2)")
		self.ms2601b.start_calibration(self.ms2601b.CAL_MODES["LEVEL (2)"])
		
	def menu_handler_calibration_correction_data(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_correction_data(event.IsChecked())

	def menu_handler_calibration_response_data(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_response_data(event.IsChecked())

	def console_input_enter_event(self, event): # wxGlade: MainFrame.<event_handler>
		command = self.console_input_text_ctrl.GetValue()
		self.console_input_text_ctrl.SetValue("")
		self.ms2601b.send(command)
		if command.startswith("++"):
			data = self.ms2601b.gpib.read()
		else:
			data = self.ms2601b.recv()+"\n"
		data = data.replace("\r\n", "\n")
		self.console_output_text_ctrl.AppendText(data)

	def menu_handler_initial(self, event): # wxGlade: MainFrame.<event_handler>
		self.statusbar.SetStatusText("Reset to initial values ...")
		self.ms2601b.set_initial()
		self.update_res_bw_atten_sweep_time_video_bw()
		self.update_scale_menu()
		self.update_unit_menu()
		self.update_antenna_menu()
		self.update_calibration_menu()
		self.update_trigger_menu()

	def menu_handler_local(self, event): # wxGlade: MainFrame.<event_handler>
		self.statusbar.SetStatusText("Returning control to local ...")
		self.ms2601b.gpib.set_loc()

	def menu_handler_scale(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_scale(self.MENUITEM_ID_TO_SCALE[event.GetId()])

	def menu_handler_antenna(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_antenna(self.MENUITEM_ID_TO_ANTENNA[event.GetId()])

	def menu_handler_trigger(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_trigger(self.MENUITEM_ID_TO_TRIGGER_TYPE[event.GetId()])

	def menu_handler_trigger_sweep(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.sweep()

	def menu_handler_unit(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_unit(self.MENUITEM_ID_TO_UNIT[event.GetId()])

	def res_bw_auto_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_resolution_bandwidth_auto(event.GetString()=="Auto")
		self.update_res_bw_atten_sweep_time_video_bw()

	def res_bw_select_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_resolution_bandwidth(event.GetString())
		self.update_res_bw_atten_sweep_time_video_bw()

	def atten_auto_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_attenuation_auto(event.GetString()=="Auto")
		self.update_res_bw_atten_sweep_time_video_bw()

	def atten_select_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_attenuation(event.GetString())
		self.update_res_bw_atten_sweep_time_video_bw()

	def sweep_time_auto_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_sweep_time_auto(event.GetString()=="Auto")
		self.update_res_bw_atten_sweep_time_video_bw()

	def sweep_time_select_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_sweep_time(event.GetString())
		self.update_res_bw_atten_sweep_time_video_bw()

	def video_bw_auto_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_video_bandwidth_auto(event.GetString()=="Auto")
		self.update_res_bw_atten_sweep_time_video_bw()

	def video_bw_select_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_video_bandwidth(event.GetString())
		self.update_res_bw_atten_sweep_time_video_bw()

	def spinctrl_handler_ref_level(self, event): # wxGlade: MainFrame.<event_handler>
		value = self.ref_level_spin_ctrl.GetValue()
		try:
			self.ms2601b.set_reference_level(float(value))
		except:
			pass

	def button_handler_peak_to_ref_level(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.peak_to_reference_level()
		self.update_reference_level()

	def spinctrl_handler_center_freq(self, event): # wxGlade: MainFrame.<event_handler>
		print "Event handler `spinctrl_handler_center_freq' not implemented"
		event.Skip()

	def button_handler_peak_to_center_freq(self, event): # wxGlade: MainFrame.<event_handler>
		print "Event handler `button_handler_peak_to_center_freq' not implemented"
		event.Skip()

	def spinctrl_handler_span(self, event): # wxGlade: MainFrame.<event_handler>
		print "Event handler `spinctrl_handler_span' not implemented"
		event.Skip()

	def button_handler_zero_span(self, event): # wxGlade: MainFrame.<event_handler>
		print "Event handler `button_handler_zero_span' not implemented"
		event.Skip()

	def spinctrl_handler_start_freq(self, event): # wxGlade: MainFrame.<event_handler>
		print "Event handler `spinctrl_handler_start_freq' not implemented"
		event.Skip()

	def spinctrl_handler_stop_freq(self, event): # wxGlade: MainFrame.<event_handler>
		print "Event handler `spinctrl_handler_stop_freq' not implemented"
		event.Skip()

	def update_reference_level(self):
		print self.ms2601b.get_reference_level()
		self.ref_level_spin_ctrl.SetValue(self.ms2601b.get_reference_level())

	def update_res_bw_atten_sweep_time_video_bw(self):
		self.res_bw_auto.SetSelection((1-int(self.ms2601b.get_resolution_bandwidth_auto())))
		self.res_bw_select.SetStringSelection(self.ms2601b.get_resolution_bandwidth())
		self.atten_auto.SetSelection((1-int(self.ms2601b.get_attenuation_auto())))
		self.atten_select.SetStringSelection(self.ms2601b.get_attenuation())
		self.sweep_time_auto.SetSelection((1-int(self.ms2601b.get_sweep_time_auto())))
		self.sweep_time_select.SetStringSelection(self.ms2601b.get_sweep_time())
		self.video_bw_auto.SetSelection((1-int(self.ms2601b.get_video_bandwidth_auto())))
		self.video_bw_select.SetStringSelection(self.ms2601b.get_video_bandwidth())
		self.uncal_label.Show(self.ms2601b.get_uncal_status())

	def update_scale_menu(self):
		self.menubar.FindItemById(self.SCALE_TO_MENUITEM_ID[self.ms2601b.get_scale()]).Check(True)

	def update_unit_menu(self):
		self.menubar.FindItemById(self.UNIT_TO_MENUITEM_ID[self.ms2601b.get_unit()]).Check(True)

	def update_antenna_menu(self):
		self.menubar.FindItemById(self.ANTENNA_TO_MENUITEM_ID[self.ms2601b.get_antenna()]).Check(True)

	def update_calibration_menu(self):
		self.menubar.FindItemById(MENU_CALIBRATION_CORRECTION_DATA).Check(self.ms2601b.get_correction_data())
		self.menubar.FindItemById(MENU_CALIBRATION_RESPONSE_DATA).Check(self.ms2601b.get_response_data())

	def update_trigger_menu(self):
		self.menubar.FindItemById(self.TRIGGER_TYPE_TO_MENUITEM_ID[self.ms2601b.get_trigger()]).Check(True)

# end of class MainFrame


if __name__ == "__main__":
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frame_1 = MainFrame(None, -1, "")
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()
