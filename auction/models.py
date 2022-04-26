from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField
from django.conf import settings
from django.db import models
import datetime


class CustomUser(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


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
        return f"{self.choice}"


class Role(models.Model):
    WRITER = 'Writer'
    ARTIST = 'Artist'
    PENCILLER = 'Penciller'
    INKER = 'Inker'
    COLORIST = 'Colorist'
    COVER_ARTIST = 'Cover Artist'
    LETTERER = 'Letterer'
    EDITOR = 'Editor'
    CREATED_BY = 'Created By'
    ROLES = [
        ('', '----'),
        (WRITER, 'Writer'),
        (ARTIST, 'Artist'),
        (PENCILLER, 'Penciller'),
        (INKER, 'Inker'),
        (COLORIST, 'Colorist'),
        (COVER_ARTIST, 'Cover Artist'),
        (LETTERER, 'Letterer'),
        (EDITOR,  'Editor'),
        (CREATED_BY, 'Created By'),
    ]
    con_role = models.CharField(max_length=12, choices=ROLES,blank=True)

    def __str__(self):
        return f"{self.con_role}"


class Contributor(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.ManyToManyField(Role)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Detail(models.Model):
    cover_date = models.IntegerField(default=current_year(), validators=[
                                     MinValueValidator(1897), max_value_current_year])
    publisher = models.CharField(max_length=200, null=False)
    issue_number = models.IntegerField(null=False)
    variant = models.BooleanField(null=False, default=False)
    virgin_cover = models.BooleanField(null=False, default=False)
    characters = models.CharField(max_length=200, null=True,blank=True)
    BRONZE_AGE = 'Bronze Age'
    COPPER_AGE = 'Copper Age'
    GOLDEN_AGE = 'Golden Age'
    MODERN_AGE = 'Modern Age'
    PLATINUM_AGE = 'Platinum Age'
    SILVER_AGE = 'Silver Age'
    ERA = [
        ('', '----'),
        (BRONZE_AGE, 'Bronze Age'),
        (COPPER_AGE, 'Copper Age'),
        (GOLDEN_AGE, 'Golden Age'),
        (MODERN_AGE, 'Modern Age'),
        (PLATINUM_AGE, 'Platinum Age'),
        (SILVER_AGE, 'Silver Age'),
    ]
    choice = models.CharField(max_length=12, choices=ERA,blank=True)
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
        ('', '----'),
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
    grade = models.CharField(blank=True,
        max_length=5, choices=CGC_GRADING_SCALE)

    def __str__(self):
        return f"{str(self.cover_date)}, Publisher: {self.publisher}, Issue Number: {self.issue_number}, Characters: {self.characters}, Era: {self.ERA}"


class Item(models.Model):
    title = models.CharField(max_length=200, null=False)
    contributors = models.ManyToManyField(Contributor)
    details = models.ManyToManyField(Detail)

    def __str__(self):
        return f"Title: {self.title}, Contributor: {self.contributors}, Details: {self.details}"


class Auction(models.Model):
    open_date = models.DateTimeField(auto_now_add=True, null=False)
    close_date = models.DateTimeField(null=False)
    minimum_bid = MoneyField(
        max_digits=12, decimal_places=2, default_currency='USD')
    seller = models.ManyToManyField(CustomUser)
    auction_status = models.ManyToManyField(AuctionStatus)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"Open date: {self.open_date}, Close date: {self.close_date}, Min bid: {str(self.minimum_bid)}"


class Bid(models.Model):
    bid_amount = MoneyField(max_digits=12, decimal_places=2,
                            default_currency='USD', null=False)
    bid_time = models.DateTimeField(auto_now_add=True, null=False)
    auction = models.ManyToManyField(Auction)
    bidder = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f"Bid amount: {self.bid_amount}, Bid time: {self.bid_time}"


class Review(models.Model):
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2
    ONE = 1
    ZERO = 0
    STARS = [
        ('', '----'),
        (FIVE, 5),
        (FOUR, 4),
        (THREE, 3),
        (TWO, 2),
        (ONE, 1),
        (ZERO, 0),
    ]
    rate = models.IntegerField(choices=STARS, null=False)
    comment = models.CharField(max_length=200, null=True)
    review_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f" Rate: {self.rate}"
