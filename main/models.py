from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models
from django.utils.html import mark_safe

class information(models.Model):
	heading = models.CharField(max_length=1024)
	details = tinymce_models.HTMLField()
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)
	displayDate = models.DateTimeField(blank=True, help_text="Used to sort the all informations")
	archieve = models.BooleanField(default=False, help_text="Hides this information")
	important = models.BooleanField(default=False, help_text="Signifies that this is important")

	def save(self, *args, **kwargs):
		if not self.displayDate:
			self.displayDate = timezone.now()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.heading

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

	def __str__(self):
		return self.heading

class newPage(models.Model):
	url = models.CharField(max_length=1024, help_text="aryaSamaj.com/{YOUR INPUT}/")
	heading = models.CharField(max_length=1024)
	details = tinymce_models.HTMLField()
	image = models.ImageField()
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)
	displayDate = models.DateTimeField(blank=True, help_text="Used to sort the all informations")
	archieve = models.BooleanField(default=False, help_text="Hides this information")
	vertical = models.BooleanField(default=False, help_text="Dont Change this")

	def save(self, *args, **kwargs):
		if not self.displayDate:
			self.displayDate = timezone.now()
		if(self.image.height>self.image.width):
			self.vertival = True
		else:
			self.vertival = False
		self.url = self.url.lower().strip()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.heading


class loadingModal(models.Model):
	data = tinymce_models.HTMLField()
	linkto = models.CharField(max_length=1024)
	image = models.ImageField(blank=True)
	dateUpdated = models.DateTimeField(auto_now=True)
	archieve = models.BooleanField(default=False, help_text="Hides this information")

class AdminControls(models.Model):
	admissionsOn = models.BooleanField(default=True)
	def __str__(self):
		return "ON" if self.heading else "OFF"

