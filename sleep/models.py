from django.db import models

class Mood(models.Model):
    mood = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.mood}"
