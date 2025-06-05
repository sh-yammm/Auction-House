from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class AuctionItem(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='auction_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    end_time = models.DateTimeField()

    seller = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):

        return self.title
    

class Bid(models.Model):

    item = models.ForeignKey(AuctionItem,on_delete=models.CASCADE, related_name='bids')

    bidder = models.ForeignKey(User, on_delete=models.CASCADE)

    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    bid_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f"{self.bidder.username} - {self.bid_amount} on {self.item.title}"