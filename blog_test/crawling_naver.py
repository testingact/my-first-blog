import os
import sys
import urllib.request
import ast
import pprint
import json

client_id = "Iybik9u8bJ6S9cZLHzWx"
client_secret = "QcrgPnh4oi"
url_incomplete = "https://openapi.naver.com/v1/search/"

def requests_naver(category, keyword, sort, size):
    search_word = urllib.parse.quote(keyword)
    url = url_incomplete + category + "?query=" + \
          search_word + "&sort=" + sort + "&display=" + str(size)
    return url

def naver_blog(keyword, size):

    url = requests_naver('blog', keyword, "sim", size)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = ast.literal_eval(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    return result

def naver_news(keyword, size):

    url = requests_naver('news', keyword, "sim", size)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = ast.literal_eval(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    return result

def naver_cafe(keyword, size):

    url = requests_naver('cafearticle', keyword, "sim", size)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = ast.literal_eval(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    return result

def naver_kin(keyword, size):

    url = requests_naver('kin', keyword, "sim", size)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = ast.literal_eval(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    return result

def url_list(result):
    urllist = []
    article_counts = len(result['items'])
    for i in range(0, article_counts):
        url = (result['items'][i]['link'])
        urllist.append(url)
    return urllist

def title_list(result):
    titlelist = []
    article_counts = len(result['items'])
    for i in range(0, article_counts):
        title = (result['items'][i]['title'])
        titlelist.append(title)
    return titlelist

def content_list(result):
    contentlist = []
    article_counts = len(result['items'])
    for i in range(0, article_counts):
        content = (result['items'][i]['description'])
        contentlist.append(content)
    return contentlist

def list(result):
    list = []
    article_counts = len(result['items'])
    for i in range(0, article_counts):
        url = (result['items'][i]['link'])
        title = (result['items'][i]['title'])
        content = (result['items'][i]['description'])
        row = [url, title, content]
        list.append(row)
    return list

def all_result(keyword, size):
    cafe = naver_cafe(keyword, size)
    news = naver_news(keyword, size)
    blog = naver_blog(keyword, size)
    cafe_result = list(cafe)
    news_result = list(news)
    blog_result = list(blog)
    all_result = []
    for p in blog_result:
        all_result.append(p)
    for j in news_result:
        all_result.append(j)
    for i in cafe_result:
        all_result.append(i)
    return all_result

def blog_news_result(keyword, size):
    news = naver_news(keyword, size)
    blog = naver_blog(keyword, size)
    news_result = list(news)
    blog_result = list(blog)
    all_result = []
    for j in blog_result:
        all_result.append(j)
    for i in news_result:
        all_result.append(i)
    return all_result

def blog_cafe_result(keyword, size):
    cafe = naver_cafe(keyword, size)
    blog = naver_blog(keyword, size)
    cafe_result = list(cafe)
    blog_result = list(blog)
    all_result = []
    for p in blog_result:
        all_result.append(p)
    for i in cafe_result:
        all_result.append(i)
    return all_result

def news_cafe_result(keyword, size):
    cafe = naver_cafe(keyword, size)
    news = naver_news(keyword, size)
    cafe_result = list(cafe)
    news_result = list(news)
    all_result = []
    for p in news_result:
        all_result.append(p)
    for j in cafe_result:
        all_result.append(j)
    return all_result

def blog_result(keyword, size):
    blog = naver_blog(keyword, size)
    blog_result = list(blog)
    all_result = []
    for p in blog_result:
        all_result.append(p)
    return all_result

def news_result(keyword, size):
    news = naver_news(keyword, size)
    news_result = list(news)
    all_result = []
    for j in news_result:
        all_result.append(j)
    return all_result

def cafe_result(keyword, size):
    cafe = naver_cafe(keyword, size)
    cafe_result = list(cafe)
    all_result = []
    for i in cafe_result:
        all_result.append(i)
    return all_result



#result = naver_blog('가상화폐', 5)
#print(len(result))
#print(type(result))
#pprint.pprint(result)



#category = "blog"
#size = 5
#result = naver_news('가상화폐', size)
#print(len(result['items']))
#print(title_list(result))
#pprint.pprint(result['items'])
#save_dir = "C:/Users/user/Desktop/crawling_save/"
#file = open(save_dir+"crawling_ex_naver.txt", 'w', encoding="utf-8")
#for i in range(0, size):
#    file.write(result["items"][i]["description"] + "\n")
#file.close()
'''
category > request parameter
- blog : 블로그 > query display start sort
- news : 뉴스 > query display start sort
- book : 책 > query display start sort
- encyc : 백과사전 > query display start *
- cafearticle : 카페 > query display start sort
- kin : 지식인 > query display start sort
- webkr : 웹문서 > query display start *
- doc : 전문자료 > query display start *
'''