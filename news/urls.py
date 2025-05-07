from django.urls import path
from news.views import homepage,detail,category_func


urlpatterns = [
    path('',homepage,name='home'),
    path('news/<int:id>/',detail,name='detail'),
    path('category/<int:id>/',category_func,name='category')
]
