__author__ = 'stephenhsu'

import requests
requests.packages.urllib3.disable_warnings()

try:
    import urlparse
    from urllib import quote as urlquote
    from urllib import urlencode
    from urllib import unquote as urlunquote
except ImportError:
    # Python3
    import urllib.parse as urlparse
    from urllib.parse import quote as urlquote
    from urllib.parse import urlencode
    from urllib.parse import unquote as urlunquote

try:  # pragma no cover
    from collections import OrderedDict
except ImportError:  # pragma no cover
    try:
        from ordereddict import OrderedDict
    except ImportError:
        OrderedDict = dict
