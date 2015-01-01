import ConfigParser


class Config():
    config = None

    def __init__(self, file):

        self.config = ConfigParser.ConfigParser(allow_no_value=True)
        self.config.read(file)

    def get(self, section, key):
        return self.config.get(section, key)

    def getSplit(self, section, key):
        return self.get(section, key).split()