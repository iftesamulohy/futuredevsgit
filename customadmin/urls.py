from django.urls import path

from customadmin.views import Index,BookingView,AboutAdmin


urlpatterns = [
    path('',Index.as_view(),name='dashboard'),
    path('booking/',BookingView.as_view(),name='booking'),
    path('about/',AboutAdmin.as_view(),name='about-admin'),
]