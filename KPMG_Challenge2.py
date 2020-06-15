#!/usr/bin/env python

import requests
import json


# Converts AWS EC2 instance metadata to a dictionary
def load():
    metaurl = 'http://169.254.169.254/latest'
    # Can get dynamic & user-data by passing them into dict
    dict = {'meta-data': {}}

    for subsect in dict.keys():
        get_info('{0}/{1}/'.format(metaurl, subsect), dict[subsect])

    return dict

def get_info(url, d):
    r = requests.get(url)
    if r.status_code == 404:
        return

    for l in r.text.split('\n'):
        if not l:
            continue
        newurl = '{0}{1}'.format(url, l)

        if l.endswith('/'):
            newkey = l.split('/')[-2]
            d[newkey] = {}
            get_info(newurl, d[newkey])

        else:
            r = requests.get(newurl)
            if r.status_code != 404:
                try:
                    d[l] = json.loads(r.text)
                except ValueError:
                    d[l] = r.text
            else:
                d[l] = None



if __name__ == '__main__':
    print(json.dumps(load()))
