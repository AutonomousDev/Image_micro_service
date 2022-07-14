from django.db import models


# Create your models here.
class ImageFile(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    alt_text = models.TextField()
    image_file = models.ImageField()

    def __str__(self) -> str:
        return self.name
