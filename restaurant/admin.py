from django.contrib import admin
from solo.admin import SingletonModelAdmin
from restaurant.models import AboutItem, AboutUs, Booking, CounterData, Slider, SliderItem

# Register your models here.
admin.site.register(SliderItem)
admin.site.register(Booking)
admin.site.register(AboutItem)
admin.site.register(Slider,SingletonModelAdmin)
admin.site.register(CounterData,SingletonModelAdmin)
admin.site.register(AboutUs,SingletonModelAdmin)