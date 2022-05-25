from django.db import models

# Create your models here.

class Categorya(models.Model):
    name = models.CharField(null=True, max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    cat_id = models.ForeignKey(Categorya, on_delete=models.SET_NULL, null=True)

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

    def __str__(self):
        return self.theme