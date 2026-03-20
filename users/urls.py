from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_user, name='create-user'),
    path('list/', list_users, name='list-users'),
    path('list/<int:pk>/', get_user, name='get-user'),
    path('update/<int:pk>/', update_user, name='update-user'),
    path('delete/<int:pk>/', delete_user, name='delete-user'),
]