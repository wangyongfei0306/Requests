import json

import exception as exception
import requests
from requests import exceptions

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def request_method():
    response = requests.get(build_uri('users/imoocdemo'))
    print(better_print(response.text))

def params_request():
    response = requests.get(build_uri('users'), params={'since': 11})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.url)

def json_request():
    response = requests.patch(build_uri('user'), auth=('******', '******'),
                              json={'name': 'baby'})
    print(better_print(response.text))

def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=0.1)
    except exceptions.Timeout as e:
        print(e)
    else:
        print(response.text)


if __name__ == '__main__':
    # request_method()
    # params_request()
    # json_request()
    timeout_request()
    pass