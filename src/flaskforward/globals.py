"""
********************************************************************************************

https://docs.python-requests.org/en/latest/api/#requests.Request

requests.request parms:
    method:   HTTP method to use.
    url:      URL to send.
    headers:  dictionary of headers to send.
    files:    dictionary of {filename: fileobject} files to multipart upload.
    data:     the body to attach to the request. If a dictionary or list of tuples [(key, value)] is provided,   form-encoding will take place.
    json:     json for the body to attach to the request (if files or data is not specified).
    params:   URL parameters to append to the URL. If a dictionary or list of tuples [(key, value)] is provided, form-encoding will take place.
    auth:     Auth handler or (user, pass) tuple.
    cookies:  dictionary or CookieJar of cookies to attach to this request.
    hooks:    dictionary of callback hooks, for internal usage.

********************************************************************************************
"""

from __future__ import annotations

url     : str                = None
headers : dict               = None
files   : dict               = None
data    : dict | str | bytes = None
params  : dict               = None
auth    : tuple              = None
cookies : dict               = None
hooks   : dict               = None