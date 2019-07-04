#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import socket

import requests
import requests.packages.urllib3.util.connection as urllib3_cn
from bs4 import BeautifulSoup as bs


def allowed_gai_family():
    return socket.AF_INET  # force ipv4


urllib3_cn.allowed_gai_family = allowed_gai_family
base = 'https://news.tsinghua.edu.cn/'
index = 'publish/thunews/%d/index.html'
index_s = 'publish/thunews/%d/index_%d.html'
cats = {'头条新闻': 9648, '综合新闻': 10303, '要闻聚焦': 9649, '媒体清华': 9650}

news = {}

for cat, c in cats.items():
    urls = []

    entry = requests.get(base + index % c)
    entry.encoding = entry.apparent_encoding
    i = 1
    while entry.status_code == 200:
        soup = bs(entry.text, 'lxml')
        figs = soup.find_all('figcaption')
        if figs == []:
            figs = soup.find_all('h3')
        for fig in figs:
            for a in fig.contents:
                href = a.get('href')
                if href:
                    url = base + href
                    urls.append(url)

        i += 1
        entry = requests.get(base + index_s % (c, i))

    news[cat] = urls
    print('%s: %d' % (cat, len(urls)))

with open('urls.json', 'w', encoding='utf-8') as f:
    json.dump(news, f, ensure_ascii=False)
