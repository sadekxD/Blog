from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='image/', default=r'C:\Users\Sadek Irfan\django\personal-blog\media\image\index.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_posted = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-time_posted']

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

