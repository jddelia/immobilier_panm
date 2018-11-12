from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='mainsite-index'),
    path('location/<int:post_id>/', views.post, name='mainsite-location')
]
