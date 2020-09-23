from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'sentiment', 'flag', 'visited', 'sarcasm', 'helpfulness']
    list_filter = ['visited', ]
