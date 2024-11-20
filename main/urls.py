from django.urls import path
from rest_framework.authtoken import views
from .views import UserApiView, TodoApiListView, TodoApiUpdateView



urlpatterns = [
    path('users/', UserApiView.as_view()),
    path('todos/', TodoApiListView.as_view()),
    path('todos/<pk>/', TodoApiUpdateView.as_view()),
    path('token-auth/', views.obtain_auth_token),
    
]