# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Speaker, Talk

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','title','photo','is_public']

class TalkAdmin(admin.ModelAdmin):
    list_display = ['speakers_names', 'title', 'description', 'is_public']
    list_editable = ['title','description']

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)