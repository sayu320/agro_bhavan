from django.urls import path
from.import views
urlpatterns=[
    path('view_schemes',views.view_schemes),
    path('products',views.products),
    path('apply_now/<int:id>',views.apply_now),
    path('fy_apply_now',views.fy_apply_now),
    path('view_subscheme/<int:id>',views.view_subscheme),
    path('req_query',views.req_query),
    path('view_products',views.view_products),
    path('book_prod/<int:id>',views.book_prod),
    path('news',views.news),
    path('profile',views.profile),
    path('apply_ele/<int:id>',views.apply_ele),
    path('apply_pen/<int:id>',views.apply_pen),
    path('apply_SHM/<int:id>',views.apply_SHM),
    path('apply_PMK/<int:id>',views.apply_PMK)
    
    
]