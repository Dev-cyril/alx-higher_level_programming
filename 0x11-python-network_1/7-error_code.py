#!/usr/bin/python3
"""
    A module that takes in a URL  sends a request to the URL
    and displays the body of the response (decoded in utf-8).
"""


from urllib.error import HTTPError


if __name__ == '__main__':
    import requests
    from sys import argv

    try:
        req = requests.get(argv[1])
        print(req.text)
    except HTTPError:
        print('Error code: {}'.format(req.status_code))
