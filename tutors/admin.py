

from django.contrib import admin

from .models import Tutor
from .models import Review


admin.site.register(Tutor)
admin.site.register(Review)