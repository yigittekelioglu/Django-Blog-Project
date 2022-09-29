from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_request, name="login_request"),
    path('register/', views.register_request, name="register_request"),
    path('logout/', views.logout_request, name="logout_request"),
    path('profile/', views.profile, name="profile"),
    path('changepassword/', views.changepassword, name="changepassword"),

]
