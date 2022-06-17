
from django.contrib import admin
from .models import Trakt, Stockwerk, Raum, Geratekategorie, Geratehersteller, Gerat, Ticket



# Register your models here.
admin.site.register(Trakt)
admin.site.register(Stockwerk)
admin.site.register(Raum)
admin.site.register(Gerat)
admin.site.register(Ticket)


admin.site.register(Geratekategorie)
admin.site.register(Geratehersteller)
