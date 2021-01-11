
class Helper(object):
    def __init__(self, app):
        self.app = app

    def path(self, path):
        return self.app.config.get('APIPATH') + path

    def uri(self, path):
        return self.app.config.get('BASEURI') + self.app.config.get('APIPATH') + path
