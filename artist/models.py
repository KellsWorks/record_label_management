from django.db import models
from content.models import Genre
from user.models import User

class Artist(models.Model):

    GENDER_CHOICES = ("Male", "Female")

    account = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="user.png")
    height = models.IntegerField(default=6)
    gender = models.CharField(max_length=40, default="Male", choices=GENDER_CHOICES)
    location = models.CharField(max_length=255, null=False)
    date_of_birth = models.DateField(null=False)
    genre = models.ForeignKey(Genre, default=1, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'${self.account.first_name} ${self.account.last_name}'
