from .views import DetailViewSet, ReviewViewSet, RoleViewSet, ItemViewSet, BidViewSet
from .views import AuctionStatusViewSet, ContributorViewSet, AuctionViewSet
from rest_framework_simplejwt import views as jwt_views
from .views import UserCreate, UserDetail
from django.urls import path, include
from rest_framework import routers
from auction import views


router = routers.DefaultRouter()
router.register(r'contributor', views.ContributorViewSet)
router.register(r'status', views.AuctionStatusViewSet)
router.register(r'auction', views.AuctionViewSet)
router.register(r'detail', views.DetailViewSet)
router.register(r'review', views.ReviewViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'role', views.RoleViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'bid', views.BidViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]