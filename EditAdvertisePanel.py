import wx
from AdsPanel import AdsPanel


class EditAdvertisePanel(wx.Panel, AdsPanel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.init()

    def init(self):
        self.createGUILayout()

    def createGUILayout(self):
        pass
