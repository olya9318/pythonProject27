from django.contrib import admin

from ads.models import Category, Ad
from users.models import Location, User

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Ad)
admin.site.register(Category)
