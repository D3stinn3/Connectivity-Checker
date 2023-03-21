#!/usr/bin/python3

from http.client import HTTPConnection
from urllib.parse import urlparse

"""Site Connectivity Check Function"""

def site_iko_online(url, timeout=2):
    """Returns 'True' if the target endpoint is online.
    Raise an exception otherwise"""
    error = Exception("Error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443, 8000):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error

            