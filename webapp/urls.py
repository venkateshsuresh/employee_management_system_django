from django.urls import path
from . import views
urlpatterns = [
    #path('', views.index),
    #path('ar/', views.hello),
    path('', views.hello),
    path('ar/', views.index),
]
