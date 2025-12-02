#!/usr/bin/python3
"""This task is urllib."""

import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:

x_request_id = response.getheader("x-request-id")
print(x_request_id)
