from django.urls import path
from.import views
urlpatterns=[
    path('view_user',views.view_user),
    path('approval',views.approval),
    path('appro/<int:id>',views.appro)
   
]