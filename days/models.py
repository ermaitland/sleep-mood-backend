from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Days(models.Model):
    user = models.ForeignKey('jwt_auth.User', related_name='days', on_delete=models.CASCADE)
    mood = models.ForeignKey('sleep.Mood', related_name='days', on_delete=models.CASCADE)
    sleep = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    day_logged = models.DateField(blank=True)


    def __str__(self):
        return f"{self.day_logged} - {self.user} - {self.mood}"
