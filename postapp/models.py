from django.db import models

# Create your models here.

class Post(models.Model):
    theme = models.CharField(max_length=100, null=True)
    shortText = models.CharField(max_length=255, null=True)
    text = models.TextField(null=True)
    img = models.ImageField(null=True)
    date = models.DateField(null=True)
    view_count = models.IntegerField(default=0, null=True)


    @property
    def get_image(self):
        try:
            return self.img.url
        except:
            return ''
    def view_count_add(self):
        self.view_count+=1
        self.save()

    def __str__(self):
        return self.theme