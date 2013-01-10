# -*- coding: utf-8 -*-
import markdown

from django import template
from vote.models import Vote

register = template.Library()

@register.filter
def voted_by_user(entry, user):
	try:
		return Vote.objects.get(user=user, entry=entry)
	except:
		return None

@register.filter
def markdown_display(text):
	return markdown.markdown(text)