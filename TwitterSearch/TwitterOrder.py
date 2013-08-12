# -*- coding: utf-8 -*-

from .TwitterSearchException import TwitterSearchException
from .utils import py3k

class TwitterOrder(object):

    arguments = {}
    
    def createSearchURL(self):
        """ Generates (urlencoded) query string from stored key-values tuples. Has to be implemented within child classes. """
        raise NotImplementedError
        
    def setSearchURL(self):
        """ Reads given query string and stores key-value tuples. Has to be implemented within child classes. """
        raise NotImplementedError

    def setSinceID(self, twid):
        """ Sets 'since_id' parameter """
        if py3k:
            if not isinstance(twid, int):
                raise TwitterSearchException(1004)
        else:
           if not isinstance(twid, (int, long)):
                raise TwitterSearchException(1004)

        if twid > 0:
            self.arguments.update( { 'since_id' : '%s' % twid } )
        else:
            raise TwitterSearchException(1004)

    def setMaxID(self, twid):
        """ Sets 'max_id' parameter """
        if py3k:
            if not isinstance(twid, int):
                raise TwitterSearchException(1004)
        else:
           if not isinstance(twid, (int, long)):
                raise TwitterSearchException(1004)

        if twid > 0:
            self.arguments.update( { 'max_id' : '%s' % twid } )
        else:
            raise TwitterSearchException(1004)
            
    def setCount(self, cnt):
        """ Sets 'count' paramater """
        if isinstance(cnt, int) and cnt > 0 and cnt <= 100:
            self.arguments.update( { 'count' : '%s' % cnt } )
        else:
            raise TwitterSearchException(1004)
            
    def setIncludeEntities(self, include):
        """ Sets 'include entities' paramater """
        if not isinstance(include, bool):
            raise TwitterSearchException(1008)
        self.arguments.update( { 'include_entities' : 'true' if include else 'false' } )
