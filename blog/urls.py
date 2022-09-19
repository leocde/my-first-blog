from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.post_list, name='post_list'),
    # This part post/<int:pk>/ specifies a URL pattern
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]