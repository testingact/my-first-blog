import requests
import pprint
import json

def define(sort, article_count, keyword):
    headers = {'Content-Type': 'application/json; charset=utf-8',
               'Authorization': 'KakaoAK a9656cfb495d4846ba88224bbdf9e6c5'}
    params = {'sort': sort, 'size': article_count, 'query': keyword}
    url = "https://dapi.kakao.com/"
    return headers, params, url

def daum_web(keyword, article_count):
    headers, params, url = define('accuracy', article_count, keyword)
    result = requests.get(url+"v2/search/web", headers=headers, params=params)
    return (result)

def daum_tip(keyword, article_count):
    headers, params, url = define('accuracy', article_count, keyword)
    result = requests.get(url+"v2/search/tip", headers=headers, params=params)
    return (result)

def daum_book(keyword, article_count):
    headers, params, url = define('accuracy', article_count, keyword)
    result = requests.get(url+"v2/search/book", headers=headers, params=params)
    return (result)

def daum_blog(keyword, article_count):
    headers, params, url = define('accuracy', article_count, keyword)
    result = requests.get(url+"v2/search/blog", headers=headers, params=params)
    return (result)

def daum_cafe(keyword, article_count):
    headers, params, url = define('accuracy', article_count, keyword)
    result = requests.get(url+"v2/search/cafe", headers=headers, params=params)
    return(result)

def url_list(result):
    urllist = []
    article_counts = len(result.json()['documents'])
    for i in range(0, article_counts):
        url = (result.json()['documents'][i]['url'])
        urllist.append(url)
    return urllist

def title_list(result):
    titlelist = []
    article_counts = len(result.json()['documents'])
    for i in range(0, article_counts):
        title = (result.json()['documents'][i]['title'])
        titlelist.append(title)
    return titlelist

def content_list(result):
    contentlist = []
    article_counts = len(result.json()['documents'])
    for i in range(0, article_counts):
        content = (result.json()['documents'][i]['contents'])
        contentlist.append(content)
    return contentlist

def list(result):
    list = []
    article_counts = len(result.json()['documents'])
    for i in range(0, article_counts):
        url = (result.json()['documents'][i]['url'])
        title = (result.json()['documents'][i]['title'])
        content = (result.json()['documents'][i]['contents'])
        row = [url, title, content]
        list.append(row)
    return list

def all_result(keyword, size):
    cafe = daum_cafe(keyword, size)
    web = daum_web(keyword, size)
    blog = daum_blog(keyword, size)
    cafe_result = list(cafe)
    web_result = list(web)
    blog_result = list(blog)
    all_result = []
    for p in blog_result:
        all_result.append(p)
    for j in web_result:
        all_result.append(j)
    for i in cafe_result:
        all_result.append(i)
    return all_result

def blog_web_result(keyword, size):
    web = daum_web(keyword, size)
    blog = daum_blog(keyword, size)
    web_result = list(web)
    blog_result = list(blog)
    all_result = []
    for j in blog_result:
        all_result.append(j)
    for i in web_result:
        all_result.append(i)
    return all_result

def web_cafe_result(keyword, size):
    cafe = daum_cafe(keyword, size)
    web = daum_web(keyword, size)
    cafe_result = list(cafe)
    web_result = list(web)
    all_result = []
    for j in web_result:
        all_result.append(j)
    for i in cafe_result:
        all_result.append(i)
    return all_result

def blog_cafe_result(keyword, size):
    cafe = daum_cafe(keyword, size)
    blog = daum_blog(keyword, size)
    cafe_result = list(cafe)
    blog_result = list(blog)
    all_result = []
    for p in blog_result:
        all_result.append(p)
    for i in cafe_result:
        all_result.append(i)
    return all_result

def blog_result(keyword, size):
    blog = daum_blog(keyword, size)
    blog_result = list(blog)
    all_result = []
    for p in blog_result:
        all_result.append(p)
    return all_result

def web_result(keyword, size):
    web = daum_web(keyword, size)
    web_result = list(web)
    all_result = []
    for j in web_result:
        all_result.append(j)
    return all_result

def cafe_result(keyword, size):
    cafe = daum_cafe(keyword, size)
    cafe_result = list(cafe)
    all_result = []
    for i in cafe_result:
        all_result.append(i)
    return all_result


#result = cafe_result('가상화폐', 6)
#print(len(result))
#print(type(result))
#print(result[0][2])


#file = open(save_dir+"crawling_ex.txt", 'w', encoding="utf-8")
#for i in range(0, article_count):
#    file.write(result.json()["documents"][i]["contents"]+"\n")
#file.close()