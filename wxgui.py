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
		
		# Menu Bar
		self.menubar = wx.MenuBar()
		wxglade_tmp_menu = wx.Menu()
		wxglade_tmp_menu.Append(MENU_INITIAL, "Initial", "", wx.ITEM_NORMAL)
		wxglade_tmp_menu.Append(MENU_LOCAL, "Local", "", wx.ITEM_NORMAL)
		self.menubar.Append(wxglade_tmp_menu, "Device")
		wxglade_tmp_menu = wx.Menu()
		wxglade_tmp_menu.Append(MENU_SCALE_1DB, "Log 1dB", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_SCALE_2DB, "Log 2dB", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_SCALE_5DB, "Log 5dB", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_SCALE_10DB, "Log 10dB", "", wx.ITEM_RADIO)
		wxglade_tmp_menu.Append(MENU_SCALE_LIN, "Lin", "", wx.ITEM_RADIO)
		self.menubar.Append(wxglade_tmp_menu, "Scale")
		wxglade_tmp_menu = wx.Menu()
		wxglade_tmp_menu.Append(MENU_CALIBRATION_ALL, "All", "", wx.ITEM_NORMAL)
		wxglade_tmp_menu.Append(MENU_CALIBRATION_LEVEL_1, "Level (1)", "", wx.ITEM_NORMAL)
		wxglade_tmp_menu.Append(MENU_CALIBRATION_LEVEL_2, "Level (2)", "", wx.ITEM_NORMAL)
		wxglade_tmp_menu.Append(MENU_CALIBRATION_FREQUENCY, "Frequency", "", wx.ITEM_NORMAL)
		self.menubar.Append(wxglade_tmp_menu, "Calibration")
		self.SetMenuBar(self.menubar)
		# Menu Bar end
		self.statusbar = self.CreateStatusBar(1, 0)
		self.res_bw_label = wx.StaticText(self.notebook_main, -1, "Resolution bandwidth")
		self.res_bw_auto = wx.RadioBox(self.notebook_main, -1, "Auto/Manual", choices=["Auto", "Manual"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
		self.res_bw_select = wx.ComboBox(self.notebook_main, -1, choices=["1 MHz", "300 kHz", "100 kHz", "30 kHz", "10 kHz", "3 kHz", "1 kHz", "300 Hz", "100 Hz", "30 Hz"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
		self.atten_label = wx.StaticText(self.notebook_main, -1, "Attenuation")
		self.atten_auto = wx.RadioBox(self.notebook_main, -1, "Auto/Manual", choices=["Auto", "Manual"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
		self.atten_select = wx.ComboBox(self.notebook_main, -1, choices=["50 dB", "40 dB", "30 dB", "20 dB", "10 dB", "0 dB"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
		self.sweep_time_label = wx.StaticText(self.notebook_main, -1, "Sweep time")
		self.sweep_time_auto = wx.RadioBox(self.notebook_main, -1, "Auto/Manual", choices=["Auto", "Manual"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
		self.sweep_time_select = wx.ComboBox(self.notebook_main, -1, choices=["1000 s", "700 s", "500 s", "300 s", "200 s", "150 s", "100 s", "70 s", "50 s", "30 s", "20 s", "15 s", "10 s", "7 s", "5 s", "3 s", "2 s", "1.5 s", "1 s", "700 ms", "500 ms", "300 ms", "200 ms", "150 ms", "100 ms", "70 ms", "50 ms"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
		self.video_bw_label = wx.StaticText(self.notebook_main, -1, "Video bandwidth")
		self.video_bw_auto = wx.RadioBox(self.notebook_main, -1, "Auto/Manual", choices=["Auto", "Manual"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
		self.video_bw_select = wx.ComboBox(self.notebook_main, -1, choices=["-OFF-", "100 kHz", "10 kHz", "1 kHz", "100 Hz", "10 Hz", "1 Hz"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
		self.uncal_label = wx.StaticText(self.notebook_main, -1, "Uncalibrated")
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
		self.Bind(wx.EVT_MENU, self.menu_handler_calibrate_all, id=MENU_CALIBRATION_ALL)
		self.Bind(wx.EVT_MENU, self.menu_handler_calibrate_level_1, id=MENU_CALIBRATION_LEVEL_1)
		self.Bind(wx.EVT_MENU, self.menu_handler_calibrate_level_2, id=MENU_CALIBRATION_LEVEL_2)
		self.Bind(wx.EVT_MENU, self.menu_handler_calibrate_frequency, id=MENU_CALIBRATION_FREQUENCY)
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
		
		self.ms2601b = MS2601B.MS2601B()
		# set scale menu correctly
		self.SCALE_TO_MENUITEM_ID = {"1 dB": MENU_SCALE_1DB, "2 dB": MENU_SCALE_2DB, "5 dB": MENU_SCALE_5DB, "10 dB": MENU_SCALE_10DB, "Linear": MENU_SCALE_LIN }
		self.MENUITEM_ID_TO_SCALE = dict([(b,a) for (a,b) in self.SCALE_TO_MENUITEM_ID.iteritems()])
		self.menubar.FindItemById(self.SCALE_TO_MENUITEM_ID[self.ms2601b.scale]).Check(True)
		# update main settings with actual values
		self.update_res_bw_sweep_time_video_bw()
		# update sweep time with actual values
		self.updat_atten()

	def __set_properties(self):
		# begin wxGlade: MainFrame.__set_properties
		self.SetTitle("MS2601B GPIB control")
		self.SetSize((967, 903))
		self.statusbar.SetStatusWidths([-1])
		# statusbar fields
		statusbar_fields = [""]
		for i in range(len(statusbar_fields)):
		    self.statusbar.SetStatusText(statusbar_fields[i], i)
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
		main_settings_sizer.AddGrowableRow(0)
		main_settings_sizer.AddGrowableRow(1)
		main_settings_sizer.AddGrowableRow(2)
		main_settings_sizer.AddGrowableRow(3)
		main_settings_sizer.AddGrowableRow(4)
		main_settings_sizer.AddGrowableCol(0)
		main_sizer.Add(main_settings_sizer, 1, wx.ALL|wx.ALIGN_RIGHT, 5)
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

	def menu_handler_local(self, event): # wxGlade: MainFrame.<event_handler>
		self.statusbar.SetStatusText("Returning control to local ...")
		self.ms2601b.gpib.set_loc()

	def menu_handler_scale(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_scale(self.MENUITEM_ID_TO_SCALE[event.GetId()])

	def res_bw_auto_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_resolution_bandwidth_auto(event.GetString()=="Auto")
		self.update_res_bw_sweep_time_video_bw()

	def res_bw_select_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_resolution_bandwidth(event.GetString())
		self.update_res_bw_sweep_time_video_bw()

	def atten_auto_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_attenuation_auto(event.GetString()=="Auto")
		self.updat_atten()

	def atten_select_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_attenuation(event.GetString())
		self.updat_atten()

	def sweep_time_auto_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_sweep_time_auto(event.GetString()=="Auto")
		self.update_res_bw_sweep_time_video_bw()

	def sweep_time_select_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_sweep_time(event.GetString())
		self.update_res_bw_sweep_time_video_bw()

	def video_bw_auto_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_video_bandwidth_auto(event.GetString()=="Auto")
		self.update_res_bw_sweep_time_video_bw()

	def video_bw_select_handler(self, event): # wxGlade: MainFrame.<event_handler>
		self.ms2601b.set_video_bandwidth(event.GetString())
		self.update_res_bw_sweep_time_video_bw()

	def update_res_bw_sweep_time_video_bw(self):
		if self.ms2601b.res_bw_auto:
			self.res_bw_auto.SetSelection((1-int(self.ms2601b.get_resolution_bandwidth_auto())))
			self.res_bw_select.SetStringSelection(self.ms2601b.get_resolution_bandwidth())
		if self.ms2601b.sweep_time_auto:
			self.sweep_time_auto.SetSelection((1-int(self.ms2601b.get_sweep_time_auto())))
			self.sweep_time_select.SetStringSelection(self.ms2601b.get_sweep_time())
		if self.ms2601b.video_bw_auto:
			self.video_bw_auto.SetSelection((1-int(self.ms2601b.get_video_bandwidth_auto())))
			self.video_bw_select.SetStringSelection(self.ms2601b.get_video_bandwidth())
		self.uncal_label.Show(self.ms2601b.get_uncal_status())

	def updat_atten(self):
		self.atten_auto.SetSelection((1-int(self.ms2601b.get_attenuation_auto())))
		self.atten_select.SetStringSelection(self.ms2601b.get_attenuation())

# end of class MainFrame


if __name__ == "__main__":
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frame_1 = MainFrame(None, -1, "")
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()
