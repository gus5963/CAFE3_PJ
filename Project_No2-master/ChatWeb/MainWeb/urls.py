from django.contrib import admin
from django.urls    import path, include
from MainWeb        import views


urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('test/', views.test, name='test'),
    path('chattrain', views.chattrain, name='chattrain'),
    path('chatanswer', views.chatanswer, name='chatanswer'),
    path('example', views.example, name='example'),
    path('example2', views.example2, name='example2'),
    path('getLocate',views.getLocate, name='getLocate')
]