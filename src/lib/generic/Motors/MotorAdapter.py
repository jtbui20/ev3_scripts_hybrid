class MotorAdapter(object):
    def __init__(self, config):
        self.port = config.get("Port", None)
        pass

    def CreateMotorAdapter(self):
        pass

    def HandleErrorStop(self):
        pass

    def On(self, speed):
        pass

    def Off(self, mode):
        pass

    @property
    def isStalled(self):
        pass
