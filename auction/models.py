from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

class AuctionStatus(models.Model):
    ACTIVE = 'Active'
    CANCELLED = 'Cancelled'
    COMPLETE = 'Complete'
    PENDING = 'Pending'
    STATUS = [
        (ACTIVE, 'Active'),
        (CANCELLED, 'Cancelled'),
        (COMPLETE, 'Complete'),
        (PENDING, 'Pending'), 
    ]
    choice = models.CharField(max_length=9, choices=STATUS, default=ACTIVE)
    
    class Meta:
        verbose_name_plural = 'Action Status'

    def __str__(self):
        return self.choice

class Role(models.Model):
    writer = models.CharField(max_length=200,null=True)
    artist = models.CharField(max_length=200,null=True)
    penciller = models.CharField(max_length=200,null=True)
    inker = models.CharField(max_length=200,null=True)
    colorist = models.CharField(max_length=200,null=True)
    cover_artist = models.CharField(max_length=200,null=True)
    letterer = models.CharField(max_length=200,null=True)
    editor = models.CharField(max_length=200,null=True)
    created_by = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.writer

class Contributor(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    role = models.ManyToManyField(Role)

    def __str__(self):
        return self.last_name

class Detail(models.Model):
    cover_date = models.DateField(null=False)
    publisher = models.CharField(max_length=200,null=False)
    issue_number = models.IntegerField(null=False)
    variant = models.BooleanField(null=False,default=False)
    virgin_cover = models.BooleanField(null=False,default=False)
    character = models.CharField(max_length=200,null=True)
    BRONZE_AGE = 'Bronze Age'
    COPPER_AGE = 'Copper Age'
    GOLDEN_AGE = 'Golden Age'
    MODERN_AGE = 'Modern Age'
    PLATINUM_AGE = 'Platinum Age'
    SILVER_AGE = 'Silver Age'
    ERA = [
        (BRONZE_AGE, 'Bronze Age'),
        (COPPER_AGE, 'Copper Age'),
        (GOLDEN_AGE, 'Golden Age'),
        (MODERN_AGE, 'Modern Age'),
        (PLATINUM_AGE, 'Platinum Age'),
        (SILVER_AGE, 'Silver Age'),
    ]
    choice = models.CharField(max_length=12, choices=ERA, default=None)
    GEM_MINT = 'GM'
    MINT = 'M'
    NEAR_MINT_MINT = 'NM/M'
    NEAR_MINT_ = 'NM+'
    NEAR_MINT = 'NM'
    NEARM_INT = 'NM-'
    VERY_FINE_NEAR_MINT = 'VF/NM'
    VERY_FINE_ = 'VF+'
    VERY_FINE = 'VF'
    VER_YFINE = 'VF-'
    FINE_VERY_FINE = 'F/VF'
    FINE_ = 'F+'
    FINE = 'F'
    FIN_E = 'F-'
    VERY_GOOD_FINE = 'VG/F'
    VERY_GOOD = 'VG+'
    VERYGOOD = 'VG'
    VERY_G_OOD = 'VG-'
    GOOD_VERY_GOOD = 'G/VG'
    GOOD = 'G+'
    GOO_D = 'G'
    GO_OD = 'G-'
    FAIR_GOOD = 'F/G'
    FAIR = 'F'
    POOR = 'P'
    CGC_GRADING_SCALE = [
        (GEM_MINT, 'GM'),
        (MINT, 'M'),
        (NEAR_MINT_MINT, 'NM/M'),
        (NEAR_MINT_, 'NM+'),
        (NEAR_MINT, 'NM'),
        (NEARM_INT, 'NM-'),
        (VERY_FINE_NEAR_MINT, 'VF/NM'),
        (VERY_FINE_, 'VF+'),
        (VERY_FINE, 'VF'),
        (VER_YFINE, 'VF-'),
        (FINE_VERY_FINE, 'F/VF'),
        (FINE_, 'F+'),
        (FINE, 'F'),
        (FIN_E, 'F-'),
        (VERY_GOOD_FINE, 'VG/F'),
        (VERY_GOOD, 'VG+'),
        (VERYGOOD, 'VG'),
        (VERY_G_OOD, 'VG-'),
        (GOOD_VERY_GOOD, 'G/VG'),
        (GOOD, 'G+'),
        (GOO_D, 'G'),
        (GO_OD, 'G-'),
        (FAIR_GOOD, 'F/G'),
        (FAIR, 'F'),
        (POOR, 'P'),
    ]
    grade = models.CharField(max_length=5, choices=CGC_GRADING_SCALE, default=None)
    
    def __str__(self):
        return self.cover_date

class Item(models.Model):
    title = models.CharField(max_length=200,null=False)
    contributors = models.ManyToManyField(Contributor)
    details = models.ManyToManyField(Detail)

    def __str__(self):
        return self.title

class Auction(models.Model):
    title = models.CharField(max_length=200,null=False)
    description = models.CharField(max_length=200,null=False)
    open_date = models.DateTimeField(auto_now_add=True,null=False)
    close_date = models.DateTimeField(null=False)
    minimum_bid = MoneyField(max_digits=12,decimal_places=2,default_currency='USD')
    seller = models.ManyToManyField(User)
    auction_status = models.ManyToManyField(AuctionStatus)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.title

class Bid(models.Model):
    bid_amount = MoneyField(max_digits=12,decimal_places=2,default_currency='USD',null=False)
    bid_time = models.DateTimeField(auto_now_add=True,null=False)
    auction = models.ManyToManyField(Auction)
    bidder = models.ManyToManyField(User)

    def __str__(self):
        return self.bid_amount

class Review(models.Model):
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2
    ONE = 1
    ZERO = 0
    STARS = [
        (FIVE, 5),
        (FOUR, 4),
        (THREE, 3),
        (TWO, 2),
        (ONE, 1),
        (ZERO, 0),
    ]
    rate = models.IntegerField(choices=STARS, default=None)
    comment = models.CharField(max_length=200,null=True)
    review_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.number_stars
