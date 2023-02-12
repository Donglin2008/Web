"""定义learning的url模式"""

from django.urls import path, include

from . import views

app_name = 'learning'
urlpatterns = [
    path('learning/', views.index, name='learning'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('entry/<int:entry_id>/', views.entry, name='entry'),
]
