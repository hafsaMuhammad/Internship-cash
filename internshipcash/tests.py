from django.test import TestCase

# Create your tests here.


from .models import Transaction
from .models import Account
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class TransactionModelTests(TestCase):



    # Transfer balance method test ...... note: not completed
    def test_transfer_balance(self):
        pass
        sender = User(username= 'hafsa', password='l2hzn2010', id=1)
        sender.save()
        senderAcc = Account(account_number = '1234', balance= 100, created_at= timezone.now() , User= sender)
        senderAcc.save()
        reciever = User(username= 'nada', password='l2hzn2010', id=2)
        reciever.save()
        receiverAcc = Account(account_number = '1243', balance= 100, created_at= timezone.now() , User= reciever)
        receiverAcc.save()
        owner = User(username= 'owner', password='l2hzn2010', id=3)
        owner.save()
        ownerAcc = Account(account_number = '1432', balance= 100, created_at= timezone.now() , User= owner)
        ownerAcc.save()

        fee = (4/100) * 50.0
        expectedSender = senderAcc.balance - 50
        expectedReceived= receiverAcc.balance + (50.0-fee)
        expectedOwner = ownerAcc.balance + fee

        # t = Transaction(type= 't', amount=50.0, transaction_time= timezone.now(), account= senderAcc)
        # t.save()

        # self.assertEqual( senderAcc.balance , expectedSender )
        # self.assertEqual(receiverAcc.balance, expectedReceived )
        # self.assertEqual(ownerAcc.balance, expectedOwner )
       




    # testing cash in method
    def test_cash_in(self):
        sender = User(username= 'hafsa', password='l2hzn2010', id=1)
        sender.save()
        senderAcc = Account(account_number = '1234', balance= 100, created_at=timezone.now() , User= sender)
        senderAcc.save()
        expected = float(senderAcc.balance + 50.0) 
        t = Transaction(type= 'in', amount=50.0, transaction_time= timezone.now(), account= senderAcc)
        t.save()
        self.assertEqual( float(senderAcc.balance) , expected )


    # testing cash out method
    def test_cash_out(self):
        sender = User(username= 'hafsa', password='l2hzn2010', id=1)
        sender.save()
        senderAcc = Account(account_number = '1234', balance= 100, created_at=timezone.now() , User= sender)
        senderAcc.save()
        expected = float(senderAcc.balance - 50.0) 
        t = Transaction(type= 'out', amount=50.0, transaction_time= timezone.now(), account= senderAcc)
        t.save()
        self.assertEqual( float(senderAcc.balance) , expected )