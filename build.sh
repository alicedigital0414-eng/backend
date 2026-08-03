#!/bin/bash

set -o errexit

echo "=========================================="
echo "Starting Build Process"
echo "=========================================="

echo "Python version:"
python --version

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Force install psycopg2-binary with no build isolation
pip install --no-binary psycopg2-binary psycopg2-binary==2.9.10

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@gmail.com').exists():
    User.objects.create_superuser('admin@gmail.com', 'admin123', first_name='Admin', last_name='User')
    print("Superuser created")
else:
    print("Superuser already exists")
EOF

echo "Seeding database with initial data..."
python seed_test_data.py

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "=========================================="
echo "Build Completed Successfully!"
echo "=========================================="