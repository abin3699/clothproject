from django.shortcuts import render,redirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse

from django.views.generic import CreateView,FormView
from yousta.models import User,Category
from yousta.forms import RegistrationForm,LoginForm,CategoryCreateForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
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
                return redirect("signin")
            else:
                messages.error(request,"failed...")
                return render(request,self.template_name,{"form":form})
            


            







