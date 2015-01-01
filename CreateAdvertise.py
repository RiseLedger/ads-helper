import wx


class CreateAdvertise(wx.Frame):
    panel = None

    def __init__(self, *args, **kw):
        super(CreateAdvertise, self).__init__(*args, **kw)
        self.init()

    def init(self):
        self.createGUILayout()

    def createGUILayout(self):
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.panel, label='Advertise Name')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(self.panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        self.panel.SetSizer(vbox)
        self.panel.Show()
