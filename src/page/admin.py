from django.contrib import admin
from .models import Event,Contacts,Comment,Ticket
# Register your models here.
admin.site.register(Event)
admin.site.register(Contacts)
admin.site.register(Comment)
admin.site.register(Ticket)
