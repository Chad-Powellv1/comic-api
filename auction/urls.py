from .views import DetailViewSet, ReviewViewSet, RoleViewSet, ItemViewSet, BidViewSet
from .views import AuctionStatusViewSet, ContributorViewSet, AuctionViewSet
from django.urls import path, include
from rest_framework import routers
from auction import views


router = routers.DefaultRouter()
router.register(r'status', views.AuctionStatusViewSet)
router.register(r'contributor', views.ContributorViewSet)
router.register(r'auction', views.AuctionViewSet)
router.register(r'detail', views.DetailViewSet)
router.register(r'review', views.ReviewViewSet)
router.register(r'role', views.RoleViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'bid', views.BidViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
