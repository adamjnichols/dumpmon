'''
helper.py - provides misc. helper functions
Author: Jordan

'''

import requests
import settings
from time import sleep, strftime
import logging


r = requests.Session()


def download(url, headers=None):
    if not headers:
        #headers = None
        headers = {'Cookie': '__utma=47852966.2049816161.1362497527.1363207137.1364224777.8; __utmz=47852966.1362497527.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cookie_key=5; realuser=1; pastebin_user=2dad02b0591bdb36dbd97fffee0b4147'}

    if headers:
        r.headers.update(headers)
    try:
        response = r.get(url).text
    except requests.ConnectionError:
        logging.warn('[!] Critical Error - Cannot connect to site')
        sleep(5)
        logging.warn('[!] Retrying...')
        response = download(url)
    return response


def log(text):
    '''
    log(text): Logs message to both STDOUT and to .output_log file

    '''
    #print(text)
    with open(settings.log_file, 'a') as logfile:
        logfile.write(text + '\n')

def action(paste):

    if paste.match():
        if paste.num_emails > 0:
            print(paste.emails)
