from .serializers import AuctionStatusSerializer, ContributorSerializer, AuctionSerializer, DetailSerializer, ImageSerializer
from .serializers import ReviewSerializer, RoleSerializer, ItemSerializer, BidSerializer, CustomUserSerializer
from .models import AuctionStatus, Contributor, Auction, Detail, Review, Role, Item, Bid, CustomUser, Image
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import permissions, status, generics, viewsets



class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class AuctionStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all items
    """
    queryset = AuctionStatus.objects.all()
    serializer_class = AuctionStatusSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'choice']
    search_fields = ['=choice']
    ordering = ['id']


class ContributorViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all items
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'first_name', 'last_name']
    search_fields = ['=first_name', '=last_name']
    ordering = ['last_name']


class AuctionViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all items
    """
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'open_date', 'close_date', 'minimum_bid', 'items']
    search_fields = ['=open_date', '=close_date', '=minimum_bid', '=items']
    ordering = ['id']

class DetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all items
    """
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'publisher', 'variant', 'virgin_cover', 'characters', 'choice', 'grade']
    search_fields = ['=publisher', '=characters']
    ordering = ['id']

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all items
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all items
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'con_role']
    search_fields = ['=con_role']
    ordering = ['id']


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'title', 'contributors', 'details']
    search_fields = ['=title', '=contributors', '=details']
    ordering = ['id']


class BidViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all items
    """
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'bid_amount', 'bid_time']
    search_fields = ['=bid_amount', '=bid_time']
    ordering = ['id']

    def create_bid(self,request):
        user_id = request.data.append('bidder')
        bid_amount = request.data.append('bid_amount')
        auction = request.data.append('auction')

        

class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint with all items
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
  

