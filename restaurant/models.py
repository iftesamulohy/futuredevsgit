from django.db import models
from solo.models import SingletonModel
# Create your models here.
class SliderItem(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=50)
    image=models.ImageField(upload_to="slider/",default='slider/slider.jpeg')
    button_one = models.URLField()
    button_two = models.URLField()
    def __str__(self):
        return self.name
class AboutItem(models.Model):
    name = models.CharField(max_length=20)
    image=models.ImageField(upload_to="slider/",default='slider/slider.jpeg')
    def __str__(self):
        return self.name
class Slider(SingletonModel):
    name = models.CharField(max_length=20)
    slider_item = models.ManyToManyField(SliderItem)
class AboutUs(SingletonModel):
    greating_text = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=50)
    about_item = models.ManyToManyField(AboutItem)
    def __str__(self):
        return self.title
class Booking(models.Model):
    TYPE_CHOICE=(
        ('BREAKFAST', 'Breakfast: 8 am to 10 am'),
        ('LUNCH', 'Lunch: 12 am to 2 pm'),
        ('DINNER', 'Lunch: 8 pm to 10 pm'),

    )
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    number_of_people = models.IntegerField()
    date = models.DateField()
    type = models.CharField(max_length=50,choices=TYPE_CHOICE,default='BREAKFAST')
    message = models.TextField()
    def __str__(self):
        return self.name
class CounterData(SingletonModel):
    happy_people = models.IntegerField(default=0)
    recipe = models.IntegerField(default=0)
    coffee = models.IntegerField(default=0)
    best_award = models.IntegerField(default=0)