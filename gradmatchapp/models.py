from django.db import models


# Create your models here.
class Deadline(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    priority = models.CharField(max_length=200)


class Location(models.Model):

	def __str__(self):
		return self.location_name

	location_name = models.CharField(max_length=200)
	location_type = models.CharField(max_length=200)


class School(models.Model):

	def __str__(self):
		return self.school_name

	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	school_name = models.CharField(max_length=200, default="")
	area = models.CharField(max_length=200, default="")
	tuition = models.CharField(max_length=200, default="")
	acceptance_rate = models.CharField(max_length=200, default="")
	graduation_rate = models.CharField(max_length=200, default="")
	student_pop = models.CharField(max_length=200, default="")
	image_url = models.CharField(max_length=200, default="")
