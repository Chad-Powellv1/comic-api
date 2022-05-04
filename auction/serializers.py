from .models import AuctionStatus, Contributor, Auction, Detail, Review, Role, Item, Bid, Image
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser

# API url 
URL = 'https://8000-chadpowellv1-comicapi-tiv0x3tc1cg.ws-us43.gitpod.io'

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )

    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id','email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
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
        fields = ('id','open_date', 'close_date', 'minimum_bid', 'seller',
         'auction_status', 'items')
        depth = 3


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('cover_date', 'publisher', 'issue_number', 'variant', 'virgin_cover', 'characters', 'choice', 'grade')


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
    class Meta:
        model = Bid
        fields = ('bid_amount', 'bid_time', 'auction', 'bidder')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'contributors','details')


class ImageSerializer(serializers.ModelSerializer):
    cover_image = serializers.SerializerMethodField('get_cover_image_url')

    class Meta:
        model = Image
        fields = ('cover_image',)

    def get_cover_image_url(self, obj):
        if obj.cover_image:
            return URL + obj.cover_image.url
