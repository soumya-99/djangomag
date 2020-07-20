from django.db import models

# Create your models here.

class Content_Type(models.Model):
    typeC = models.CharField(max_length=50)

    def __str__(self):
        return self.typeC

class Content_Edition(models.Model):
    typeE = models.CharField(max_length=50)

    def __str__(self):
        return self.typeE

class Content_Year(models.Model):
    typeY = models.CharField(max_length=50)

    def __str__(self):
        return self.typeY

class All_Fields(models.Model):
    storyname = models.CharField(max_length=200)
    authorname = models.CharField(max_length=150)
    content = models.TextField()
    content_type = models.ForeignKey(Content_Type, on_delete=models.CASCADE)
    edition = models.ForeignKey(Content_Edition, on_delete=models.CASCADE)
    year = models.ForeignKey(Content_Year, on_delete=models.CASCADE)


class Image(models.Model):
    img = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.img