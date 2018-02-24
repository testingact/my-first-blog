from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField

'''
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
'''
class Crawling(models.Model):
    keyword = models.CharField(max_length=10)
    article_count = models.IntegerField(default=5)
    naver_blog = models.TextField(null=True)
    naver_news = models.TextField(null=True)
    naver_cafe = models.TextField(null=True)
    daum_blog = models.TextField(null=True)
    daum_web = models.TextField(null=True)
    daum_cafe = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    option_naver = (
        ('naver_all', '전체'),
        ('naver_blog', '블로그'),
        ('naver_news', '뉴스'),
        ('naver_cafe', '카페')
    )
    option_daum = (
        ('daum_all', '전체'),
        ('daum_blog', '블로그'),
        ('daum_web', '웹'),
        ('daum_cafe', '카페')
    )
    #checkbox = models.CharField(max_length=10, choices=option_choices)

    def __str__(self):
        return self.keyword
