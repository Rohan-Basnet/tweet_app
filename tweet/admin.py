from django.contrib import admin
from .models import Tweet,Profile,Comments,Like,Follow


# Register your models here.
admin.site.register(Tweet)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Like)
admin .site.register(Follow)