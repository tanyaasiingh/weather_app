
from django.urls import path
from the_app import views

urlpatterns = [
    
    path("",views.home,name="home"),

]
