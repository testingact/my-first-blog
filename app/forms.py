from django import forms
from .models import Crawling

'''
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


option_choices = (
        ('ss', 'dddd'),
        ('aaa', 'efq')
    )
'''
class crawling_info(forms.ModelForm):
    ck_naver = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Crawling.option_naver
    )
    ck_daum = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Crawling.option_daum
    )
    class Meta:
        model = Crawling
        fields = ('keyword', 'article_count',)
