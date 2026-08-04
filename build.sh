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

# Check if superuser exists with username 'admin'
if not User.objects.filter(username='admin').exists():
    # Check if user exists with email
    if User.objects.filter(email='admin@gmail.com').exists():
        user = User.objects.get(email='admin@gmail.com')
        # Update username to 'admin'
        user.username = 'admin'
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print("Updated existing user to superuser with username 'admin'")
    else:
        # Create new superuser with username 'admin'
        User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print("Superuser 'admin' created successfully")
else:
    print("Superuser 'admin' already exists, skipping creation")
EOF

echo "Seeding database with initial data..."
python seed_test_data.py || echo "Warning: Seeding had errors but continuing..."

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "=========================================="
echo "Build Completed Successfully!"
echo "=========================================="