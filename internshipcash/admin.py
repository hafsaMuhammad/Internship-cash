from django.contrib import admin
from .models import Account
from .models import User
from .models import Transaction

# Register your models here.

@admin.action(description='Cash in')
def cash_in(modeladmin, request, queryset):
    queryset.update(balance= float( request.POST['amount']))


class AccountAdmin(admin.ModelAdmin):
    list_display= ['User_id', 'balance']
    actions= [cash_in]

admin.site.register(Account, AccountAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display= ['account','receiverAccNumber','type','amount','fee','transaction_time']
    
admin.site.register(Transaction, TransactionAdmin)