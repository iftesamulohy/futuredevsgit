from django.urls import path

from statickwork.views import about, index
urlpatterns = [
    path('',index,name="index"),
    path('about/',about,name="about")
]