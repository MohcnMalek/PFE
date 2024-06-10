from django.urls import path
from .views import base_view, preprocessing, classification, clustering  # Import de la vue clustering
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('base/', base_view, name='base'),
    path('preprocessing/', preprocessing, name='preprocessing'),
    path('checker_page/', views.checker_page, name='checker_page'),
    path('chooseMethod/', views.chooseMethod, name='chooseMethod'),
    path('classification/', classification, name='classification'),
    path('clustering/', clustering, name='clustering'),
]
