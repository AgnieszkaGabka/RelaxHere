from datetime import datetime

from django.db import models

MONTH = (
    (1, 'January'),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December")
)

SCENERY = (
    (1, "forest"),
    (2, "ocean"),
    (3, "desert"),
    (4, "city"),
    (5, "mountains"),
    (6, "safari"),
)

ACTIVITY = (
    (1, 'Hiking'),
    (2, "Relax"),
    (3, "Surfing"),
    (4, "Safari"),
    (5, "Swimming"),
    (6, "Partying"),
    (7, "Jogging"),
    (8, "Snorkeling"),
    (9, "Kayaking"),
    (10, "Cruising"),
    (11, "Biking"),
    (12, "Sightseeing"),
    (13, "skiing"),
)

CLIMATE = (
    (1, "dry"),
    (2, "rainy"),
    (3, "hot"),
    (4, "warm"),
    (5, "windy"),
    (6, "sunny"),
    (7, "cloudy"),
    (7, "cold"),
)


CHILDREN_ACTIVITY = (
    (1, "park for children"),
    (2, "children swimming pool"),
    (3, "zoo"),
    (4, "playground"),
    (5, "bike rent"),
    (6, "game saloon"),
    (7, "gentle mountain routes"),
    (8, "none"),
)


CONTINENT = (
    (1, "North America"),
    (2, "South America"),
    (3, "Europe"),
    (4, "Asia"),
    (5, "Africa"),
    (6, "Australia"),
    (7, "Antarctica"),
)


class Scenery(models.Model):
    type = models.IntegerField(choices=SCENERY)


class Activities(models.Model):
    activity = models.IntegerField(choices=ACTIVITY)


class Climate(models.Model):
    climate = models.IntegerField(choices=CLIMATE)


class ChildrenActivities(models.Model):
    children_activity = models.IntegerField(choices=CHILDREN_ACTIVITY)


class Continent(models.Model):
    continent = models.IntegerField(choices=CONTINENT)


class Place(models.Model):
    name = models.CharField(max_length=255)
    visit_from = models.DateField(blank=True, default=datetime.now)
    visit_to = models.DateField(blank=True, default=datetime.now)
    climate = models.ForeignKey(Activities, on_delete=models.SET_NULL, null=True)
    activities = models.ForeignKey(Climate, on_delete=models.SET_NULL, null=True)
    children_friendly = models.ForeignKey(ChildrenActivities, on_delete=models.SET_NULL, null=True)
    scenery = models.ForeignKey(Scenery, on_delete=models.SET_NULL, null=True)
    continent = models.ForeignKey(Continent, on_delete=models.SET_NULL, null=True)
    long_stay = models.BooleanField()
    short_stay = models.BooleanField()