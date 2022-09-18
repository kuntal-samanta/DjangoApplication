from django.urls import path
from .import views


urlpatterns = [
    path('test/', views.Test, name="app1_test"),

    path('template1/', views.sample_html_1, name="sample_html_1"),

    path('template2/', views.sample_html_2, name="sample_html_2"),

    path('template3/', views.sample_html_3, name="sample_html_3"),

    path('template4/', views.sample_html_4, name="sample_html_4"),

    path('test-media/', views.test_media, name="sample_test_media"),

    path('test-slugfy/', views.test_slugify, name="sample_test_slugify"),
    path('test-slugfy-url/<slug:slug>', views.test_slugify_special_blog, name="sample_slugify_blog_url"),
    
]
