import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from products.models import Product, Category

User = get_user_model()

CATEGORIES = [
    {'name': 'Electronics', 'description': 'Gadgets, devices, and electronic equipment'},
    {'name': 'Food & Beverages', 'description': 'Perishable and packaged food items'},
    {'name': 'Medicine & Healthcare', 'description': 'Pharmaceuticals and medical supplies'},
    {'name': 'Cosmetics & Beauty', 'description': 'Skincare, makeup, and beauty products'},
    {'name': 'Supplements & Vitamins', 'description': 'Dietary supplements and vitamins'},
    {'name': 'Cleaning Supplies', 'description': 'Household and industrial cleaning products'},
    {'name': 'Beverages', 'description': 'Drinks and refreshments'},
    {'name': 'Dairy Products', 'description': 'Milk, cheese, yogurt and dairy items'},
    {'name': 'Frozen Foods', 'description': 'Frozen meals, vegetables, and meats'},
    {'name': 'Canned Goods', 'description': 'Canned vegetables, soups, and preserved foods'},
]

today = datetime.now().date()

PRODUCTS = [
    # EXPIRED PRODUCTS
    {
        'product_name': 'Organic Milk 1L',
        'description': 'Fresh organic milk, pasteurized',
        'category': 'Dairy Products',
        'sku': 'SKU-MLK-001',
        'batch_number': 'BATCH-MLK-001',
        'quantity': 50.00,
        'unit': 'litres',
        'manufacture_date': today - timedelta(days=30),
        'expiry_date': today - timedelta(days=15),
        'supplier_name': 'Fresh Farms Ltd',
        'is_active': True
    },
    {
        'product_name': 'Chicken Breast 500g',
        'description': 'Fresh chicken breast, vacuum packed',
        'category': 'Frozen Foods',
        'sku': 'SKU-CHK-002',
        'batch_number': 'BATCH-CHK-002',
        'quantity': 30.00,
        'unit': 'kg',
        'manufacture_date': today - timedelta(days=20),
        'expiry_date': today - timedelta(days=7),
        'supplier_name': 'Quality Meats Inc',
        'is_active': True
    },
    {
        'product_name': 'Pain Relief Tablets 30ct',
        'description': 'Over-the-counter pain relief medication',
        'category': 'Medicine & Healthcare',
        'sku': 'SKU-MED-003',
        'batch_number': 'BATCH-MED-003',
        'quantity': 100.00,
        'unit': 'tablets',
        'manufacture_date': today - timedelta(days=60),
        'expiry_date': today - timedelta(days=45),
        'supplier_name': 'PharmaCare Ltd',
        'is_active': True
    },
    {
        'product_name': 'Vitamin C 60ct',
        'description': 'Vitamin C supplement for immune support',
        'category': 'Supplements & Vitamins',
        'sku': 'SKU-VIT-004',
        'batch_number': 'BATCH-VIT-004',
        'quantity': 75.00,
        'unit': 'tablets',
        'manufacture_date': today - timedelta(days=40),
        'expiry_date': today - timedelta(days=20),
        'supplier_name': 'NutriHealth Ltd',
        'is_active': True
    },
    {
        'product_name': 'Yogurt 500ml',
        'description': 'Greek yogurt, plain',
        'category': 'Dairy Products',
        'sku': 'SKU-YOG-005',
        'batch_number': 'BATCH-YOG-005',
        'quantity': 40.00,
        'unit': 'ml',
        'manufacture_date': today - timedelta(days=10),
        'expiry_date': today - timedelta(days=3),
        'supplier_name': 'Dairy Fresh Ltd',
        'is_active': True
    },
    {
        'product_name': 'Ground Coffee 250g',
        'description': 'Premium roasted coffee beans, ground',
        'category': 'Beverages',
        'sku': 'SKU-COF-006',
        'batch_number': 'BATCH-COF-006',
        'quantity': 60.00,
        'unit': 'g',
        'manufacture_date': today - timedelta(days=60),
        'expiry_date': today - timedelta(days=10),
        'supplier_name': 'Coffee Roasters Ltd',
        'is_active': True
    },
    {
        'product_name': 'Ice Cream 1L',
        'description': 'Vanilla ice cream',
        'category': 'Frozen Foods',
        'sku': 'SKU-ICE-007',
        'batch_number': 'BATCH-ICE-007',
        'quantity': 25.00,
        'unit': 'litres',
        'manufacture_date': today - timedelta(days=15),
        'expiry_date': today - timedelta(days=5),
        'supplier_name': 'Frozen Delights Ltd',
        'is_active': True
    },
    # EXPIRING TODAY
    {
        'product_name': 'Fresh Bread 400g',
        'description': 'Freshly baked whole wheat bread',
        'category': 'Food & Beverages',
        'sku': 'SKU-BRD-008',
        'batch_number': 'BATCH-BRD-008',
        'quantity': 35.00,
        'unit': 'packs',
        'manufacture_date': today - timedelta(days=3),
        'expiry_date': today,
        'supplier_name': 'Bakery Fresh Ltd',
        'is_active': True
    },
    {
        'product_name': 'Orange Juice 1L',
        'description': '100% pure squeezed orange juice',
        'category': 'Beverages',
        'sku': 'SKU-OJ-009',
        'batch_number': 'BATCH-OJ-009',
        'quantity': 45.00,
        'unit': 'litres',
        'manufacture_date': today - timedelta(days=5),
        'expiry_date': today,
        'supplier_name': 'Juice Masters Ltd',
        'is_active': True
    },
    {
        'product_name': 'Face Cream 50ml',
        'description': 'Moisturizing face cream',
        'category': 'Cosmetics & Beauty',
        'sku': 'SKU-CRM-010',
        'batch_number': 'BATCH-CRM-010',
        'quantity': 20.00,
        'unit': 'ml',
        'manufacture_date': today - timedelta(days=90),
        'expiry_date': today,
        'supplier_name': 'Beauty Plus Ltd',
        'is_active': True
    },
    # EXPIRING IN 2 DAYS
    {
        'product_name': 'Cheese 200g',
        'description': 'Cheddar cheese block',
        'category': 'Dairy Products',
        'sku': 'SKU-CHS-011',
        'batch_number': 'BATCH-CHS-011',
        'quantity': 55.00,
        'unit': 'g',
        'manufacture_date': today - timedelta(days=20),
        'expiry_date': today + timedelta(days=2),
        'supplier_name': 'Dairy Fresh Ltd',
        'is_active': True
    },
    {
        'product_name': 'Canned Beans 400g',
        'description': 'Baked beans in tomato sauce',
        'category': 'Canned Goods',
        'sku': 'SKU-BNS-012',
        'batch_number': 'BATCH-BNS-012',
        'quantity': 80.00,
        'unit': 'g',
        'manufacture_date': today - timedelta(days=180),
        'expiry_date': today + timedelta(days=2),
        'supplier_name': 'Canned Foods Ltd',
        'is_active': True
    },
    # EXPIRING IN 5 DAYS
    {
        'product_name': 'Milk Chocolate Bar 100g',
        'description': 'Smooth milk chocolate',
        'category': 'Food & Beverages',
        'sku': 'SKU-CHOC-013',
        'batch_number': 'BATCH-CHOC-013',
        'quantity': 90.00,
        'unit': 'packs',
        'manufacture_date': today - timedelta(days=30),
        'expiry_date': today + timedelta(days=5),
        'supplier_name': 'Chocolate Factory Ltd',
        'is_active': True
    },
    {
        'product_name': 'Salmon Fillet 200g',
        'description': 'Fresh Atlantic salmon fillet',
        'category': 'Frozen Foods',
        'sku': 'SKU-SLM-014',
        'batch_number': 'BATCH-SLM-014',
        'quantity': 15.00,
        'unit': 'kg',
        'manufacture_date': today - timedelta(days=5),
        'expiry_date': today + timedelta(days=5),
        'supplier_name': 'Seafood Express Ltd',
        'is_active': True
    },
    # EXPIRING IN 7 DAYS
    {
        'product_name': 'Eggs 6-pack',
        'description': 'Free-range large eggs',
        'category': 'Dairy Products',
        'sku': 'SKU-EGG-015',
        'batch_number': 'BATCH-EGG-015',
        'quantity': 100.00,
        'unit': 'packs',
        'manufacture_date': today - timedelta(days=10),
        'expiry_date': today + timedelta(days=7),
        'supplier_name': 'Farm Fresh Eggs Ltd',
        'is_active': True
    },
    {
        'product_name': 'Shampoo 500ml',
        'description': 'Nourishing hair shampoo',
        'category': 'Cosmetics & Beauty',
        'sku': 'SKU-SHP-016',
        'batch_number': 'BATCH-SHP-016',
        'quantity': 40.00,
        'unit': 'ml',
        'manufacture_date': today - timedelta(days=60),
        'expiry_date': today + timedelta(days=7),
        'supplier_name': 'Hair Care Ltd',
        'is_active': True
    },
    # EXPIRING IN 14 DAYS
    {
        'product_name': 'Canned Soup 500ml',
        'description': 'Creamy tomato soup',
        'category': 'Canned Goods',
        'sku': 'SKU-SOUP-017',
        'batch_number': 'BATCH-SOUP-017',
        'quantity': 70.00,
        'unit': 'ml',
        'manufacture_date': today - timedelta(days=180),
        'expiry_date': today + timedelta(days=14),
        'supplier_name': 'Soup Kitchen Ltd',
        'is_active': True
    },
    {
        'product_name': 'Laptop Battery',
        'description': 'Replacement laptop battery',
        'category': 'Electronics',
        'sku': 'SKU-BAT-018',
        'batch_number': 'BATCH-BAT-018',
        'quantity': 10.00,
        'unit': 'pieces',
        'manufacture_date': today - timedelta(days=30),
        'expiry_date': today + timedelta(days=14),
        'supplier_name': 'Tech Parts Ltd',
        'is_active': True
    },
    # EXPIRING IN 20 DAYS
    {
        'product_name': 'Chips 150g',
        'description': 'Potato chips, salted',
        'category': 'Food & Beverages',
        'sku': 'SKU-CHIP-019',
        'batch_number': 'BATCH-CHIP-019',
        'quantity': 120.00,
        'unit': 'packs',
        'manufacture_date': today - timedelta(days=30),
        'expiry_date': today + timedelta(days=20),
        'supplier_name': 'Snacks Ltd',
        'is_active': True
    },
    {
        'product_name': 'Multi-Vitamin 120ct',
        'description': 'Complete daily multivitamin supplement',
        'category': 'Supplements & Vitamins',
        'sku': 'SKU-MVIT-020',
        'batch_number': 'BATCH-MVIT-020',
        'quantity': 60.00,
        'unit': 'tablets',
        'manufacture_date': today - timedelta(days=90),
        'expiry_date': today + timedelta(days=20),
        'supplier_name': 'NutriHealth Ltd',
        'is_active': True
    },
    # EXPIRING IN 30 DAYS
    {
        'product_name': 'Granola Bar 6-pack',
        'description': 'Oats and honey granola bars',
        'category': 'Food & Beverages',
        'sku': 'SKU-GRN-021',
        'batch_number': 'BATCH-GRN-021',
        'quantity': 85.00,
        'unit': 'packs',
        'manufacture_date': today - timedelta(days=60),
        'expiry_date': today + timedelta(days=30),
        'supplier_name': 'Healthy Snacks Ltd',
        'is_active': True
    },
    {
        'product_name': 'Toothpaste 100ml',
        'description': 'Whitening toothpaste with fluoride',
        'category': 'Cosmetics & Beauty',
        'sku': 'SKU-TTH-022',
        'batch_number': 'BATCH-TTH-022',
        'quantity': 50.00,
        'unit': 'ml',
        'manufacture_date': today - timedelta(days=90),
        'expiry_date': today + timedelta(days=30),
        'supplier_name': 'Oral Care Ltd',
        'is_active': True
    },
    {
        'product_name': 'Pasta 500g',
        'description': 'Spaghetti pasta, durum wheat',
        'category': 'Canned Goods',
        'sku': 'SKU-PST-023',
        'batch_number': 'BATCH-PST-023',
        'quantity': 110.00,
        'unit': 'g',
        'manufacture_date': today - timedelta(days=180),
        'expiry_date': today + timedelta(days=30),
        'supplier_name': 'Pasta Italia Ltd',
        'is_active': True
    },
    # EXPIRING IN 40 DAYS
    {
        'product_name': 'Phone Charger',
        'description': 'USB-C fast charging cable',
        'category': 'Electronics',
        'sku': 'SKU-CHG-024',
        'batch_number': 'BATCH-CHG-024',
        'quantity': 30.00,
        'unit': 'pieces',
        'manufacture_date': today - timedelta(days=60),
        'expiry_date': today + timedelta(days=40),
        'supplier_name': 'Tech Accessories Ltd',
        'is_active': True
    },
    {
        'product_name': 'Almond Milk 1L',
        'description': 'Unsweetened almond milk',
        'category': 'Beverages',
        'sku': 'SKU-ALM-025',
        'batch_number': 'BATCH-ALM-025',
        'quantity': 65.00,
        'unit': 'litres',
        'manufacture_date': today - timedelta(days=30),
        'expiry_date': today + timedelta(days=40),
        'supplier_name': 'Plant Based Ltd',
        'is_active': True
    },
    # LONG EXPIRY
    {
        'product_name': 'Rice 5kg',
        'description': 'Premium long grain white rice',
        'category': 'Canned Goods',
        'sku': 'SKU-RIC-026',
        'batch_number': 'BATCH-RIC-026',
        'quantity': 150.00,
        'unit': 'kg',
        'manufacture_date': today - timedelta(days=60),
        'expiry_date': today + timedelta(days=180),
        'supplier_name': 'Global Grains Ltd',
        'is_active': True
    },
    {
        'product_name': 'Olive Oil 500ml',
        'description': 'Extra virgin olive oil',
        'category': 'Food & Beverages',
        'sku': 'SKU-OLI-027',
        'batch_number': 'BATCH-OLI-027',
        'quantity': 80.00,
        'unit': 'ml',
        'manufacture_date': today - timedelta(days=90),
        'expiry_date': today + timedelta(days=365),
        'supplier_name': 'Mediterranean Foods Ltd',
        'is_active': True
    },
]

