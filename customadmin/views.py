from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from restaurant.models import AboutItem, AboutUs, Booking
# Create your views here.
class Index(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('admin:login')
    template_name = 'customadmin/index.html'

class BookingView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('admin:login')
    template_name = 'customadmin/booking.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Booking.objects.all()
        #celery, websocket.io, 
        # print(context)
        return context
    def post(self,request, *args,**kwargs):
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        no_of_people = request.POST.get('noofpeople')
        date = request.POST.get('date')
        time = request.POST.get('time')
        contact_message = request.POST.get('contact_message')
        print("data print here: ")
        print(contact_name,contact_email,contact_phone,no_of_people,date,time,contact_message)
        # Booking.objects.create(
        #     name = contact_name,
        #     email = contact_email,
        #     phone = contact_phone,
        #     number_of_people = no_of_people,
        #     date = date,
        #     type = time,
        #     message = contact_message
        # )
        return redirect('index')
    
class AboutAdmin(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('admin:login')
    template_name = 'customadmin/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutUs.objects.first()
        context['about_items'] = AboutItem.objects.all()
        #celery, websocket.io, 
        # print(context)
        return context
    def post(self,request, *args,**kwargs):
        id = request.POST.get('id')
        title = request.POST.get('contact_name')
        greating = request.POST.get('greating')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('contact_message')
        print("data print here: ")
        print(title,greating,subtitle,description,id)
        about = AboutUs.objects.get(pk=id)
        about.title = title
        about.greating_text = greating
        about.sub_title = subtitle
        about.descriptions = description
        about.save()
        # Booking.objects.create(
        #     name = contact_name,
        #     email = contact_email,
        #     phone = contact_phone,
        #     number_of_people = no_of_people,
        #     date = date,
        #     type = time,
        #     message = contact_message
        # )
        return redirect('about-admin')
   