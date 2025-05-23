from django.db import models


class NewsCore(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()

    class Meta:
        db_table = 'newscore'

    def __str__(self):
        return self.title
