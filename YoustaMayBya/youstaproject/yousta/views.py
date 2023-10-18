from django.db import models
from django.shortcuts import render,redirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from yousta.models import User,Category,Cloths,ClothVarients,Offers
from yousta.forms import RegistrationForm,LoginForm,CategoryCreateForm,ClothAddForm,ClothVarientForm,ClothOfferForm

# Create your views here.

class SignUpView(CreateView):
    template_name = "yousta/reg.html"
    form_class = RegistrationForm
    model = User
    success_url = reverse_lazy("signin")

    def form_valid(self,form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)
    

class SigninView(FormView):
    template_name="yousta/login.html"
    form_class = LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success...")
                return redirect("add-category")
            else:
                messages.error(request,"failed...")
                return render(request,self.template_name,{"form":form})
            

class CategoryCreateView(CreateView,ListView):
    template_name="yousta/category_add.html"
    form_class= CategoryCreateForm
    model=Category
    context_object_name="categories"
    success_url=reverse_lazy("add-category")
    def form_valid(self, form):
        messages.success(self.request,"category added...")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"category adding failed...")
        return super().form_invalid(form)
    
    def get_queryset(self):
        return Category.objects.filter(is_active=True)
    

def remove_category(request,*args,**kwargs):
    id=kwargs.get("pk")
    Category.objects.filter(id=id).update(is_active=False)
    messages.success(request,"category removed...")
    return redirect("add-category")

class ClothCreateView(CreateView):
    template_name ="yousta/cloth_add.html"
    model=Cloths
    form_class = ClothAddForm
    success_url=reverse_lazy("cloth-list")

    def form_valid(self, form):
        messages.success(self.request,"cloth has been added...")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"cloth adding failed...")
        return super().form_invalid(form)


class ClothListView(ListView):
    template_name="yousta/cloth_list.html"
    model=Cloths
    context_object_name="cloths"


class ClothUpdateView(UpdateView):
    template_name="yousta/cloth_edit.html"
    model=Cloths
    form_class=ClothAddForm
    success_url=reverse_lazy("cloth-list")

    def form_valid(self, form):
        messages.success(self.request,"cloth updated...")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"cloth updating failed...")
        return super().form_invalid(form)
    
def remove_clothview(request,*args,**kwargs):
    id=kwargs.get("pk")
    Cloths.objects.filter(id=id).delete()
    messages.success(request,"item removed...")
    return redirect("cloth-list")


class ClothVarientCreateView(CreateView):
    template_name="yousta/clothvarient_add.html"
    model=ClothVarients
    form_class=ClothVarientForm
    success_url=reverse_lazy("cloth-list")

    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=Cloths.objects.get(id=id)
        form.instance.cloth=obj
        messages.success(self.request,"varient has been added...")
        return super().form_valid(form)


class ClothDetailView(DetailView):
    template_name="yousta/cloth_detail.html"
    model=Cloths
    context_object_name="cloth"

class ClothVarientUpdateView(UpdateView):
    template_name="yousta/varient_edit.html"
    model=ClothVarients
    form_class=ClothVarientForm
    # success_url=reverse_lazy("cloth-list")
    
    def form_valid(self, form):
        messages.success(self.request,"cloth varient updated...")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"cloth varient updating failed...")
        return super().form_invalid(form)
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        cloth_varient_object=ClothVarients.objects.get(id=id)
        cloth_id=cloth_varient_object.cloth.id

        return reverse("cloth-detail",kwargs={"pk":cloth_id})

    
def remove_varient(request,*args,**kwargs):
    id=kwargs.get("pk")
    ClothVarients.objects.filter(id=id).delete()
    messages.success(request,"item removed...")
    return redirect("cloth-list")

class ClothOfferView(CreateView):
    template_name="yousta/cloth_offer.html"
    model=Offers
    form_class=ClothOfferForm
    success_url=reverse_lazy("cloth-list")

    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=ClothVarients.objects.get(id=id)
        form.instance.clothvarient=obj

        messages.success(self.request,"offer has been added...")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request," offer close...")
        return super().form_invalid(form)
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        cloth_varient_object= ClothVarients.objects.get(id=id)
        cloth_id=cloth_varient_object.cloth.id

        return reverse("cloth-detail",kwargs={"pk":cloth_id})
    
def remove_offer(request,*args,**kwargs):
    id=kwargs.get("pk")
    offer_obj=Offers.objects.get(id=id)
    cloth_id=offer_obj.clothvarient.cloth.id
    offer_obj.delete()
    return redirect("cloth-detail",pk=cloth_id)

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")