from django.db import models


class Comment(models.Model):
    
    name = models.CharField(max_length=200, null=False)
    score = models.IntegerField(default=3)
    comments = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.name


# Create your models here.
