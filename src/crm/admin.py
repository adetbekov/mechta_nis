from django.contrib import admin
from .models import Client, Reservation, Transaction

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('first_name','last_name','iin')
    search_fields=['first_name','last_name','iin']

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ('client','estimated_date_in','estimated_date_out', 'type_of_room')
    list_filter=['type_of_room']
    search_fields=['client']

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('reservation','date_in','date_out')
    list_filter=['payment_form']
    search_fields=['reservation']

admin.site.register(Client, ClientAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Transaction, TransactionAdmin)