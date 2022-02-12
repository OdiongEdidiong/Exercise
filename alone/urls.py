from django.urls import path
from . import views
urlpatterns=[
    path("",views.signup,name="signup"),
    path("login/",views.signin,name="login"),
    path("welcome/",views.welcome,name="welcome"),
    path("logout/",views.signout,name="logout")
]