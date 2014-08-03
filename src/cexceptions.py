'''
Created on 03-Aug-2014

@author: rahul
'''


class ImproperlyConfigured(Exception):
    '''
        Raised when the redis server configuration in improper / missing.
    '''
    def __init__(self, value):
        '''
            Initialize.
        '''
        self.value = value

    def __str__(self):
        '''
            Represent this object in string format.
        '''
        return repr(self.value)


class MissingArguments(Exception):
    '''
        Raised when user does not supply required parameters from
        command line while calling this program.
    '''
    def __init__(self, value):
        '''
            Initialize.
        '''
        self.value = value

    def __str__(self):
        '''
            Represent this object in string format.
        '''
        return repr(self.value)
