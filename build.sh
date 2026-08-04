#!/bin/bash

set -o errexit

echo "=========================================="
echo "Starting Build Process"
echo "=========================================="

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()

# Check if superuser exists
if not User.objects.filter(username='admin@gmail.com').exists():
    if not User.objects.filter(email='admin@gmail.com').exists():
        User.objects.create_superuser(
            username='admin@gmail.com',
            email='admin@gmail.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print("Superuser created successfully")
    else:
        print("User with email already exists but username differs, updating...")
        user = User.objects.get(email='admin@gmail.com')
        user.username = 'admin@gmail.com'
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print("Superuser updated successfully")
else:
    print("Superuser already exists, skipping creation")
EOF

echo "Seeding database with initial data..."
python seed_test_data.py || echo "Warning: Seeding had errors but continuing..."

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "=========================================="
echo "Build Completed Successfully!"
echo "=========================================="