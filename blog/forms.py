from django import forms
from django.contrib.auth.models import User
from .models import *


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class BannerUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['RestuarantName','tag', 'Banner', 'menu1','menu2','menu3','menu4', 'lowprice', 'highprice',
        'tel','address', 'parking','wifi','googlemap','content', 'foodpanda', 'grab', 'openday','closeday']


class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Reviewpost
        fields = ['title','image', 'pic1','pic2','pic3','pic4', 'content','address','googlemap']
        