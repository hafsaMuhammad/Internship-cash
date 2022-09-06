from curses.ascii import US
from sqlite3 import Date
from turtle import update
from xmlrpc.client import DateTime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
from .models import Transaction
from django.contrib.auth.models import User
import datetime


def base(request):
    return render(request,'internshipcash/base.html' )




def home(request, user_id):
    user = User.objects.filter(id= user_id)
    userAccount = Account.objects.filter(User_id= user_id)
    context = {
        'user' : user,
        'userAccount': userAccount,

    }
    return render(request,'internshipcash/index.html', context)

    # return HttpResponse("You're viewing user %s Account" %user_id)

def transfer(request, user_id):
    user = User.objects.filter(id= user_id)
    context = {
        'user' : user,
    }
    return render(request,'internshipcash/transfer.html', context)




def transferConfirmed(request, user_id):
    receiverNum = request.POST['receiverAccount']
    amount = float(request.POST['amount'])
    userAcc = Transaction.transferBalance(receiverNum, amount, user_id)
    user = User.objects.filter(id= user_id)
    userAccount = Account.objects.filter(User_id= user_id)
    context = {
        'user' : user,
        'userAccount': userAccount,

    }
    return render(request,'internshipcash/transferConfirmed.html', context)

   
   