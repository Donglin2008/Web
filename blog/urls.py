"""定义blog的url模式"""

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 查看已有笔记
    path('blog/<int:blog_id>/', views.blog, name='blog'),
    # 新建笔记
    path('new_blog/', views.new_blog, name='new_blog'),
    # 编辑已有笔记
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    # 个人博客首页
    path('blogs/', views.blogs, name='blogs'),
    # 介绍
    path('about/', views.about, name='about'),
]