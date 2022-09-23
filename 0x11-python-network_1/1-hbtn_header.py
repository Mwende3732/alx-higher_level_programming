#!/usr/bin/python3
"""a python script that takes in a url, displays the value of the X-request-id variable
found in header response"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(url) as response:
        body = response.info()
        print(body.get("X-Request-Id"))
