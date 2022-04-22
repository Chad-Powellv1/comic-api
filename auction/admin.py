from django.contrib import admin
from .models import (
 AuctionStatus,
 Contributor,
 Auction,
 Detail,
 Review,
 Role,
 Item,
 Bid,
)

admin.site.register(AuctionStatus)
admin.site.register(Contributor)
admin.site.register(Auction)
admin.site.register(Detail)
admin.site.register(Review)
admin.site.register(Role)
admin.site.register(Item)
admin.site.register(Bid)