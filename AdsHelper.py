import wx
from Config import Config
from ContextMenu import ContextMenu
from MainAdvertisePanel import MainAdvertisePanel
from CreateAdvertisePanel import CreateAdvertisePanel
from EditAdvertisePanel import EditAdvertisePanel


class AdsHelper(wx.Frame):
    config = None
    sizer = None
    ids = [1, 2, 3] # use for menu bindings

    def __init__(self, *args, **kw):
        super(AdsHelper, self).__init__(*args, **kw)
        self.init()

    def init(self):
        self.loadConfig()
        self.setPanels()
        self.eventsBind()
        self.createMenuBar()
        self.createGUIWindow()

    def loadConfig(self):
        self.config = Config('config.ini')

    def setPanels(self):
        self.main_panel = MainAdvertisePanel(self)
        self.create_panel = CreateAdvertisePanel(self)
        self.edit_panel = EditAdvertisePanel(self)

        self.create_panel.Hide()
        self.edit_panel.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.main_panel, 1, wx.EXPAND)
        self.sizer.Add(self.create_panel, 1, wx.EXPAND)
        self.sizer.Add(self.edit_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    def eventsBind(self):
        for val in self.ids:
            self.Bind(wx.EVT_MENU, self.onPanelSwitch, id=val)

    def createGUIWindow(self):
        self.SetSize((350, 130))
        self.SetTitle('Ads Helper')
        self.Centre()
        self.Show(True)

    def createMenuBar(self):
        menuItems = self.config.getSplit('menubar', 'items')
        menuBar = wx.MenuBar()

        for item in menuItems:
            submenuItems = self.config.getSplit('menubar', item)
            fMenu = wx.Menu()

            i = 0
            for subItem in submenuItems:
                fMenu.Append(self.ids[i], subItem)
                i += 1

            menuBar.Append(fMenu, item )
        self.SetMenuBar(menuBar)

    def onPanelSwitch(self, event):
        if event.GetId() == 1:
            self.main_panel.Show()
            self.create_panel.Hide()
            self.edit_panel.Hide()
            self.Layout()

        if event.GetId() == 2:
            self.main_panel.Hide()
            self.create_panel.Show()
            self.edit_panel.Hide()
            self.Layout()

        if event.GetId() == 3:
            self.main_panel.Hide()
            self.create_panel.Hide()
            self.edit_panel.Show()
            self.Layout()
