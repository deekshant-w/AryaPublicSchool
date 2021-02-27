from django.db import models
from django.utils import timezone

class information(models.Model):
	heading = models.TextField()
	details = models.TextField()
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)
	displayDate = models.DateTimeField(blank=True, help_text="Used to sort the all informations")
	archieve = models.BooleanField(default=False, help_text="Hides this information")
	important = models.BooleanField(default=False, help_text="Signifies that this is important")

	def save(self, *args, **kwargs):
		if not self.displayDate:
			self.displayDate = timezone.now()
		super().save(*args, **kwargs)

class notice(models.Model):
	heading = models.TextField()
	file = models.FileField()
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)
	displayDate = models.DateTimeField(blank=True, help_text="Used to sort the all informations")
	archieve = models.BooleanField(default=False, help_text="Hides this information")
	important = models.BooleanField(default=False, help_text="Signifies that this is important")

	def save(self, *args, **kwargs):
		if not self.displayDate:
			self.displayDate = timezone.now()
		super().save(*args, **kwargs)

class newPage(models.Model):
	heading = models.TextField()
	file = models.FileField(blank=True)
	image = models.ImageField()
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)
	displayDate = models.DateTimeField(blank=True, help_text="Used to sort the all informations")
	archieve = models.BooleanField(default=False, help_text="Hides this information")

	def save(self, *args, **kwargs):
		if not self.displayDate:
			self.displayDate = timezone.now()
		super().save(*args, **kwargs)

class loadingModal(models.Model):
	html = models.TextField()
	linkto = models.TextField()
	image = models.ImageField(blank=True)
	dateUpdated = models.DateTimeField(auto_now=True)
	archieve = models.BooleanField(default=False, help_text="Hides this information")

class AdminControls(models.Model):
	admissionsOn = models.BooleanField(default=True)
