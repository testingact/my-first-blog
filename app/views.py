from django.utils import timezone
from .models import Crawling
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from .forms import crawling_info
import json
import csv
import pandas
import blog_test.crawling_daum
import blog_test.crawling_naver
import blog_test.freq
from konlpy.tag import Twitter
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import matplotlib
plt.switch_backend('agg')

# Create your views here.
def menu(request):

    return render(request, 'blog_test/menu.html')

def setting(request):
    if request.method == "POST":
        form = crawling_info(request.POST)
        naver = request.POST.getlist('ck_naver')
        daum = request.POST.getlist('ck_daum')
        if naver and daum:
            crawling = form.save(commit=False)
            if 'naver_all' in naver:
                naver_blog_result = blog_test.crawling_naver.blog_result(crawling.keyword, crawling.article_count)
                naver_news_result = blog_test.crawling_naver.news_result(crawling.keyword, crawling.article_count)
                naver_cafe_result = blog_test.crawling_naver.cafe_result(crawling.keyword, crawling.article_count)
                crawling.naver_blog = json.dumps(naver_blog_result, ensure_ascii=False)
                crawling.naver_news = json.dumps(naver_news_result, ensure_ascii=False)
                crawling.naver_cafe = json.dumps(naver_cafe_result, ensure_ascii=False)
            if 'daum_all' in daum:

                daum_blog_result = blog_test.crawling_daum.blog_result(crawling.keyword, crawling.article_count)
                daum_web_result = blog_test.crawling_daum.web_result(crawling.keyword, crawling.article_count)
                daum_cafe_result = blog_test.crawling_daum.cafe_result(crawling.keyword, crawling.article_count)
                crawling.daum_blog = json.dumps(daum_blog_result, ensure_ascii=False)
                crawling.daum_web = json.dumps(daum_web_result, ensure_ascii=False)
                crawling.daum_cafe = json.dumps(daum_cafe_result, ensure_ascii=False)
                #crawling.save()

            if 'naver_blog' in naver:
                #crawling = form.save(commit=False)
                naver_blog_result = blog_test.crawling_naver.blog_result(crawling.keyword,
                                                                         crawling.article_count)
                crawling.naver_blog = json.dumps(naver_blog_result, ensure_ascii=False)
                #crawling.save()
                #return redirect('result_detail', pk=crawling.pk)
            if 'naver_news' in naver:
                #crawling = form.save(commit=False)
                naver_news_result = blog_test.crawling_naver.news_result(crawling.keyword,
                                                                         crawling.article_count)
                crawling.naver_news = json.dumps(naver_news_result, ensure_ascii=False)
                #crawling.save()
                #return redirect('result_detail', pk=crawling.pk)
            if 'naver_cafe' in naver:
                #crawling = form.save(commit=False)
                naver_cafe_result = blog_test.crawling_naver.cafe_result(crawling.keyword,
                                                                         crawling.article_count)
                crawling.naver_cafe = json.dumps(naver_cafe_result, ensure_ascii=False)
                #crawling.save()
                #return redirect('result_detail', pk=crawling.pk)
            if 'daum_blog' in daum:
                #crawling = form.save(commit=False)
                daum_blog_result = blog_test.crawling_daum.blog_result(crawling.keyword, crawling.article_count)
                crawling.daum_blog = json.dumps(daum_blog_result, ensure_ascii=False)
                #crawling.save()
                #return redirect('result_detail', pk=crawling.pk)
            if 'daum_web' in daum:
                #crawling = form.save(commit=False)
                daum_web_result = blog_test.crawling_daum.web_result(crawling.keyword, crawling.article_count)
                crawling.daum_web = json.dumps(daum_web_result, ensure_ascii=False)
                #crawling.save()
                #return redirect('result_detail', pk=crawling.pk)
            if 'daum_cafe' in daum:
                #crawling = form.save(commit=False)
                daum_cafe_result = blog_test.crawling_daum.cafe_result(crawling.keyword, crawling.article_count)
                crawling.daum_cafe = json.dumps(daum_cafe_result, ensure_ascii=False)
                #crawling.save()
                #return redirect('result_detail', pk=crawling.pk)
            crawling.save()
            return redirect('result_detail', pk=crawling.pk)
        else:
            if naver and not daum:
                if 'naver_all' in naver:
                    crawling = form.save(commit=False)
                    naver_blog_result = blog_test.crawling_naver.blog_result(crawling.keyword, crawling.article_count)
                    naver_news_result = blog_test.crawling_naver.news_result(crawling.keyword, crawling.article_count)
                    naver_cafe_result = blog_test.crawling_naver.cafe_result(crawling.keyword, crawling.article_count)
                    crawling.naver_blog = json.dumps(naver_blog_result, ensure_ascii=False)
                    crawling.naver_news = json.dumps(naver_news_result, ensure_ascii=False)
                    crawling.naver_cafe = json.dumps(naver_cafe_result, ensure_ascii=False)
                    crawling.save()
                    return redirect('result_detail', pk=crawling.pk)
                else:
                    if 'naver_blog' in naver and 'naver_news' in naver:
                        crawling = form.save(commit=False)
                        naver_blog_result = blog_test.crawling_naver.blog_result(crawling.keyword,
                                                                                 crawling.article_count)
                        naver_news_result = blog_test.crawling_naver.news_result(crawling.keyword,
                                                                                 crawling.article_count)
                        crawling.naver_blog = json.dumps(naver_blog_result, ensure_ascii=False)
                        crawling.naver_news = json.dumps(naver_news_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
                    elif 'naver_news' in naver and 'naver_cafe' in naver:
                        crawling = form.save(commit=False)
                        naver_news_result = blog_test.crawling_naver.news_result(crawling.keyword,
                                                                                 crawling.article_count)
                        naver_cafe_result = blog_test.crawling_naver.cafe_result(crawling.keyword,
                                                                                 crawling.article_count)
                        crawling.naver_news = json.dumps(naver_news_result, ensure_ascii=False)
                        crawling.naver_cafe = json.dumps(naver_cafe_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
                    elif 'naver_blog' in naver and 'naver_cafe' in naver:
                        crawling = form.save(commit=False)
                        naver_blog_result = blog_test.crawling_naver.blog_result(crawling.keyword,
                                                                                 crawling.article_count)
                        naver_cafe_result = blog_test.crawling_naver.cafe_result(crawling.keyword,
                                                                                 crawling.article_count)
                        crawling.naver_blog = json.dumps(naver_blog_result, ensure_ascii=False)
                        crawling.naver_cafe = json.dumps(naver_cafe_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
                    elif 'naver_blog' in naver:
                        crawling = form.save(commit=False)
                        naver_blog_result = blog_test.crawling_naver.blog_result(crawling.keyword,
                                                                                 crawling.article_count)
                        crawling.naver_blog = json.dumps(naver_blog_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
                    elif 'naver_news' in naver:
                        crawling = form.save(commit=False)
                        naver_news_result = blog_test.crawling_naver.news_result(crawling.keyword,
                                                                                 crawling.article_count)
                        crawling.naver_news = json.dumps(naver_news_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
                    else:
                        crawling = form.save(commit=False)
                        naver_cafe_result = blog_test.crawling_naver.cafe_result(crawling.keyword,
                                                                                 crawling.article_count)
                        crawling.naver_cafe = json.dumps(naver_cafe_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
            elif not naver and daum:
                if 'daum_all' in daum:
                    crawling = form.save(commit=False)
                    daum_blog_result = blog_test.crawling_daum.blog_result(crawling.keyword, crawling.article_count)
                    daum_web_result = blog_test.crawling_daum.web_result(crawling.keyword, crawling.article_count)
                    daum_cafe_result = blog_test.crawling_daum.cafe_result(crawling.keyword, crawling.article_count)
                    crawling.daum_blog = json.dumps(daum_blog_result, ensure_ascii=False)
                    crawling.daum_web = json.dumps(daum_web_result, ensure_ascii=False)
                    crawling.daum_cafe = json.dumps(daum_cafe_result, ensure_ascii=False)
                    crawling.save()
                    return redirect('result_detail', pk=crawling.pk)
                else:
                    if 'daum_blog' in daum and 'daum_web' in daum:
                        crawling = form.save(commit=False)
                        daum_blog_result = blog_test.crawling_daum.blog_result(crawling.keyword, crawling.article_count)
                        daum_web_result = blog_test.crawling_daum.web_result(crawling.keyword, crawling.article_count)
                        crawling.daum_blog = json.dumps(daum_blog_result, ensure_ascii=False)
                        crawling.daum_web = json.dumps(daum_web_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
                    elif 'daum_web' in daum and 'daum_cafe' in daum:
                        crawling = form.save(commit=False)
                        daum_web_result = blog_test.crawling_daum.web_result(crawling.keyword, crawling.article_count)
                        daum_cafe_result = blog_test.crawling_daum.cafe_result(crawling.keyword, crawling.article_count)
                        crawling.daum_web = json.dumps(daum_web_result, ensure_ascii=False)
                        crawling.daum_cafe = json.dumps(daum_cafe_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
                    elif 'daum_blog' in daum and 'daum_cafe' in daum:
                        crawling = form.save(commit=False)
                        daum_blog_result = blog_test.crawling_daum.blog_result(crawling.keyword, crawling.article_count)
                        daum_cafe_result = blog_test.crawling_daum.cafe_result(crawling.keyword, crawling.article_count)
                        crawling.daum_blog = json.dumps(daum_blog_result, ensure_ascii=False)
                        crawling.daum_cafe = json.dumps(daum_cafe_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
                    elif 'daum_blog' in daum:
                        crawling = form.save(commit=False)
                        daum_blog_result = blog_test.crawling_daum.blog_result(crawling.keyword, crawling.article_count)
                        crawling.daum_blog = json.dumps(daum_blog_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
                    elif 'daum_web' in daum:
                        crawling = form.save(commit=False)
                        daum_web_result = blog_test.crawling_daum.web_result(crawling.keyword, crawling.article_count)
                        crawling.daum_web = json.dumps(daum_web_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
                    else:
                        crawling = form.save(commit=False)
                        daum_cafe_result = blog_test.crawling_daum.cafe_result(crawling.keyword, crawling.article_count)
                        crawling.daum_cafe = json.dumps(daum_cafe_result, ensure_ascii=False)
                        crawling.save()
                        return redirect('result_detail', pk=crawling.pk)
    else:
        form = crawling_info()
        return render(request, 'blog_test/setting.html', {'form': form})

def crawling_list(request):
    crawling_list = Crawling.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog_test/crawling_list.html', {'crawling_list': crawling_list})

def export_csv(request, pk):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    list = ['주소', '타이틀', '본문']
    writer.writerow(list)

    crawling = get_object_or_404(Crawling, pk=pk)
    jsondec = json.decoder.JSONDecoder()
    csv_list = []
    if crawling.naver_blog:
        naver_blog = jsondec.decode(crawling.naver_blog)
        for i in naver_blog:
            csv_list.append(i)
    if crawling.naver_news:
        naver_news = jsondec.decode(crawling.naver_news)
        for i in naver_news:
            csv_list.append(i)
    if crawling.naver_cafe:
        naver_cafe = jsondec.decode(crawling.naver_cafe)
        for i in naver_cafe:
            csv_list.append(i)
    if crawling.daum_blog:
        daum_blog = jsondec.decode(crawling.daum_blog)
        for i in daum_blog:
            csv_list.append(i)
    if crawling.daum_web:
        daum_web = jsondec.decode(crawling.daum_web)
        for i in daum_web:
            csv_list.append(i)
    if crawling.daum_cafe:
        daum_cafe = jsondec.decode(crawling.daum_cafe)
        for i in daum_cafe:
            csv_list.append(i)

    for row in csv_list:
        writer.writerow(row)

    return response

def result_detail(request, pk):
    crawlings = get_object_or_404(Crawling, pk=pk)
    jsondec = json.decoder.JSONDecoder()
    if  crawlings.naver_blog == None:
        naver_blog_result = ''
    else:
        naver_blog_result = jsondec.decode(crawlings.naver_blog)
    if  crawlings.naver_news == None:
        naver_news_result = ''
    else:
        naver_news_result = jsondec.decode(crawlings.naver_news)
    if  crawlings.naver_cafe == None:
        naver_cafe_result = ''
    else:
        naver_cafe_result = jsondec.decode(crawlings.naver_cafe)
    if crawlings.daum_blog == None:
        daum_blog_result = ''
    else:
        daum_blog_result = jsondec.decode(crawlings.daum_blog)
    if crawlings.daum_web == None:
        daum_web_result = ''
    else:
        daum_web_result = jsondec.decode(crawlings.daum_web)
    if crawlings.daum_cafe == None:
        daum_cafe_result = ''
    else:
        daum_cafe_result = jsondec.decode(crawlings.daum_cafe)
    return render(request, 'blog_test/result_detail.html',
                  {'crawlings': crawlings, 'naver_blog_result': naver_blog_result, 'naver_news_result': naver_news_result,
                   'naver_cafe_result': naver_cafe_result, 'daum_blog_result': daum_blog_result, 'daum_web_result': daum_web_result,
                   'daum_cafe_result': daum_cafe_result})

def file_input(request):
    
    
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        file = pandas.read_csv(csvfile, delimiter=',', encoding='utf-8')
        words = []
        words = file['본문'].tolist()
        word = ' '.join(words)
        spliter = Twitter()
        nouns = spliter.nouns(word)
        count = Counter(nouns)
        df = pd.DataFrame(columns=["word", "freq"])
        for n, c in count.most_common(50):
            df.loc[len(df)] = [n, c]
        fig = plt.figure(figsize=(7,7))
        plt.barh(range(0, len(df)), df['freq'])
        plt.yticks(range(0, len(df)), df['word'])
        #plt.gca().invert_yaxis()
        #plt.xticks(rotation=45)
        #df.plot(kind='bar', x='word', y='freq', color='grey', legend=None)
        fig_html = mpld3.fig_to_html(fig)
        return render_to_response('blog_test/file_input.html', {'figure': fig_html})
    #list = ['평창', '동계', '올림픽']
    return render(request, 'blog_test/file_input.html', locals())

'''
#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    post2 = Crawling.objects.filter(time__lte=timezone.now()).order_by('-time')
#    return render(request, 'blog_test/post_list.html', {'posts': posts, 'post2': post2})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_test/post_detail.html', {'post': post})

#def search_form(request):
     #return render_to_response('blog_test/search_form.html')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog_test/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_test/post_edit.html', {'form': form})
'''


'''
def crawling_input(request):
    if request.method == "POST":
        form = crawling_info(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.generate()
            naver = blog_test.crawling_naver.naver_news(post.keyword, 5)
            daum = blog_test.crawling_daum.daum_blog(post.keyword, 5)
            naver_result = blog_test.crawling_naver.list(naver)
            daum_result = blog_test.crawling_daum.list(daum)

            #text = main(['crawling_naver', 1, post.keyword, 0, 0, 0, 3, '2018.01.30', '2018.02.01', 2, 'example.txt'])
            post.naver_result = json.dumps(naver_result, ensure_ascii=False)
            post.daum_result = json.dumps(daum_result, ensure_ascii=False)
            #post.text = 'ddd'
            #post.text = '굿'
            post.save()
            #Crawling.objects.create(keyword = post.keyword, text = '굿')
            return redirect('setting')
    else:
        form = crawling_info()
    return render(request, 'blog_test/crawling_input_keyword.html', {'form': form})
'''
#def crawling_list(request):
#    post2 = Post.objects.filter(time__lte=timezone.now()).order_by('time')
#    return render(request, 'blog_test/post_list.html', {'post2': post2})

'''
def crawling_detail(request, pk):
    crawlings = get_object_or_404(Crawling, pk=pk)
    jsondec = json.decoder.JSONDecoder()
    naver_url = crawlings.naver_url
    urllist = jsondec.decode(naver_url)
    titlelist = jsondec.decode(crawlings.naver_title)
    #contentlist = jsondec.decode(crawlings.content)
    #crawling = main(['crawling_naver', 1, crawlings.keyword, 0, 0, 0, 3, '2018.01.30', '2018.02.01', 2, 'example.txt'])
    return render(request, 'blog_test/crawling_detail.html', {'crawlings': crawlings, 'urllist': urllist, 'titlelist': titlelist})
'''
#def index(request):
 #   val = User.objects.all()
  #  return render(request, 'blog_test/search_form.html', {'val':val})


