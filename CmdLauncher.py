# !/usr/bin/env python
# coding:utf-8

import os,wx

'''
	Simple Command Launcher.

	create 2013/01/22
	auther hiroki8080
	version 0.1.0
	
'''
class CmdLauncher(wx.Frame):

	def __init__(self, parent, title):
		'''
			build a command-line window.
		'''
		
		self.List = []
		Frm = wx.Frame(None, -1, "CmdLauncher", size=(400,50),pos=(400,400))
		self.TxtCtr = wx.TextCtrl(Frm, -1)
		self.TxtCtr.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
		self.lbFrame = wx.Frame(None, 0, "wxPython", size=(420,200),pos=(400,448),style=wx.DOUBLE_BORDER)
		self.LBox = wx.ListBox(self.lbFrame, -1, choices = self.List, size=(415,200))
		self.LBox.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
		Frm.Show()
		self.TxtCtr.SetFocus()

	def on_key_down(self,event):
		'''
			handling the key.
		'''
		
		key = event.GetKeyCode()
		input = self.TxtCtr.GetValue()
		if input == u'':
			input = '/'
		input = os.path.normpath(os.path.normcase(input))
		select = self.LBox.GetStringSelection()
		if key ==  wx.WXK_ESCAPE:
			wx.Exit()
		elif key == wx.WXK_SHIFT:
			event.Skip()
		elif key == wx.WXK_TAB:
			set_text(self, select)
			if search_exist(self, input):
				set_list(self, select)
			else:
				event.Skip()
		elif key == wx.WXK_UP:
			count = self.LBox.GetCount()
			next = self.LBox.GetSelection() - 1
			self.LBox.EnsureVisible(next)
			if next >=  0:
				self.LBox.SetSelection(next)
			else: self.LBox.SetSelection(count - 1)
		elif key == wx.WXK_DOWN:
			count = self.LBox.GetCount()
			next = self.LBox.GetSelection() + 1
			self.LBox.EnsureVisible(next)
			if next < count:
				self.LBox.SetSelection(next)
			elif count > 0:
				self.LBox.SetSelection(0)
			else:
				event.Skip()
		elif key == wx.WXK_RETURN:
			set_text(self, select)
			self.lbFrame.Hide()
			if os.path.isdir(select) :
				os.system("explorer " + select)
			else:
				os.system(select)
		else:
			if input != "" and os.path.exists(input) :
				if search_exist(self, input):
					event.Skip()
				else:
					set_list(self, input)
					event.Skip()
			else:
				event.Skip()
			self.lbFrame.SetFocus()

def set_text(self, value):
	self.TxtCtr.Clear()
	self.TxtCtr.SetValue(value)
	self.TxtCtr.SetFocus()
	self.TxtCtr.SetInsertionPoint(self.TxtCtr.LastPosition)

def set_list(self, input):
	self.LBox.Clear()
	self.lbFrame.Show()
	if os.path.isdir(input):
		files = os.listdir(input)
		for file in files:
			if os.path.isdir(file):
				self.LBox.Append(input + os.sep + file + os.sep)
			else:
				self.LBox.Append(input + os.sep + file)
		self.TxtCtr.SetFocus()
	
def search_exist(self, target):
	for item in self.LBox.GetItems():
		item = os.path.normpath(os.path.normcase(item))
		if item.encode('utf-8').startswith(target.encode('utf-8')) :
			return True

def main():
	app = wx.App(False)
        launcher = CmdLauncher(None, 'My CmdLauncher')
	app.MainLoop()

if __name__ == '__main__':
    main()



#	dlg = wx.MessageDialog( self.lbFrame, inputValue, "Value", wx.OK)
#	dlg.ShowModal()
#	dlg.Destroy()

