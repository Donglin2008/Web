"""定义users的url模式"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # 包含默认身份验证的url
    path('', include('django.contrib.auth.urls')),
    # 注册
    path('register/', views.register, name='register'),
]