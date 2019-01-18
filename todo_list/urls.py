from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('done/<item_id>', views.done, name='done'),
    path('undone/<item_id>', views.undone, name='undone'),
    path('edit/<item_id>', views.edit, name='edit')
]