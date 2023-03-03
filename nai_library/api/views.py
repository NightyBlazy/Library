from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()

    serializer_class = BooksSerializer

    parser_classes = (MultiPartParser, FormParser)

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()

    serializer_class = PublisherSerializer

    parser_classes = (MultiPartParser, FormParser)

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()

    serializer_class = AuthorSerializer

    parser_classes = (MultiPartParser, FormParser)

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    parser_classes = (MultiPartParser, FormParser)

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()

    serializer_class = MemberSerializer

    parser_classes = (MultiPartParser, FormParser)

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        memberhold = Holds.objects.create(
            hold_holder=serializer.validated_data['member_name'])
        return serializer.save(member_holds=memberhold)


class HoldsViewSet(ModelViewSet):
    queryset = Holds.objects.all()

    serializer_class = HoldsSerializer

    parser_classes = (MultiPartParser, FormParser)

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
