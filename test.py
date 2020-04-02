import urllib.request, urllib3


URI_IP = 'http://127.0.0.1:5000'

def use_simple_urllib2():
    response = urllib.request.urlopen(URI_IP)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    # print(''.join([line for line in response.readlines()]))
    print(response.status)


if __name__ == '__main__':
    print('>>>Use simple urllib')
    use_simple_urllib2()