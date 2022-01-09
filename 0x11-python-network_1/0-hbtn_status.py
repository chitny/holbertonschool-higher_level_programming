#!/usr/bin/python3
"""0. What's my status? #0"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\N{tab}- type: {}'.format(type(html)))
        print('\N{tab}- content: {}'.format(html))
        print('\N{tab}- utf8 content: {}'.format(html.decode("utf-8", "replace")))
