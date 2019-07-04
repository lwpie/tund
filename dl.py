#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import multiprocessing as mp
import socket

import requests
import requests.packages.urllib3.util.connection as urllib3_cn
from bs4 import BeautifulSoup as bs
from tqdm import tqdm


def allowed_gai_family():
    return socket.AF_INET


urllib3_cn.allowed_gai_family = allowed_gai_family


def get_news(url):
    try:
        data = requests.get(url)
        data.encoding = data.apparent_encoding
        if data.status_code == 200:
            soup = bs(data.text, 'lxml')
            title = soup.title.text
            content = '\n'.join([p.text for p in soup.find_all('p')])
            return {'url': url, 'title': title, 'content': content}
        else:
            return None
    except:
        return None


if __name__ == '__main__':
    with open('urls.json', 'r', encoding='utf-8') as f:
        news = json.load(f)

    pool = mp.Pool(8)
    contents = {}
    for cat, urls in news.items():
        print(cat)
        contents[cat] = list(
            tqdm(pool.imap_unordered(get_news, urls), total=len(urls)))

        with open('news.json', 'w', encoding='utf-8') as f:
            json.dump(contents, f, ensure_ascii=False)
