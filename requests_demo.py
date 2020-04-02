import requests


URI_IP = 'http://127.0.0.1:5000/ip'
URI_GET = 'http://127.0.0.1:5000/get'


def use_simple_requests():
    response = requests.get(URI_IP)
    print('>>>Response Headers:')
    print(response.headers)
    print('>>>Response Body:')
    print(response.text)


def use_params_requests():
    params = {'param1': 'hello', 'param2': 'world'}
    response = requests.get(URI_IP, params=params)
    print('>>>Response Headers:')
    print(response.headers)
    print('>>>Status Code:')
    print(response.status_code)
    print(response.reason)
    print('>>>Response Body:')
    print(response.json)



if __name__ == '__main__':
    print('>>>Use simple requests:')
    use_simple_requests()
    print('-----------')
    print('>>>Use params requests:')
    use_params_requests()