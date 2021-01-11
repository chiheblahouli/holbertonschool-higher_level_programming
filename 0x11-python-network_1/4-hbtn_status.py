#!/usr/bin/python3
"""
script that fetches an url using requests package
"""
import requests

answer = requests.get('https://intranet.hbtn.io/status')
print("Body answer:\n\
\t- type: {}\n\
\t- content: {}".format(type(answer.text), answer.text))
