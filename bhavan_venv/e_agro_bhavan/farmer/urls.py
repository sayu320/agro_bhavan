from django.urls import path
from.import views
urlpatterns=[
    path('farmer',views.farmer),
    path('webpage',views.webpage),
    path('',views.index),
    path('contact',views.contact),
    path('about',views.about),
    path('register',views.register),
    path('officer',views.officer),
    path('shop_register',views.shops),
    path('login',views.login),
    path('logout',views.logout),
    path('view_officers',views.view_officers),
    path('forgot_password',views.forgot_password),
    
]