from django.db import models
from django.utils import timezone
from .utils import generate_code

class Board(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('-created',)
    


class Status(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)




class Task(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)