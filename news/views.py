from django.shortcuts import render,get_object_or_404
from .models import News

# Create your views here.
def homepage(request):
    posts = News.objects.all()
    return render(request,'index.html',{'posts':posts})

def detail(request,id):
    news = get_object_or_404(News,id=id)
    return render(request,'detail.html',{'abc':news})