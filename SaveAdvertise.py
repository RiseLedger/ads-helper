import wx
import json


class SaveAdvertise:
    json_data = {
        "url" : None,
        "data" : []
    }

    def __init__(self, name, url, widgets):
        self.name = name
        self.url = url
        self.widgets = widgets

        self.buildData()
        self.writeToFile()

    def buildData(self):
        self.json_data['url'] = self.url
        for widget in self.widgets:
            item = {}
            if widget['type'] == 'input' or widget['type'] == 'textarea' or widget['type'] == 'number':
                item[widget['type']] = [widget['code'].GetValue(), widget['text'].GetValue()]
            else:
                item[widget['type']] = widget['code'].GetValue()

            self.json_data['data'].append(item)

    def writeToFile(self):
        with open('tests/999.json', 'w') as outfile:
            json.dump(self.json_data, outfile)
            wx.MessageBox('Advertise was saved. Go to Home window to publish the ad. Thanks', 'Info', wx.OK | wx.ICON_INFORMATION)
