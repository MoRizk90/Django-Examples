from django.urls import re_path,path
from basic_app import views


app_name = 'basic_app'

urlpatterns = [

    # re_path(r'^$', views.index, name='index'),
    path('index/',views.index,name='index'),
    path('user_login/',views.user_login,name='user_login'),
    path('register/', views.register, name='register'),
    # re_path(r'^relative',views.relative_Temp,name = 'relative')

]
