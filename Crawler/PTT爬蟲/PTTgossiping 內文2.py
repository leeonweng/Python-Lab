# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 10:21:15 2018

@author: Home love
"""
import requests
from bs4 import BeautifulSoup



URL = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# 取得頁面原始碼
def get_page_content(URL):
    res = requests.get(
    	url=URL,
        cookies={'over18':'1'}
    )
    content = BeautifulSoup(res.text)
    return content
# 取得該版文章總頁數
def get_total_page_num(URL):
    content = get_page_content(URL)
    pagination = content.find('div', {'class':'btn-group-paging'}).findAll('a', {'class':'btn'})
    next_page = pagination[1]['href']
    total_page = next_page.replace('/bbs/Gossiping/index', '')
    total_page = int(total_page[:-5]) + 1
    return total_page
# 取得目前文章列表頁的文章連結
def parse_get_each_row(URL):
    content = get_page_content(URL)
    rows = content.findAll('div',{'class':'r-ent'})
    posts = list()
    for row in rows:
        meta = row.find('div', 'title').find('a')
        if meta :
            posts.append({
                'link': meta['href'],
                'title': meta.text,
                'date': article.find('div', 'date').text,
                'author': article.find('div', 'author').text,
                'push': article.find('div', 'nrec').text
            })
    return posts
# 取得文章內文
def parse_get_article(URL):
    content = get_page_content(URL)
    shift = content.findAll('div',['article-metaline', 'article-metaline-right', 'push'])
    if shift:
        for elem in shift:
            elem = elem.extract()
    main_content = content.find(id='main-content')
    if main_content:
    	content = main_content.text.lstrip().rstrip()
    else:
    	content = 'None'
    return content
# 取得文章列表頁網址
def get_links(total_page, page_want_to_crawl):
    links = list()
    for i in range(total_page, total_page - page_want_to_crawl, -1):
        link = 'https://www.ptt.cc/bbs/Gossiping/index' + str(i) + '.html'
        links.append(link)
    return links

links = get_links(500, 100)
post_meta = list()
for link in links:
    post_meta += parse_get_each_row(link)

contents = list()
for post_meta in all_post_meta:
    content = parse_get_article(post_meta['link'])
    contents.append(article)
if __name__ == '__main__':
    post_links = [entry['link'] for entry in all_post_meta]
    all_post_content = list()
    with Pool(10) as p:
        contents = p.map(parse_get_article, post_links)

all_post = list()
for i in range(len(all_post_meta)):
    all_post.append({
        'title': post_list[i]['title'], 
        'link': post_list[i]['link'], 
        'date': post_list[i]['date'],
        'author': post_list[i]['author'], 
        'push': post_list[i]['push'], 
        'content': contents[i]
    })



