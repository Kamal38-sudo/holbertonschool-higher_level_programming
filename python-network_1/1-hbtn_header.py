#!/usr/bin/python3
"""
1-hbtn_header.py

This script takes in a URL, sends a HTTP request to the URL,
and displays the value of the X-Request-Id variable found in
the header of the response.

Usage:
    ./1-hbtn_header.py <URL>

Example:
    ./1-hbtn_header.py https://intranet.hbtn.io
"""

import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    # Get the X-Request-Id header
    x_request_id = response.getheader("X-Request-Id")
    print(x_request_id)

