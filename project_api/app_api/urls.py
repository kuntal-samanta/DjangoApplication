from django.urls import path
from .import views


urlpatterns = [
    path('', views.Test, name="app_api_test"),
    path('users/', views.UserListAPIView.as_view()),

    path('1/books/', views.Book_List_API_View_1.as_view()),
    path('2/books/', views.Book_List_API_View_2.as_view()),

    path('books/', views.Book_Create_API_View.as_view()),
]

