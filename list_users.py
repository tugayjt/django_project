import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')  # Replace 'django_project' with the correct name of your settings folder if it's different
django.setup()

from django.contrib.auth.models import User

# Fetch and print all users
users = User.objects.all()
for user in users:
    print(user)