def seed_categories():
    print("Seeding categories...")
    count = 0
    for cat_data in CATEGORIES:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            count += 1
            print(f"  Created: {category.name}")
    print(f"Categories seeded: {count}")
    return count

def seed_products():
    print("\nSeeding products...")
    count = 0
    errors = 0
    
    for product_data in PRODUCTS:
        try:
            category = Category.objects.get(name=product_data['category'])
        except Category.DoesNotExist:
            print(f"  Warning: Category '{product_data['category']}' not found, skipping...")
            errors += 1
            continue

        # Remove category from data for create
        product_dict = product_data.copy()
        product_dict.pop('category')
        
        # Create or get product
        product, created = Product.objects.get_or_create(
            sku=product_dict['sku'],
            defaults=product_dict
        )
        
        if created:
            count += 1
            status = "EXPIRED" if product.expiry_date < today else "ACTIVE"
            days = (product.expiry_date - today).days
            print(f"  Created: {product.product_name} | Expiry: {product.expiry_date} | Days: {days} | Status: {status}")
        else:
            print(f"  Skipped: {product.product_name} (already exists)")
            
    print(f"Products seeded: {count}")
    if errors > 0:
        print(f"  Errors: {errors}")
    return count

def main():
    print("=" * 60)
    print("SEEDING EXPIRY ALERT SYSTEM DATABASE")
    print("=" * 60)
    
    try:
        # Test database connection
        from django.db import connection
        connection.ensure_connection()
        print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")
        return
    
    # Get or create admin user for added_by field
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@gmail.com',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print("Admin user created")
    
    # Run seeding
    categories_count = seed_categories()
    products_count = seed_products()
    
    print("\n" + "=" * 60)
    print("SEEDING COMPLETE!")
    print("=" * 60)
    print(f"Categories: {Category.objects.count()}")
    print(f"Products: {Product.objects.count()}")
    print("\nProduct Status Summary:")
    print(f"  Expired: {Product.objects.filter(expiry_date__lt=today).count()}")
    print(f"  Expiring Today: {Product.objects.filter(expiry_date=today).count()}")
    print(f"  Active: {Product.objects.filter(expiry_date__gt=today).count()}")

if __name__ == "__main__":
    main()