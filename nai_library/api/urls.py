from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Books', BooksViewSet, basename="books")
router.register(r'Publisher', PublisherViewSet, basename="publishers")
router.register(r'Author', AuthorViewSet, basename="authors")
router.register(r'Categories', CategoryViewSet, basename="categories")
router.register(r'Members', MemberViewSet, basename="members")
router.register(r'Holds', HoldsViewSet, basename="holds")


urlpatterns = [
    path('', include(router.urls))
]
