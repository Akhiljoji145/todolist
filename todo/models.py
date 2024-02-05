from django.db import models

# Create your models here.
class TodoList(models.Model):
	name=models.CharField(max_length=250)
	priority=models.CharField(max_length=250)
	date=models.DateTimeField()

	def __str__(self):
		return self.name