from django.shortcuts import render,get_object_or_404
from .models import News,Category

# Create your views here.
def homepage(request):
    posts = News.objects.all()
    categories = Category.objects.all()
    return render(request,'index.html',
                  {'posts':posts,
                   'categories':categories})

def detail(request,id):
    news = get_object_or_404(News,id=id)
    categories = Category.objects.all()
    return render(request,'detail.html',
                  {'abc':news,
                    'categories':categories})

def category_func(request,id):
    categories = Category.objects.all()
    news = News.objects.filter(category_id=id)

    return render(request, 'category.html',
                  {'news':news,
                   'categories':categories})