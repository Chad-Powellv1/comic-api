from .models import AuctionStatus, Contributor, Auction
from .models import Detail, Review, Role, Item, Bid, Image
from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AuctionStatus)
admin.site.register(Contributor)
admin.site.register(Auction)
admin.site.register(Detail)
admin.site.register(Review)
admin.site.register(Image)
admin.site.register(Role)
admin.site.register(Item)
admin.site.register(Bid)
