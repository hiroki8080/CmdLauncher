# !/usr/bin/env python
# coding:utf-8

import os
import wx

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
		self.TxtCtr.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
		self.lbFrame = wx.Frame(None, 0, "wxPython", size=(420,200),pos=(400,448),style=wx.DOUBLE_BORDER)
		self.LBox = wx.ListBox(self.lbFrame, -1, choices = self.List, size=(415,200))
		Frm.Show()
		self.TxtCtr.SetFocus()

	def OnKeyDown(self,event):		
		'''
			handling the key.
		'''
		
		key = event.GetKeyCode()
		input = self.TxtCtr.GetValue()
		input = os.path.normpath(os.path.normcase(input))
		select = self.LBox.GetStringSelection()
		if key ==  wx.WXK_ESCAPE:
			wx.Exit()
		elif key == wx.WXK_SHIFT:
			event.Skip()
		elif key == wx.WXK_TAB:
			SetTextValue(select)
			if SearchExist(self, input):
				SetCurrentList(self, select)
			else:
				event.Skip()
		elif key == wx.WXK_UP:
			count = self.LBox.GetCount()
			next = self.LBox.GetSelection() - 1
			if next >=  0:
				self.LBox.SetSelection(next)
			else: self.LBox.SetSelection(count - 1)
		elif key == wx.WXK_DOWN:
			count = self.LBox.GetCount()
			next = self.LBox.GetSelection() + 1
			if next < count:
				self.LBox.SetSelection(next)
			elif count > 0:
				self.LBox.SetSelection(0)
			else:
				event.Skip()
		elif key == wx.WXK_RETURN:
			SetTextValue(select)
			self.lbFrame.Hide()
			if os.path.isdir(select) :
				os.system("explorer " + select)
			else:
				os.system(select)
		else:
			if input != "" and os.path.exists(input) :
				if SearchExist(self, input):
					event.Skip()
				else:
					SetCurrentList(self, input)
					event.Skip()
			else:
				event.Skip()

def SetTextValue(self, value):
	self.TxtCtr.Clear()
	self.TxtCtr.SetValue(value)
	self.TxtCtr.SetFocus()
	self.TxtCtr.SetInsertionPoint(self.TxtCtr.LastPosition)

def SetCurrentList(self, input):
	self.LBox.Clear()
	self.lbFrame.Show()
	files = os.listdir(input)
	for file in files:
		if os.path.isdir(file):
			self.LBox.Append(input + os.sep + file + os.sep)
		else:
			self.LBox.Append(input + os.sep + file)
	self.TxtCtr.SetFocus()
	
def SearchExist(self, target):
	for i in self.LBox.GetItems():
		if i == target :
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

