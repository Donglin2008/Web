"""定义blog的url模式"""

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
]