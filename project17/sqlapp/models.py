from django.db import models

class studyonlinetable(models.Model):
	name = models.CharField(max_length=50)
	dob = models.DateField(max_length=50)
	mail_id = models.EmailField()
	phone_number = models.CharField(max_length=50)
	branch = models.CharField(max_length=50)

	def __str__(self):
		return self.name
