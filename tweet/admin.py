from django.contrib import admin
from .models import Tweet,Profile,Comments


# Register your models here.
admin.site.register(Tweet)
admin.site.register(Profile)
admin.site.register(Comments)
