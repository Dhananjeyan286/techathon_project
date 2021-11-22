from os import name
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.start,name='start'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('sigin_redirect',views.signin_redirect,name='sigin_redirect'),
    path('changepass',views.forgot_pass,name='forgot_pass'),
    path('send_otp',views.send_otp,name='send_otp'),
    path('check_otp',views.validate_otp,name='validate_otp'),
    path('request_changepass',views.request_changepass,name='request_changepass'),
    path('new_pass',views.new_pass,name='new_pass'),
    path('home_page',views.home_page,name='home_page'),
    path('users_details',views.user_details,name='user_details'),
    path('logout',views.logout,name='logout'),
    path('change',views.change,name='change'),
    path('change_user',views.change_user,name='change_user'),
    path('decline_user',views.decline_user,name='decline_user')
    
]
