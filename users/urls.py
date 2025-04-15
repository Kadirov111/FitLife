from django.urls import path
from .views import RegisterView, LogoutView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile'),
]
