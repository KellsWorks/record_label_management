from django.db import models

class song(models.Model):

    title = models.CharField(max_length=255, null=False)
    audio = models.FileField(null=False)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    