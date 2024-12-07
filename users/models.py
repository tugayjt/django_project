from django.db import models
from django.contrib.auth.models import User
from PIL import Image,UnidentifiedImageError
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the user first

        # Only process the image if it exists
        if self.image and os.path.exists(self.image.path):
            try:
                img = Image.open(self.image.path)
                # Resize the image if it exceeds 300x300
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
            except (OSError, UnidentifiedImageError) as e:
                print(f"Error processing image {self.image.path}: {e}")
                # Optionally, handle this by logging or setting a default image
