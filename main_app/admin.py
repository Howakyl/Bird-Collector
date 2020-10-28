from django.contrib import admin
from .models import Bird, Spotting, Habitat

admin.site.register(Bird)
admin.site.register(Spotting)
admin.site.register(Habitat)