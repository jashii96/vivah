from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(blank = True, null = True ,upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' 
        # show how we want it to be displayed

    
    def save(self):
        super().save()
        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image
