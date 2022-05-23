from django.db import models

# Create your models here.

class Post(models.Model):
    theme = models.CharField(max_length=100)
    shortText = models.CharField(max_length=255)
    img = models.ImageField()
    date = models.DateField()
    view_count = models.IntegerField(default=0)



    def view_count_add(self):
        self.view_count+=1
        self.save()

    def __str__(self):
        return self.theme