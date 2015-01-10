import os


class Terminal:
    main_path = None

    @staticmethod
    def startSelenium():
        Terminal.main_path = os.getcwd()

        os.chdir("node_modules/nightwatch/lib")

        try:
            os.system("java -jar sel-serv.jar")
        except:
            pass

    @staticmethod
    def publishAd():
        os.chdir(Terminal.main_path)
        os.system('node nightwatch.js')
