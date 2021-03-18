from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=150)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
