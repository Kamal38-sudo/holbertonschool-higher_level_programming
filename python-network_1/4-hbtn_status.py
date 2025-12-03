#!/usr/bin/python3
"""salam"""
import requests

url = "https://intranet.hbtn.io/status"
response = requests.get(url)
print(response)
