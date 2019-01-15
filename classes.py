# klasser

class User(object):
    def __init__(self, name, userID, subbedChannels, userClassObject):
        self.name = name
        self.userID = userID
        self.subbedChannels = subbedChannels
        self.userClassObject = userClassObject

    def addChannel(self, channelName):
        self.subbedChannels = self.subbedChannels + [channelName]
