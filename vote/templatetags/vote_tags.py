# -*- coding: utf-8 -*-
from django import template
from vote.models import Vote

register = template.Library()

@register.filter
def voted_by_user(entry, user):
	try:
		return Vote.objects.get(user=user, entry=entry)
	except:
		return None