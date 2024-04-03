from django.contrib import admin

# Register your models here.
from .models import Contact, Training, Blog, Team,Event

admin.site.register(Contact)
admin.site.register(Training)
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(Event)



