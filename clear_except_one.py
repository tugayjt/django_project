import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')  # Replace 'django_project' with your project name
django.setup()

from django.contrib.auth.models import User

# Get the user you want to keep (JbTugay in this case)
user_to_keep = User.objects.get(username='JbTugay')

# Delete all users except the one you want to keep
User.objects.exclude(username='JbTugay').delete()

print(f"All users except {user_to_keep.username} have been deleted.")
