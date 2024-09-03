from django.db import models


class WishList(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name= 'wishlist')
    auctions = models.ForeignKey('auction.AuctionDetails', on_delete=models.CASCADE, related_name='auction_wishlist')


class Transactions(models.Model):
    CHOICES={
        'Credit Card':'Credit Card',
        'Debit Card':'Debit Card',
        'Wallet': 'Wallet'
    }
    #transactions_id=models.BigAutoField(primary_key=True)
    transactions_amount=models.FloatField(blank=True,null=True)
    transactions_method=models.CharField(max_length=32,choices=CHOICES,blank=True ,null=True)
    user=models.ForeignKey('accounts.User',on_delete=models.CASCADE,blank=True ,null=True)
    transactions_date=models.DateTimeField(auto_now_add=True,blank=True ,null=True)
    transactions_status=models.CharField(max_length=20,blank=True ,null=True)
    
    
