from django.contrib import admin
from .models import Season, Foraged, Foray, Resource
# Register your models here.
admin.site.register(Season)
admin.site.register(Foraged)
admin.site.register(Foray)
admin.site.register(Resource)