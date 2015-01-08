import wx
from AdsPanel import AdsPanel


class CreateAdvertisePanel(wx.Panel, AdsPanel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.init()

    def init(self):
        self.createGUILayout()

    def createGUILayout(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label='Advertise Name')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(self)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        self.SetSizer(vbox)
