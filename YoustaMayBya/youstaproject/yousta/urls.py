from django.urls import path
from yousta.views import SignUpView,SigninView,CategoryCreateView,remove_category,\
    ClothCreateView,ClothListView,ClothUpdateView,remove_clothview,ClothVarientCreateView,\
    ClothDetailView,ClothVarientUpdateView,remove_varient,ClothOfferView,remove_offer,signout_view



urlpatterns=[
    path("register/",SignUpView.as_view(),name="signup"),
    path("",SigninView.as_view(),name="signin"),
    path("categories/add",CategoryCreateView.as_view(),name="add-category"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("cloths/add",ClothCreateView.as_view(),name="cloth-add"),
    path("cloths/all",ClothListView.as_view(),name="cloth-list"),
    path("cloths/<int:pk>/change",ClothUpdateView.as_view(),name="cloth-change"),
    path("cloths/<int:pk>/remove",remove_clothview,name="cloth-remove"),
    path("cloths/<int:pk>/varients/add",ClothVarientCreateView.as_view(),name="add-varient"),
    path("cloths/<int:pk>/",ClothDetailView.as_view(),name="cloth-detail"),
    path("cloths/<int:pk>/varients/change",ClothVarientUpdateView.as_view(),name="update-varient"),
    path("cloths/<int:pk>/varients/remove",remove_varient,name="remove-varient"),
    path("cloths/<int:pk>/varients/offer/add",ClothOfferView.as_view(),name="offer-varient"),
    path("offers/<int:pk>/remove",remove_offer,name="offer-delete"),
    path("logout",signout_view,name="signout")



]