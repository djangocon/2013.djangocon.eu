# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.shortcuts import render

from pyquery import PyQuery

from .models import Speaker, Talk


def get_lanyard():
	page = PyQuery('http://lanyrd.com/2013/djangocon-europe/')
	h2 = page('h2.force')
	return int(PyQuery(h2[1]).text().split(' ')[0]) + int(PyQuery(h2[2]).text().split(' ')[0])

def index(request):

	lanyard = cache.get('dc_lanyard')
	if lanyard == None:
		lanyard = get_lanyard()
		cache.set('dc_lanyard', lanyard, 60*60*12)

	return render(request, "index.html", {
		'speakers': Speaker.objects.filter(is_public=True),
		'lanyard': lanyard,
	})

def speakers(request):

	return render(request, "speakers.html", {
		'speakers': Speaker.objects.filter(is_public=True),
	})

def talks(request):

	return render(request, "talks.html", {
		'talks': Talk.objects.filter(is_public=True),
	})