from .regexes import regexes
import settings
import logging
import re

class Paste(object):
    def __init__(self):
        '''
        class Paste: Generic "Paste" object to contain attributes of a standard paste

        '''
        self.emails = 0
	self.num_emails = 0
        self.sites = None
        self.text = None
        self.type = None

    def match(self):
        '''
        Matches the paste against a series of regular expressions to determine if the paste is 'interesting'

        Sets the following attributes:
                self.emails

        '''
        self.emails = list(set(regexes['email'].findall(self.text)))
        self.num_emails = len(self.emails)
        if self.num_emails > 0:
            self.sites = list(set([re.search('@(.*)$', email).group(1).lower() for email in self.emails]))
        for regex in regexes['blacklist']:
            if regex.search(self.text):
                logging.debug('\t[-] ' + regex.search(self.text).group(1))
        if (self.num_emails >= settings.EMAIL_THRESHOLD):
            self.type = 'db_dump'
        for regex in regexes['banlist']:
            if regex.search(self.text):
                self.type = None
                break
        return self.type
