import requests

BASE_URL = 'https://api.github.com'

def construct_url(endpoint):
    return '/'.join([BASE_URL, endpoint])

def basic_auth():
    """基本认证"""
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print(response.text)
    print(response.request.headers)


basic_auth()