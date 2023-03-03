from rest_framework import serializers

from .models import *


class BooksSerializer(serializers.ModelSerializer):
    book_author = serializers.SlugRelatedField(
        many=False, slug_field='author_name', queryset=Author.objects.all())
    book_publisher = serializers.SlugRelatedField(
        many=False, slug_field='publisher_name', queryset=Publisher.objects.all())
    book_category = serializers.SlugRelatedField(
        many=True, slug_field='cate_name', queryset=Category.objects.all())

    class Meta:
        model = Books
        fields = ['book_id',
                  'book_name',
                  'book_author',
                  'book_publisher',
                  'book_category',
                  'book_page',
                  'book_rating',
                  'book_desc',
                  'book_rdate',
                  ]


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    member_gender = serializers.SlugRelatedField(
        many=False, slug_field='gender_name', queryset=Gender.objects.all())
    member_borrowedbooks = serializers.SlugRelatedField(
        many=True, slug_field='book_name', queryset=Books.objects.all())
    member_holds = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='holds-detail'
    )
    member_jdate = serializers.DateField(format="%d.%m.%Y", read_only=True)
    member_bdate = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Member
        fields = ['member_id',
                  'member_name',
                  'member_gender',
                  'member_jdate',
                  'member_bdate',
                  'member_borrowedbooks',
                  'member_holds'
                  ]


class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = '__all__'


class HoldsSerializer(serializers.ModelSerializer):
    hold_books = serializers.SlugRelatedField(
        many=True, slug_field='book_name', queryset=Books.objects.all())

    class Meta:
        model = Holds
        fields = ['hold_id',
                  'hold_holder',
                  'hold_books']
