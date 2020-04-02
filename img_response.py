import requests


def download_img():
    url = 'http://pics.sc.chinaz.com/files/pic/pic9/201509/apic14546.jpg'
    headers = {'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) '
                             'AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 79.0.3945.130 Safari/537.36'}
    response = requests.get(url, headers=headers, stream=True)
    # print(response.status_code, response.reason)
    # print(response.headers)
    # print(response.content)
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


def download_image_improved():
    # 伪造headers信息
    headers = {'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) '
                             'AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 79.0.3945.130 Safari/537.36'}
    # 限定url
    url = 'http://pics.sc.chinaz.com/files/pic/pic9/201509/apic14546.jpg'
    from contextlib import closing
    # 打开一个上下文管理器，最后关上传输流
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        # 打开文件
        with open('demo1.jpg', 'wb') as fd:
            # 每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


# download_img()
download_image_improved()