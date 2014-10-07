from django.db import models


class PerformanceTest(models.Model):
    char_field = models.CharField(max_length=2)
    pos_int = models.PositiveSmallIntegerField()
    char_field_index = models.CharField(max_length=2, db_index=True)
    pos_int_index = models.PositiveSmallIntegerField(db_index=True)
