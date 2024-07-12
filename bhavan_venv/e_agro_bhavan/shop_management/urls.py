from django.urls import path
from.import views
urlpatterns=[
    path('prod',views.prod),
    path('view_add_prod',views.view_add_prod),
    path('edit_add_prod',views.edit_add_prod),
    path('profile',views.profile)
]