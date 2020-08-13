from django.urls import path
from . import views


urlpatterns = [
    # path('/', ),
    path('', views.Home, name="home"),
    path('post/<slug:slug>/', views.ViewPost, name="viewpost"),
    path('login/', views.Login, name="login"),
    path('signup/', views.SignUp, name="signup"),
    path('createblog/', views.CreateBlog, name="createblog"),
    path('check-email/', views.CheckEmailId, name="checkemail"),
    path('check-username/', views.CheckUserName, name="checkusername"),
    path('logout/', views.Logout, name="logout"),
]