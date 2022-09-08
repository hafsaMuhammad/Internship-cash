import email
from pyexpat import model
from secrets import choice
from unicodedata import name
from urllib import request
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Account(models.Model):
    account_number = models.CharField(max_length=9)
    balance = models.FloatField(default=0.0)
    created_at = models.DateTimeField('date created')
    User = models.ForeignKey(User, on_delete=models.CASCADE)

#date-->auto add, balance--> decimal not float, account_number-->unique

transaction_choices=(('t', 'Transfer'), ('in', 'Cash in'), ('out', 'Cash out'))

class Transaction(models.Model):
    type = models.CharField(max_length=20, choices=transaction_choices)
    amount = models.FloatField(default=0.0)
    fee = models.FloatField(default=0.0, editable=False)
    transaction_time = models.DateTimeField('date created')
    receiverAccNumber = models.CharField(max_length=9, default='000000000')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


    @classmethod
    def transferBalance(cls,receiverNum, amount , user_id):
        receiverAcc = Account.objects.get(account_number = receiverNum)
        senderAccount = Account.objects.get(User_id= user_id)
        fee = (4/100) * float(amount)
        owner = User.objects.get(username= 'owner')
        owner = owner.id
        ownerAcc = Account.objects.get(User_id= owner)
        senderAccount.balance -= amount
        ownerAcc.balance += float(fee)
        receiverAcc.balance += float(amount-fee)
        ownerAcc.save(update_fields=['balance'])
        senderAccount.save(update_fields=['balance'])
        receiverAcc.save(update_fields = ['balance'])
        return fee

    def save(self, *args, **kwargs):

        if self.type=='t':
            id = self.account.User_id
            fee = self.transferBalance(self.receiverAccNumber, self.amount, id )
            self.fee = fee
        elif self.type=='in':
            self.account.balance += self.amount
            self.account.save()
        elif self.type=='out':
            self.account.balance -= self.amount
            self.account.save()
        else:
            pass
        super(Transaction, self).save(*args, **kwargs)


