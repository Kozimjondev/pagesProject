from django.urls import path
from .views import HomePageView, AboutPageView, YouTube

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('youtube/', YouTube.as_view(), name='youtube'),
]