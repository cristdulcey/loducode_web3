from django.urls import include, path
from rest_framework import routers

from loducode_web3.viewset.nft_viewset import NftViewSet
from loducode_web3.viewset.attribute_viewset import AttributeNftViewSet
from loducode_web3.viewset.land_viewset import LandViewSet
from loducode_web3.viewset.attribute_land_viewset import AttributeLandViewSet

router = routers.DefaultRouter()
router.register(r'nfts', NftViewSet, basename='nfts')
router.register(r'attributes_nft', AttributeNftViewSet, basename='attributes_nft')
router.register(r'lands', LandViewSet, basename='lands')
router.register(r'attributes_lands', AttributeLandViewSet, basename='attributes_lands')
urlpatterns = [
    path('', include(router.urls)),
]
