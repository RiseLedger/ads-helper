import wx
from Config import Config
from ContextMenu import ContextMenu


class AdsHelper(wx.Frame):
    config = None
    add_ad = None
    edit_ad = None
    panel = None

    advertise_ids = {
        'ID_AD_MAIN' : wx.NewId(),
        'ID_AD_NEW' : wx.NewId(),
        'ID_AD_EDIT' : wx.NewId()
    }

    def __init__(self, *args, **kw):
        super(AdsHelper, self).__init__(*args, **kw)
        self.init()

    def init(self):
        self.loadConfig()
        self.setPanels()
        self.setPanelsState()
        self.createGUILayout()
        self.eventsBind()
        self.createMenuBar()
        self.createGUIWindow()

    def loadConfig(self):
        self.config = Config('config.ini')

    def setPanels(self):
        pass

    def setPanelsState(self):
        pass

    def eventsBind(self):
        for val in sorted( self.advertise_ids.itervalues() ):
            self.Bind(wx.EVT_MENU, self.onPanelSwitch, id=val)

    def createGUILayout(self):
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.panel, label='Advertise Name')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)

        advertises = ['Advertise 1', 'Advertise 2', 'Advertise 3']
        advertise_list = wx.ComboBox(self.panel, pos=(50, 30), choices=advertises, style=wx.CB_READONLY)
        advertise_list.Bind(wx.EVT_COMBOBOX, self.onAdvertiseSelect)
        hbox1.Add(advertise_list, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 15))

        # publish-edit buttons
        h_publish_edit_ads = wx.BoxSizer(wx.HORIZONTAL)
        self.add_ad = wx.Button(self.panel, label='Publish Selected Advertise', size=(170, 30))
        self.edit_ad = wx.Button(self.panel, label='Edit Selected Advertise', size=(170, 30))

        h_publish_edit_ads.Add(self.add_ad)
        h_publish_edit_ads.Add(self.edit_ad)
        vbox.Add(h_publish_edit_ads, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        self.panel.SetSizer(vbox)

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
            advertise_keys = self.advertise_ids.keys()

            i = 0
            for subItem in submenuItems:
                fMenu.Append(self.advertise_ids[advertise_keys[i]], subItem)
                i += 1

            menuBar.Append(fMenu, item )
        self.SetMenuBar(menuBar)

    def onAdvertiseSelect(self, e):
        print e.GetString()

    def onRightDown(self, e):
        self.PopupMenu(ContextMenu(self), e.GetPosition())

    def onPanelSwitch(self, event):
        if event.GetId() == self.advertise_ids['ID_AD_MAIN']:
            print 'show main panel'

        if event.GetId() == self.advertise_ids['ID_AD_NEW']:
            print 'show new advertise panel'

        if event.GetId() == self.advertise_ids['ID_AD_EDIT']:
            print 'show edit advertise panel'
