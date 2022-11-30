from django.db import models


class Passenger(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    travel_points = models.IntegerField()

    def __str__(self):
        return "{} {} - {}".format(self.fname, self.lname, self.travel_points)
