from django.urls import path
from .views import RegisterView, LoginView, LogoutView, PostList, PostDetail

urlpatterns = [
    path("user/register/", RegisterView.as_view(), name='register'),
    path("user/login", LoginView.as_view(), name='login'),
    path("user/logout", LogoutView.as_view(), name='logout'),
    path("post/", PostList.as_view(), name='posts'),
    path("post/<int:pk>", PostDetail.as_view(), name='post_detail'),
]
