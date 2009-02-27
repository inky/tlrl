#!/usr/bin/env python
from __future__ import with_statement
import httplib, urllib, ConfigParser, os

host, api = 'www.instapaper.com', '/api'
cfgfile = os.path.expanduser('~/.tldr')
cfgsect = 'Instapaper'

status = {
    200: 'Username and password are correct!',
    201: 'URL added!',
    403: 'Invalid username or password',
    500: 'The service encountered an error. Please try again later.',
}

def read_cfg():
    cfg = ConfigParser.RawConfigParser()
    if os.path.isfile(cfgfile):
        cfg.read(cfgfile)
        u, p = cfg.get(cfgsect, 'username'), cfg.get(cfgsect, 'password')
        return dict(username=u, password=p)
    else:
        cfg.add_section(cfgsect)
        cfg.set(cfgsect, 'username', '')
        cfg.set(cfgsect, 'password', '')
        with open(cfgfile, 'w') as f:
            cfg.write(f)
        print "Empty configuration file created at", cfgfile

def tldr(credentials, url=None):
    params = credentials.items()
    if not params:
        return
    conn = httplib.HTTPSConnection(host)
    conn.set_debuglevel(1)
    api_uri = '/'.join((api, url and 'api' or 'authenticate'))
    if url:
        params.extend([('url', url), ('auto-title', 1)])
    conn.request('GET', '?'.join((api_uri, urllib.urlencode(params))))
    return conn.getresponse().status

def main()
    cred = read_cfg()
    if cred:
        s = tldr(cred)
        if s in status:
            print status[s]
        elif s:
            print "Bad request. This shouldn't happen -- "\
                  "the program may be out of date."

if __name__ == '__main__':
    main()
