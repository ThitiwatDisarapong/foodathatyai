from django.contrib import admin
from .models import Post, Comment, Reviewpost, Reviewcomment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reviewpost)
admin.site.register(Reviewcomment)

