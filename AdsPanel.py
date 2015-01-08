from abc import ABCMeta, abstractmethod


class AdsPanel:
    __metaclass__ = ABCMeta

    @abstractmethod
    def createGUILayout(self):
        pass