#!/usr/bin/python3
"""
script sends a request to a URL and displays
the value of the X-Request-Id variable found in the header
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.info()
        request_id = headers.get("X-Request-Id")

        print(request_id)
