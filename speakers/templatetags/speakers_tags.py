# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter
def characters_length(value):
    return len(value)