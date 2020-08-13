
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name="home"), 
    path('login/', views.Login, name="login"),
    path('signup/', views.SignUp, name="singup"),
    path('check-email/', views.CheckEmailId, name="checkemail"),
    path('check-username/', views.CheckUserName, name="checkusername"),
    path('createblog/', views.CreateBlog, name="createblog"),
    path('like/', views.LikePost, name="likepost"),
    path('dislike/', views.DisLikePost, name="dislikepost"),
    path('comment/', views.MakeComment, name="makecomment"),
    path('logout/', views.Logout, name="logout"),
]