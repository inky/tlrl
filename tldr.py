#!/usr/bin/env python
from __future__ import with_statement
import httplib, urllib, ConfigParser, os

host, api = 'www.instapaper.com', '/api'
cfgfile=os.path.expanduser('~/.tldr')
cfgsect='Instapaper'

def cred():
    cfg = ConfigParser.RawConfigParser()
    if os.path.isfile(cfgfile):
        cfg.read(cfgfile)
        u, p = cfg.get(cfgsect, 'username'), cfg.get(cfgsect, 'password')
        return [('username', u), ('password', p)]
    else:
        cfg.add_section(cfgsect)
        cfg.set(cfgsect, 'username', '')
        cfg.set(cfgsect, 'password', '')
        with open(cfgfile, 'w') as f:
            cfg.write(f)
        print "Empty configuration file created at", cfgfile

def tldr(url=None):
    params = cred()
    if not params:
        return
    conn = httplib.HTTPSConnection(host)
    conn.set_debuglevel(1)
    api_uri = '/'.join((api, url and 'api' or 'authenticate'))
    if url:
        params.extend([('url', url), ('auto-title', 1)])
    conn.request('GET', '?'.join((api_uri, urllib.urlencode(params))))
    resp = conn.getresponse()
    print resp.status, resp.reason

if __name__ == '__main__':
    tldr()
