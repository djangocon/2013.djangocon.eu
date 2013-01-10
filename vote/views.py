# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import F
from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import simplejson as json

from vote.models import Entry, Vote
from vote.utils import json_response, json_error

def index(request):

	if request.user.is_authenticated():
		pks = cache.get('entry_pks_'+str(request.user.id))
		if pks == None:
			pks = Entry.objects.order_by('?').values_list('id', flat=True)
			cache.set('entry_pks_'+str(request.user.id), pks, 1209600)
	else:
		pks = Entry.objects.order_by('?').values_list('id', flat=True)

	ss = Entry.objects.all()
	entries = [s for p in pks for s in ss if s.pk == p]

	return render(request, "vote.html", {
		'entries': entries,
		'users': User.objects.all().count(),
		'votes': Vote.objects.all().count(),
	})

def add_vote(request, id=0, kind=2):
	if request.user.is_anonymous():
		return json_error('<a href="#signin">Sign in</a> to vote for submissions.')

	try:
		entry = Entry.objects.get(id=id)
	except Entry.DoesNotExist:
		return json_error('Entry does not exist.')

	try:
		kind = int(kind)
	except ValueError:
		return json_error('Wrong vote kind.')

	if kind < 0 or kind > 2:
		return json_error('Wrong vote kind.')

	if Vote.objects.filter(entry=entry, user=request.user).exists():
		return json_error('You can only add one vote for each entry.')

	Vote.objects.create(entry=entry, user=request.user, kind=kind)
	Entry.objects.filter(id=entry.id).update(score=F("score") + kind)
	return json_response({'result':'success', 'message':'Your vote has been counted.', 'score': Entry.objects.get(id=id).score})

@login_required
def cancel_vote(request, id=0):
	try:
		vote = Vote.objects.get(id=id, user=request.user)
	except Vote.DoesNotExist:
		return json_error('Vote does not exist.')

	entry = vote.entry
	Entry.objects.filter(id=entry.id).update(score=F("score") - vote.kind)
	vote.delete()

	return json_response({'result':'success', 'message':'Your vote has been cancelled.'})
