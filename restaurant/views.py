from typing import Any
from django.shortcuts import render,redirect


from django.views.generic.base import TemplateView
from datetime import datetime
from restaurant.models import AboutUs, Booking, CounterData, Slider
# Create your views here.
class Index(TemplateView):
    template_name = 'restaurant/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.all().first()
        context['about'] = AboutUs.objects.all().first()
        context['counter'] = CounterData.objects.all()[0]
        #celery, websocket.io, 
        print(context)
        return context
    def post(self,request, *args,**kwargs):
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        no_of_people = request.POST.get('noofpeople')
        date = request.POST.get('date')
        time = request.POST.get('time')
        contact_message = request.POST.get('contact_message')
        update_date = datetime.strptime(date,'%Y-%m-%d').strftime('%m-%d-%y')
        print(update_date)
        print(contact_name,contact_email,contact_phone,no_of_people,date,time,contact_message)
        Booking.objects.create(
            name = contact_name,
            email = contact_email,
            phone = contact_phone,
            number_of_people = no_of_people,
            date = date,
            type = time,
            message = contact_message
        )
        return redirect('index')