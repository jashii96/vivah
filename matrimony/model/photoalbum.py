from django.db import models
from django.contrib.auth.models import User
class PhotoAlbum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image1 = models.ImageField(default='photo1.jpg', upload_to='photo_album')
    image2 = models.ImageField(default='photo2.jpg', upload_to='photo_album')
    image3 = models.ImageField(default='photo3.jpg', upload_to='photo_album')
    image4 = models.ImageField(default='photo4.jpg', upload_to='photo_album')
    image5 = models.ImageField(default='photo5.jpg', upload_to='photo_album')


    