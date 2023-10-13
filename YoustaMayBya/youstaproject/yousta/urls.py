from django.urls import path
from yousta.views import SignUpView,SigninView



urlpatterns=[
    path("register/",SignUpView.as_view(),name="signup"),
    path("",SigninView.as_view(),name="signin")



]