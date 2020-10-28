from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('about/' , views.about , name='about'),
    path('birds/' , views.birds_index , name='index'),
    path('birds/<int:bird_id>/' , views.birds_detail , name='detail'),
    path('birds/<int:bird_id>/add_spotting/' , views.add_spotting, name='add_spotting'),
    path('birds/<int:bird_id>/assoc_habitat/<int:habitat_id>/', views.assoc_habitat, name='assoc_habitat'),
    path('birds/<int:bird_id>/remove_habitat/<int:habitat_id>/', views.remove_habitat, name='remove_habitat'),
]
