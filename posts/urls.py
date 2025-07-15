from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('',views.post_lists,name='list'),
    path('<slug:slug>',views.post_page,name="page"),
    path('<slug:slug>/like/',views.like_page,name="like"),
    

]
