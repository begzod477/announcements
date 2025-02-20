from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=75)
    def __str__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='announcements/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title[:50]
