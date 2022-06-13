from django.contrib import admin
from .models import Post, Categorya, Contact
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('theme', 'shortText')


admin.site.register(Post, PostAdmin)

admin.site.register(Categorya)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date')

admin.site.register(Contact, ContactAdmin)