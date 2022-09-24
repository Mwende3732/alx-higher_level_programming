#!/usr/bin/python3
"""This is a Python script that takes in a URL, sends a request to the URL and displays the body of the response i.e
the value of the X-Request-Id variable found in the header
(handling HTTP errors)"""
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))