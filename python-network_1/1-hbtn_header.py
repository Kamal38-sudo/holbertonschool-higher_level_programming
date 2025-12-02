#!/usr/bin/python3
"""
1-hbtn_header.py

This script takes in a URL, sends a request to the URL, and displays the
value of the X-Request-Id variable found in the header of the response.

Requirements:
- Must use the packages urllib and sys
- Cannot import packages other than urllib and sys
- The value of X-Request-Id is different for each request
- No need to check arguments passed to the script (number or type)
- Must use a with statement

Usage:
    ./1-hbtn_header.py <URL>

Example:
    $ ./1-hbtn_header.py https://intranet.hbtn.io
    ade2627e-41dd-4c34-b9d9-a0fa0f47b237

    $ ./1-hbtn_header.py https://intranet.hbtn.io
    6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
"""

import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader("X-Request-Id")
    print(x_request_id)
