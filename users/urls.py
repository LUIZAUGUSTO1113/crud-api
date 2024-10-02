from django.urls import path
from .views import UserListCreateView, UserDetailView,AllUsersListView,UserDeleteView,UserUpdateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/all/', AllUsersListView.as_view(), name='all-users-list'),  
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'), 
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'), 
]