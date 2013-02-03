# -*- coding: utf-8 -*-
from django.db import models

class Speaker(models.Model):
	first_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="First name")
	last_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Last name")
	title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Title")
	bio = models.TextField(null=True, blank=True, verbose_name="Bio")
	twitter = models.CharField(max_length=50, null=True, blank=True)
	slug = models.SlugField(null=False, blank=False, unique=True)
	is_public = models.BooleanField(default=False, null=False, blank=False)

	class Meta:
		verbose_name = "Speaker"

	def __unicode__(self):
		return "%s %s" % (self.first_name, self.last_name)

	def photo(self):
		return '/static/img/speakers/%s.png' % (self.slug.lower())

class Talk(models.Model):
	speaker = models.ManyToManyField(Speaker, null=True, blank=True)
	title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Talk title")
	description = models.TextField(null=False, blank=False, verbose_name="Description")
	is_public = models.BooleanField(default=False, null=False, blank=False)

	class Meta:
		verbose_name = "Talk"

	def __unicode__(self):
		return self.title

	def speakers_names(self):
		return ', '.join([str(a) for a in self.speaker.all()])
	speakers_names.short_description = "Speakers"