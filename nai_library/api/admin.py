from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Books)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Member)
admin.site.register(Gender)
admin.site.register(Holds)
admin.site.register(Category)
