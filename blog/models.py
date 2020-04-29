from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from multiselectfield import MultiSelectField
from taggit.managers import TaggableManager

Parking_CHOICES= [
    ('มี','มี'),
    ('ไม่มี', 'ไม่มี'),
]

Wifi_CHOICES= [
    ('มี','มี'),
    ('ไม่มี', 'ไม่มี'),
]

Panda_CHOICES= [
    ('มี','มี'),
    ('ไม่มี', 'ไม่มี'),
]

Grab_CHOICES= [
    ('มี','มี'),
    ('ไม่มี', 'ไม่มี'),
]

openday_CHOICES= [
    ('จันทร์','จันทร์'),
    ('อังคาร', 'อังคาร'),
    ('พุธ', 'พุธ'),
    ('พฤหัส', 'พฤหัส'),
    ('ศุกร์', 'ศุกร์'),
    ('เสาร์', 'เสาร์'),
    ('อาทิตย์', 'อาทิตย์'),

]

closeday_CHOICES= [
    ('จันทร์','จันทร์'),
    ('อังคาร', 'อังคาร'),
    ('พุธ', 'พุธ'),
    ('พฤหัส', 'พฤหัส'),
    ('ศุกร์', 'ศุกร์'),
    ('เสาร์', 'เสาร์'),
    ('อาทิตย์', 'อาทิตย์'),
]


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Post(models.Model):
    RestuarantName = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    tag = TaggableManager()
    Banner = models.ImageField(default='default.jpg', upload_to='menu_pics')

    menu1 = models.ImageField(default='default.jpg', upload_to='menu_pics')
    menu2 = models.ImageField(default='default.jpg', upload_to='menu_pics')
    menu3 = models.ImageField(default='default.jpg', upload_to='menu_pics')
    menu4 = models.ImageField(default='default.jpg', upload_to='menu_pics')

    lowprice = models.IntegerField(null='True')
    highprice = models.IntegerField(null='True')

    time = models.TimeField(default="00:00")

    tel = models.CharField(max_length=10, default='')

    parking = models.CharField(max_length=6, choices=Parking_CHOICES, default='มี')

    address = models.CharField(max_length=50, default='')

    wifi = models.CharField(max_length=6, choices=Wifi_CHOICES, default='มี')

    foodpanda = models.CharField(max_length=6, choices=Panda_CHOICES, default='มี')

    grab = models.CharField(max_length=6, choices=Grab_CHOICES, default='มี')

    openday = models.CharField(max_length=10, choices=openday_CHOICES, default='จันทร์')
    
    closeday = models.CharField(max_length=10, choices=closeday_CHOICES, default='อาทิตย์')

    content = models.TextField()

    googlemap = models.CharField(max_length=500, default='https://www.google.com/maps/embed?pb=!1m18......')

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.RestuarantName

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Reviewpost(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    pic1 = models.ImageField(default='default.jpg', upload_to='menu_pics')
    pic2 = models.ImageField(default='default.jpg', upload_to='menu_pics')
    pic3 = models.ImageField(default='default.jpg', upload_to='menu_pics')
    pic4 = models.ImageField(default='default.jpg', upload_to='menu_pics')

    content = models.TextField()

    address = models.CharField(max_length=50, default='')
    googlemap = models.CharField(max_length=500, default='https://www.google.com/maps/embed?pb=!1m18......')

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Reviewcomment(models.Model):
    post = models.ForeignKey('blog.Reviewpost', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text




