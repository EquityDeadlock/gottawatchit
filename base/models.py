from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30)
    count = models.PositiveIntegerField()

    class Meta:
        ordering = ['-count', '-name']

    def __str__(self) -> str:
        return self.name

class Media(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    recommender = models.CharField(max_length=200)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-update', '-created']

    def __str__(self)-> str:
        return self.title

