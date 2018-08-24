# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from celebrities.models import Celebrity
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from celebrities.forms import UserRegisterFrom,UserLoginForm
from django.contrib.auth.models import User



# Create your views here.


def index(request):
    return render(request,"celebrities/index.html")
	

def about(request):
    return render(request,"celebrities/about.html", {'message' : ["We are The Movie Creator" , "Production of 2017"]})	



class CelebrityIndex(ListView):

    def index(self,request):
     queryset = Celebrity.objects.all().order_by("age")[:10]
     print(queryset) #print it in console
     return render(request,"celebrities/celebrityIndex.html",{"records": queryset})

class CelebrityCreate(CreateView):
      model = Celebrity
      fields = ["name","age","gender","hair_color","rating","image"]


class CelebrityUpdate(UpdateView):
    model = Celebrity
    fields = ["name", "age", "gender", "hair_color", "rating", "image"]

class CelebrityDelete(DeleteView):
    model = Celebrity
    success_url = reverse_lazy("celebrities")



class UserRegisterView(View):
      form_class = UserRegisterFrom
      template_name = "celebrities/register.html"

      def get(self,request):
          form = self.form_class(None)
          return render(request, self.template_name, {"form": form})

      def post(self,request):
       form = self.form_class(request.POST)

       if form.is_valid():
           user = form.save(commit=False)
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user.set_password(password)
           user.save()

           user = authenticate(username=username,password=password)

           if user is not None:
               login(request, user)
               return redirect("celebrities")


       return render(request,self.template_name, {"form": form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = "celebrities/login.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("celebrities")
            else:
                return render(request, self.template_name, {"form": form , "userError" : "This User Does Not Exist"})


        return render(request, self.template_name, {"form": form})



def logout_view(request):
    logout(request)
    return redirect("celebrities")
