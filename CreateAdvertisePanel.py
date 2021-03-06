import wx
from AdsPanel import AdsPanel
from SaveAdvertise import SaveAdvertise


class CreateAdvertisePanel(wx.Panel, AdsPanel):

    input_type = ['select', 'check', 'input', 'number', 'textarea']
    selected_widget = None
    dynamic_sizer = None
    widgets_list = []
    name = None
    url = None

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.init()

    def init(self):
        self.createGUILayout()

    def createGUILayout(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label='Advertise Name')
        hbox0.Add(st1, flag=wx.RIGHT, border=8)
        self.name = wx.TextCtrl(self)
        hbox0.Add(self.name, proportion=1)
        vbox.Add(hbox0, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        url_label = wx.StaticText(self, label='Advertise URL')
        hbox1.Add(url_label, flag=wx.RIGHT, border=8)
        self.url = wx.TextCtrl(self)
        hbox1.Add(self.url, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        field_type = wx.ComboBox(self, pos=(50, 30), choices=self.input_type, style=wx.CB_READONLY)
        field_type.Bind(wx.EVT_COMBOBOX, self.onFieldSelect)
        hbox2.Add(field_type, proportion=1)

        add_button = wx.Button(self, label="Add")
        add_button.Bind(wx.EVT_BUTTON, self.onWidgetAdd);
        hbox2.Add(add_button, flag=wx.LEFT, border=8)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        self.dynamic_sizer = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.dynamic_sizer, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        save_button = wx.Button(self, label="Save Advertise")
        save_button.Bind(wx.EVT_BUTTON, self.saveAdvertise)
        hbox3.Add(save_button)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        self.SetSizer(vbox)

    def onWidgetAdd(self, e):
        if self.selected_widget == 'input' or self.selected_widget == 'number':
            self.addTextWidget(self.selected_widget)
        elif self.selected_widget == 'check' or self.selected_widget == 'select':
            self.addCheckboxWidget(self.selected_widget)
        elif self.selected_widget == 'textarea':
            self.addMessageWidget(self.selected_widget)

    def onFieldSelect(self, e):
        self.selected_widget = e.GetString()

    def addTextWidget(self, type):
        row_of_widgets = wx.BoxSizer(wx.HORIZONTAL)
        widget_text = wx.TextCtrl(self)
        widget_code = wx.TextCtrl(self)

        widget_text.SetValue('Text to add')
        widget_code.SetValue('XPath Code')

        row_of_widgets.Add(widget_text, proportion=1)
        row_of_widgets.Add(widget_code, proportion=1,flag=wx.EXPAND|wx.LEFT, border=4)

        self.dynamic_sizer.Add(row_of_widgets, 1, wx.EXPAND|wx.ALL)
        self.dynamic_sizer.AddSpacer(5)

        self.widgets_list.append({
            "type" : type,
            "code" : widget_code,
            "text" : widget_text
        })
        self.Layout()


    def addCheckboxWidget(self, type):
        checkbox_widget = wx.TextCtrl(self)
        checkbox_widget.SetValue('XPath Code')
        self.dynamic_sizer.Add(checkbox_widget, 1, wx.EXPAND|wx.ALL)
        self.dynamic_sizer.AddSpacer(5)
        self.widgets_list.append({
            "type" : type,
            "code" : checkbox_widget
        })
        self.Layout()

    def addMessageWidget(self, type):
        row_of_widgets = wx.BoxSizer(wx.HORIZONTAL)
        widget_textarea = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        widget_code_textarea = wx.TextCtrl(self)

        widget_textarea.SetValue('Your Message Goes Here')
        widget_code_textarea.SetValue('XPath Code')

        row_of_widgets.Add(widget_textarea, proportion=1)
        row_of_widgets.Add(widget_code_textarea, flag=wx.EXPAND|wx.LEFT, border=4)

        self.dynamic_sizer.Add(row_of_widgets, 1, wx.EXPAND|wx.ALL)
        self.dynamic_sizer.AddSpacer(5)

        self.widgets_list.append({
            "type" : type,
            "code" : widget_code_textarea,
            "text" : widget_textarea
        })
        self.Layout()

    def saveAdvertise(self, e):
        SaveAdvertise(self.name.GetValue(), self.url.GetValue(), self.widgets_list)
