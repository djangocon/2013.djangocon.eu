# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import simplejson as json

from vote.models import Entry, Vote
from vote.utils import json_response, json_error

def index(request):

	return render(request, "vote.html", {
		'entries': Entry.objects.all(),
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

	if Vote.objects.filter(entry=entry, user=request.user).count() == 0:
		Vote.objects.create(entry=entry, user=request.user, kind=kind)
		entry.score += kind
		entry.save()
	else:
		return json_error('You can only add one vote for each entry.')

	return json_response({'result':'success', 'message':'Your vote has been counted.'})

@login_required
def cancel_vote(request, id=0):
	try:
		vote = Vote.objects.get(id=id, user=request.user)
	except Vote.DoesNotExist:
		return json_error('Vote does not exist.')

	entry = vote.entry
	entry.score -= vote.kind
	entry.save()
	vote.delete()

	return json_response({'result':'success', 'message':'Your vote has been cancelled.'})