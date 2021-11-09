from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class post(models.Model):
    post_img=models.ImageField(upload_to='picture')
    post_date=models.IntegerField()
    post_month=models.CharField(max_length=10)
    post_title=models.TextField()
    post_category=models.TextField()
    post_desc=models.TextField()

class news(models.Model):
    news_img = models.ImageField(upload_to='picture')
    title = models.TextField()
    subtitle = models.TextField()

class home(models.Model):
    home_img = models.ImageField(upload_to='picture')

class testimonial(models.Model):
    t_img = models.ImageField(upload_to='picture')
    client_caption = models.TextField()
    client_name = models.CharField(max_length=20)

class footer(models.Model):
    footer_img = models.ImageField(upload_to='picture')