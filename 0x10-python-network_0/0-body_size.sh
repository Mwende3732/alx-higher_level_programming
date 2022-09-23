#!/bin/bash
# takes in a URL, sends a request to that URL
curl -H "$1" | wc -c
