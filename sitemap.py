import ast
import wddx
import requests
import json
import urllib2
import urllib
import datetime
import re
import HTMLParser
import os
import csv
import unicodedata
import string
import simplejson
from collections import Counter
import time
from lxml import etree
import pytz
from datetime import datetime
import random
import json
import json

XHTML_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML = "{%s}" % XHTML_NAMESPACE

NSMAP = {None : XHTML_NAMESPACE} # the default namespace (no prefix)

root = etree.Element(XHTML + "urlset", nsmap=NSMAP)

# Add a site to the sitemap. The function takes 3 parameters (url to add, priority from 0-1, frequency of page update) 
def add_site(url, priority, freq):

    curr_url = etree.Element('url')

    loc = etree.Element('loc')
    loc.text = url

    freq = etree.Element('changefreq')
    # Set frequency of page update
    freq.text = freq

    last = etree.Element('lastmod')
    # Get a randomized timestamp from today
    time = str(datetime.utcnow().replace(tzinfo = pytz.utc)).replace(' ','T')
    raw_t = time.split(':')[0]
    raw_offset = time.split('+')[1]
    ran_m = str(random.randint(10,59))
    ran_s = str(random.randint(10,59))
    ran_h = str(random.randint(10,23))
    new_t = raw_t.split('T')[0]+"T"+ran_h+":"+ran_m+":"+ran_s+"+"+raw_offset
    # set last modified date
    last.text = new_t

    prio = etree.Element('priority')
    prio.text = priority

    curr_url.append(loc)
    curr_url.append(freq)
    curr_url.append(last)
    curr_url.append(prio)
    root.append(curr_url)


# Add some urls to the sitemap via: add_site(url, priority from 0-1, frequency of page update)
add_site("http://example.com/", "1.0", "daily")
add_site("http://example.com/parameter", "0.8", "weekly")
add_site("http://example.com/parameter/cats", "0.7", "hourly")

s = etree.tostring(root, pretty_print=True)

# Save to Disk
with open('/root/path-to-save/sitemap.xml', 'w') as outfile:
    outfile.write(s)

