from django.contrib import admin
#from .models import Contact we can also write this method 
from home.models import Contact
from home.models import Hotels,Rooms,Reservation
# Register your models here.
admin.site.register(Contact)

# Register your models here.
admin.site.register(Hotels)
admin.site.register(Rooms)
admin.site.register(Reservation)