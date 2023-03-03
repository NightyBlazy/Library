from django.db import models
import uuid


class Books(models.Model):
    book_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    book_name = models.CharField(max_length=100, blank=False)
    book_author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, blank=False)
    book_publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    book_category = models.ManyToManyField('Category', blank=False)
    book_page = models.IntegerField(blank=False)
    book_rating = models.IntegerField(blank=False)
    book_desc = models.TextField(
        blank=True, default="Description not found...")
    book_rdate = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return f"{self.book_name} - {self.book_author}"


class Publisher(models.Model):
    publisher_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    publisher_name = models.CharField(max_length=50, blank=False)
    publisher_fdate = models.CharField(max_length=10, blank=False)
    publisher_adress = models.TextField(blank=True, default="Blank adress")

    def __str__(self):
        return self.publisher_name


class Category(models.Model):
    cate_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    cate_name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.cate_name


class Author(models.Model):
    author_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    author_name = models.CharField(max_length=50, blank=False)
    author_bdate = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.author_name


class Member(models.Model):
    member_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    member_name = models.CharField(max_length=50, blank=False)
    member_gender = models.ForeignKey(
        'Gender', on_delete=models.CASCADE, blank=False)
    member_jdate = models.DateField(auto_now_add=True, blank=False)
    member_bdate = models.DateField(blank=False)
    member_borrowedbooks = models.ManyToManyField('Books', blank=True)
    member_holds = models.OneToOneField(
        'Holds', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.member_name


class Gender(models.Model):
    gender_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    gender_name = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.gender_name


class Holds(models.Model):
    hold_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    hold_holder = models.CharField(max_length=50, blank=False)
    hold_books = models.ManyToManyField('Books', blank=True)

    def __str__(self):
        return self.hold_holder
