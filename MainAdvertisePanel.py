import wx
from AdsPanel import AdsPanel


class MainAdvertisePanel(wx.Panel, AdsPanel):
    add_ad = None
    edit_ad = None

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

        advertises = ['Advertise 1', 'Advertise 2', 'Advertise 3']
        advertise_list = wx.ComboBox(self, pos=(50, 30), choices=advertises, style=wx.CB_READONLY)
        advertise_list.Bind(wx.EVT_COMBOBOX, self.onAdvertiseSelect)
        hbox1.Add(advertise_list, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 15))

        # publish-edit buttons
        h_publish_edit_ads = wx.BoxSizer(wx.HORIZONTAL)
        self.add_ad = wx.Button(self, label='Publish Selected Advertise', size=(170, 30))
        self.edit_ad = wx.Button(self, label='Edit Selected Advertise', size=(170, 30))

        h_publish_edit_ads.Add(self.add_ad)
        h_publish_edit_ads.Add(self.edit_ad)
        vbox.Add(h_publish_edit_ads, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        self.SetSizer(vbox)

    def onAdvertiseSelect(self, e):
        print e.GetString()
