from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Level(models.Model):
	group = [
		('อาหาร', 'อาหาร'),
		('วัตถุอันตราย', 'วัตถุอันตราย'),
		('วัตถุออกฤทธิ์-วัตถุเสพติด', 'วัตถุออกฤทธิ์-วัตถุเสพติด'),
		('ยา', 'ยา'),
		('เครื่องสำอาง', 'เครื่องสำอาง'),
		('เครื่องมือแพทย์', 'เครื่องมือแพทย์'),
		]

	level_id = models.AutoField(primary_key=True)
	level_state = models.CharField(max_length=2,default="")
	level_name = models.CharField(max_length=500,default="")
	level_ref = models.CharField(max_length=500,default="")
	level_role = models.CharField(max_length=500, default="")
	level_route = models.CharField(max_length=500, default="")
	level_link = models.ManyToManyField('Level', null=True, blank=True)
	group = models.CharField(max_length=255, choices=group,default="")
	Date = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.level_state+' '+ self.level_name

class Document(models.Model):
	group = [
		('อาหาร', 'อาหาร'),
		('วัตถุอันตราย', 'วัตถุอันตราย'),
		('วัตถุออกฤทธิ์-วัตถุเสพติด', 'วัตถุออกฤทธิ์-วัตถุเสพติด'),
		('ยา', 'ยา'),
		('เครื่องสำอาง', 'เครื่องสำอาง'),
		('เครื่องมือแพทย์', 'เครื่องมือแพทย์'),
	]

	document_id = models.AutoField(primary_key=True)
	document_name = models.CharField(max_length=500,default="")
	document_file = models.FileField(upload_to='uploads/')
	document_link = models.ManyToManyField('Level')
	group = models.CharField(max_length=255, choices=group,default="")

	def __str__(self):
		return self.document_name

