from django.urls import path
from . import views

app_name='pages'

urlpatterns = [
    path('',views.home,name='home'),
    path('donations',views.donations,name='donations'),
    path('privacy',views.privacy,name='privacy'),
    path('cancellation',views.cancellation,name='cancellation'),


]