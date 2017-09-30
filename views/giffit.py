# -*- coding:utf-8 -*-
import json
import re
import urllib2

from flask import Blueprint

giffit_view = Blueprint('giffit', __name__)


@giffit_view.route('')
def show():
    url = 'https://www.reddit.com/r/gifs/'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    # return "hello world"
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('<a class="title may-blank outbound".*? href="(.*?)".*?>', re.S)
        items = re.findall(pattern, content)
        return json.dumps(items)
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
    except re.error, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
