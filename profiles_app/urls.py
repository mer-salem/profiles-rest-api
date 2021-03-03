# from django.urls import path
from profiles_app import views

from django.urls import path, re_path
#from .views import ViewsToBeImported


urlpatterns = [path('hello-view/', views.HelloApiView.as_view()),

               ]
