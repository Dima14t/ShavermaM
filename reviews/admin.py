from django.contrib import admin

# Register your models here.
from .models import Reviews, ReviewResponse


admin.site.register(Reviews)
admin.site.register(ReviewResponse)
