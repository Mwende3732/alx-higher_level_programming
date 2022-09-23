#!/usr/bin/python3
"""This is a python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
     data = urllib.parse.urlencode(value).encode("ascii")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))