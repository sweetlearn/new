from django.urls import path

from .views import HomePageView, AboutPageView, DemoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('demo/', DemoPageView.as_view(), name='demo'),
]
