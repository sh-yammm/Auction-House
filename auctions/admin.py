from django.contrib import admin
from .models import AuctionItem, Bid

# Register your models here.

admin.site.register(AuctionItem)
admin.site.register(Bid)