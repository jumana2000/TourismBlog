from django.shortcuts import render
from . models import *
# Create your views here.

def fun(request):
    obj1 = place.objects.all()
    obj2 = post.objects.all()
    obj3 = news.objects.all()
    obj4 = home.objects.all()
    obj5 = testimonial.objects.all()
    obj6 = footer.objects.all()
    return render(request,"index.html",{'results':obj1,'newses':obj2,'sides':obj3,'houses':obj4,'clients':obj5,'foots':obj6})