#!/usr/bin/python
"""
The goal of this little script is to get configuration from django-smokeping
 It take one argument: the url of django-smokping app (ex: http://localhost:8000/smokeping)
 run it from your smokeping's config.d directory
"""
import urllib2
from os import chmod
from sys import argv

admin_url = argv[1]

def get_snippet(view):
    url = '/'.join([admin_url, view])
    try:
        snippet = urllib2.urlopen(url).read()
        ret_val = snippet
    except:
        ret_val = False

    return ret_val

for view in ['targets', 'alerts', 'parents', 'slaves', 'probes', 'secrets']:
    snippet = get_snippet(view)
    if snippet:
        f = open(view + '.conf', 'w')
        f.write(snippet)
        f.close
    else:
        print 'Unable to get %s configuration' % view


chmod('secrets.conf', 00600)
