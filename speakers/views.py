# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Speaker, Talk


def index(request):

	return render(request, "index.html", {
		'speakers': Speaker.objects.filter(is_public=True),
	})

def speakers(request):

	return render(request, "speakers.html", {
		'speakers': Speaker.objects.filter(is_public=True),
	})

def talks(request):

	return render(request, "talks.html", {
		'talks': Talk.objects.filter(is_public=True),
	})