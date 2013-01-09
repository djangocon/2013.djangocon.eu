# -*- coding: utf-8 -*-
from django.contrib import admin

from vote.models import *

class EntryAdmin(admin.ModelAdmin):
    list_display = ['topic', 'description','score']
    search_fields = ['topic', 'description']

class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'entry', 'created']
    search_fields = ['=user__username',]
    list_filter = ['entry',]

admin.site.register(Entry, EntryAdmin)
admin.site.register(Vote, VoteAdmin)