from django.urls import path
from news.views import homepage,detail


urlpatterns = [
    path('',homepage,name='home'),
    path('news/<int:id>/',detail,name='detail')
]
