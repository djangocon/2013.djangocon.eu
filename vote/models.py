# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class Entry(models.Model):
	topic = models.CharField(max_length=255, null=False, blank=False)
	description = models.TextField(null=False, blank=False)
	score = models.IntegerField(default=0, null=False, blank=False)

	class Meta:
		verbose_name = "Call for papers: Entry"
		verbose_name_plural = "Call for papers: Entries"
		ordering = ('-score',)

	def __unicode__(self):
		return self.topic

class Vote(models.Model):
	entry = models.ForeignKey(Entry, null=False, blank=False)
	user = models.ForeignKey(User, null=False, blank=False)
	kind = models.IntegerField(null=False, blank=False, choices=((2,'MUST have!'),(1, 'Yaaay'),(0,'Meh')))
	created = models.DateTimeField(auto_now_add=True, null=False, blank=False)

	class Meta:
		verbose_name = "Call for papers: Vote"
		verbose_name_plural = "Call for papers: Votes"
		unique_together = ('entry', 'user')

	def __unicode__(self):
		return "%s's vote on %s" % (self.user.username, self.entry.topic)