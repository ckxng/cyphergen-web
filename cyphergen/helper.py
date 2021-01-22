'''A collection of helper functions'''


class Helper(object):
    '''A collection of helper functions'''

    def __init__(self, app):
        '''Create the Helper object

        Parameters:
        app(Flask): The Flask app

        Returns:
        Helper
        '''

        self.app = app

    def apipath(self, path):
        '''Generate a path including the API path (not including base URI)

        Parameters:
        path(str): the path to append to APIPATH

        Retrns:
        str
        '''

        return self.app.config.get('APIPATH') + path

    def apiuri(self, path):
        '''Generate a full URI for the API

        Parameters:
        path(str): the path to append to BASEURI and APIPATH

        Returns:
        str
        '''

        return self.app.config.get('BASEURI') + self.app.config.get('APIPATH') + path

    def uri(self, path):
        '''Generate a full URI

        Parameters:
        path(str): the path to append to BASEURI

        Returns:
        str
        '''

        return self.app.config.get('BASEURI') + path
