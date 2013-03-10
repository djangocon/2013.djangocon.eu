# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Speaker, Talk, Agenda

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','title','photo','is_public']
    actions = ('make_public', 'hide')

    def make_public(self, request, queryset):
        queryset.update(is_public=True)
    make_public.short_description = u'Make speakers public'

    def hide(self, request, queryset):
        queryset.update(is_public=False)
    hide.short_description = u'Hide speakers'

class TalkAdmin(admin.ModelAdmin):
    list_display = ['speakers_names', 'title', 'description', 'is_public']
    list_editable = ['title','description']
    actions = ('make_public', 'hide')

    def make_public(self, request, queryset):
        queryset.update(is_public=True)
    make_public.short_description = u'Make talks public'

    def hide(self, request, queryset):
        queryset.update(is_public=False)
    hide.short_description = u'Hide talks'

class AgendaAdmin(admin.ModelAdmin):
    list_display = ['talk', 'description', 'day', 'start', 'finish', 'is_featured']
    list_editable = ['day', 'start', 'finish', 'is_featured']

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Agenda, AgendaAdmin)