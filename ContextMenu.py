import wx
from CreateAdvertise import CreateAdvertise


class ContextMenu(wx.Menu):
    new_add = None

    def __init__(self, parent):
        super(ContextMenu, self).__init__()
        self.parent = parent

        self.new_ad = wx.MenuItem(self, wx.NewId(), 'Create New Advertise')
        self.AppendItem(self.new_ad)

        self.Bind(wx.EVT_MENU, self.onCreateAdvertise, self.new_ad)

    def onCreateAdvertise(self, e):
        self.parent.panel.Hide()
        CreateAdvertise(None)

