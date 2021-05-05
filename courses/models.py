from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Course name')
    date_start = models.DateField(verbose_name='Start date of course')
    date_end = models.DateField(verbose_name='End date of course')
    count_lectures = models.PositiveIntegerField(verbose_name='Lectures count')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['id']
