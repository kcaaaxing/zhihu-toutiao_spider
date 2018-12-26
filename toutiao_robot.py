import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    base_url = 'https://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params)
    try:  # 验证
        response = requests.get(url)
        if codes.ok == response.status_code:
            return response.json()
    except requests.ConnectionError:
        return 651  # 验证


def get_images(json):
    if json.get('data'):
        # print(json.get('data'))
        for item in json.get('data'):
            # print(item)
            if item.get('cell_type') is not None:
                # print('hello')
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {  # 验证
                    'image': 'https:' + image.get('url'),
                    'title': title
                }


def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')  # os.path.sep, 是设置网页地址的间隔符
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(img_path, md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):  # 验证
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 7

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
