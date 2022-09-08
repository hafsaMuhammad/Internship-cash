from curses.ascii import US
import email
from sqlite3 import Date
from turtle import update
from xmlrpc.client import DateTime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
from .models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def base(request):
    return render(request,'internshipcash/base.html' )


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user= User.objects.get(username= username)
#     return render(request,'internshipcash/login.html')


def profile(request):
    username = request.user.username
    id = request.user.id
    firstname= request.user.first_name
    lastname= request.user.last_name
    date= request.user.date_joined
    email= request.user.email
    userAccount = Account.objects.filter(User_id= id)
    context = {
        'user' : username,
        'firstname': firstname,
        'lastname':lastname,
        'date':date,
        'email':email,
        'userAccount': userAccount,

    }
    return render(request,'internshipcash/index.html', context)



def transfer(request):
    # user = User.objects.filter(id= user_id)
    # context = {
    #     'user' : user,
    # }
    return render(request,'internshipcash/transfer.html')




def transferConfirmed(request):
    receiverNum = request.POST['receiverAccount']
    amount = float(request.POST['amount'])
    senderId = request.user.id
    userAcc = Transaction.transferBalance(receiverNum, amount, senderId)
    user = User.objects.filter(id= senderId)
    userAccount = Account.objects.filter(User_id= senderId)
    context = {
        'user' : user,
        'userAccount': userAccount,

    }
    return render(request,'internshipcash/transferConfirmed.html', context)

   
   