from django import forms
from django.contrib.auth.models import User
from .models import *


class CommentreviewForm(forms.ModelForm):

    class Meta:
        model = Reviewcomment
        fields = ('text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class BannerUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['RestuarantName','Banner', 'menu1','menu2','menu3','menu4', 'lowprice', 'highprice',
        'tel','address', 'parking','wifi','googlemap','content', 'foodpanda', 'grab', 'openday','closeday'
        ,'is_thaifood','is_japanfood','is_chinesefood','is_northfood','is_noodlefood','is_buffetfood'
        ,'is_fastfood','is_somtumfood','is_cafefood','is_southfood']


class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Reviewpost
        fields = ['title','image', 'pic1','pic2','pic3','pic4', 'content','address','googlemap']

        