from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    recommender = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-update', '-created']

    def __str__(self)-> str:
        return self.title
