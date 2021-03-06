from .models import AuctionStatus, Contributor, Auction, Detail, Review, Role, Item, Bid, Image
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser
from datetime import datetime
from .fields import CustomForeignKeyField


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username',
                  'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class AuctionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionStatus
        fields = ('choice',)


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('first_name', 'last_name', 'role')


class AuctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auction
        fields = ('id', 'open_date', 'close_date', 'minimum_bid', 'seller',
                  'auction_status', 'items')
        depth = 3


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('cover_date', 'publisher', 'issue_number', 'variant',
                  'virgin_cover', 'characters', 'choice', 'grade')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('rate', 'comment', 'review_date')


class RoleSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=Role.ROLES)

    class Meta:
        Model = Role
        fields = ('con_role')


class BidSerializer(serializers.ModelSerializer):
    auction = CustomForeignKeyField(
        queryset=Auction.objects.all(), serializer=AuctionSerializer)
    bidder = CustomForeignKeyField(
        queryset=CustomUser.objects.all(), serializer=CustomUserSerializer)

    class Meta:
        model = Bid
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'contributors', 'details')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('cover_image',)
