#!/usr/bin/python3
"""1-write_file.py"""
ing to a text file(UTF8) and returns number of cha

def write_file(filename="", text=""):
    """writes a strracters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
