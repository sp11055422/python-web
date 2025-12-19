from django.contrib import admin
from .models import Poll, Option


# Register your models for admin
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
	list_display = ('id', 'subject', 'created')


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'poll', 'votes')

