
from django.conf.urls import url,include
from . import  views
from celebrities.models import Celebrity
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from celebrities.views import CelebrityCreate,CelebrityUpdate,CelebrityDelete,UserRegisterView,UserLoginView,CelebrityIndex







urlpatterns = [
	url(r'^$',ListView.as_view(queryset=Celebrity.objects.all().order_by("age")[:10], template_name="celebrities/index.html"),name="celebrities"),
	url(r'^about/', views.about, name="about"),
    url(r'^celebrityIndex/', CelebrityIndex().index, name="index"),
	url(r'^(?P<pk>\d+)$' , DetailView.as_view(model=Celebrity, template_name='celebrities/individual.html'), name="celebrity-detail"),
    url(r'^celebrity/add/$', CelebrityCreate.as_view(), name="celebrity-create"),
    url(r'^celebrity/(?P<pk>\d+)/$', CelebrityUpdate.as_view(), name="celebrity-update"),
    url(r'^celebrity/(?P<pk>\d+)/delete/$', CelebrityDelete.as_view(), name="celebrity-delete"),
    url(r'^celebrity/register/$', UserRegisterView.as_view(), name="register"),
    url(r'^celebrity/login/$', UserLoginView.as_view(), name="login"),
    url(r'^celebrity/logout/$', views.logout_view, name="logout"),




   ]


