#!/usr/bin/env python
from __future__ import with_statement
import httplib, urllib, ConfigParser, optparse, os, re, sys

host, api = 'www.instapaper.com', '/api'
cfgfile = os.path.expanduser('~/.tldr')
cfgsect = 'Instapaper'
valid_url = re.compile('^https?://.+$').match
status = {
    200: ('Username and password are correct!', 1),
    201: ('URL added!', 1),
    403: ('Invalid username or password.', 0),
    500: ('The service encountered an error. Please try again later.', 0),
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
    # TODO check for blank username/password
    if url and not valid_url(url):
        sys.stderr.write('URL is invalid.\n')
        return
    params = credentials.items()
    if not params:
        return
    conn = httplib.HTTPSConnection(host)
    api_uri = '/'.join((api, url and 'add' or 'authenticate'))
    if url:
        params.extend([('url', url), ('auto-title', 1)])
    conn.request('GET', '?'.join((api_uri, urllib.urlencode(params))))
    return conn.getresponse().status

def print_result(code):
    if not code or code not in status:
        return
    if status[code][1]:
        print status[code][0]
    else:
        sys.stderr.write(status[code][0] + '\n')

def main():
    cred = read_cfg()
    if not cred:
        return

    op = optparse.OptionParser(usage='usage: %prog URL')
    op.add_option('-a', '--auth', action='store_true', default=False,
                  help='verify your username and password')
    op.set_description('Add URL to Instapaper. The first time this program is run, '\
                       'a new config file is saved in your home folder, with blank '\
                       'entries for your username and password.')
    opts, args = op.parse_args()
    if opts.auth:
        print_result(tldr(cred))
    elif not args:
        op.print_help()
    elif len(args) > 1:
        sys.stderr.write('One URL at a time, please!\n')
    else:
        print_result(tldr(cred, args[0]))

if __name__ == '__main__':
    main()
