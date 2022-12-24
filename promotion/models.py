from django.db import models

class Promotion(models.Model):

    title = models.CharField(max_length=255, null=False)
    cover_art = models.ImageField(default="cover-art.png")
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    facebook = models.BooleanField(null=False, default=True)
    twitter = models.BooleanField(null=False, default=True)
    instagram = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.title
    
