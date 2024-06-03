from django.db import models

# Create your models here.
class Posts(models.Model):
    category = models.CharField(max_length=20)
    title= models.CharField(max_length=200)
    duration = models.CharField(max_length=20)
    content= models.TextField()
    image = models.FileField(upload_to="blog")
    image2 = models.FileField(upload_to="profile",null=True,blank=True)
    def __str__(self):
        return self.title