
# Register your models here.
from django.contrib import admin
from . models import details
# Register your models here.
admin.site.register(details)

from .models import Contact

admin.site.register(Contact)
