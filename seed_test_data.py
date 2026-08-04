import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from products.models import Product, Category

User = get_user_model()

# ─── Categories ──────────────────────────────────────────────────────────────
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

# ─── Today's date ────────────────────────────────────────────────────────────
today = datetime.now().date()

PRODUCTS = [
    # ─── EXPIRED PRODUCTS (Past dates) ─────────────────────────────────
    {'name': 'Organic Milk 1L', 'description': 'Fresh organic milk, pasteurized', 'category': 'Dairy Products', 'expiry_date': today - timedelta(days=15), 'batch_number': 'BATCH-MLK-001', 'quantity': 50, 'price': 3.99, 'alert_days': 3},
    {'name': 'Chicken Breast 500g', 'description': 'Fresh chicken breast, vacuum packed', 'category': 'Frozen Foods', 'expiry_date': today - timedelta(days=7), 'batch_number': 'BATCH-CHK-002', 'quantity': 30, 'price': 5.99, 'alert_days': 2},
    {'name': 'Pain Relief Tablets 30ct', 'description': 'Over-the-counter pain relief medication', 'category': 'Medicine & Healthcare', 'expiry_date': today - timedelta(days=45), 'batch_number': 'BATCH-MED-003', 'quantity': 100, 'price': 8.99, 'alert_days': 5},
    {'name': 'Vitamin C 60ct', 'description': 'Vitamin C supplement for immune support', 'category': 'Supplements & Vitamins', 'expiry_date': today - timedelta(days=20), 'batch_number': 'BATCH-VIT-004', 'quantity': 75, 'price': 12.99, 'alert_days': 7},
    {'name': 'Yogurt 500ml', 'description': 'Greek yogurt, plain', 'category': 'Dairy Products', 'expiry_date': today - timedelta(days=3), 'batch_number': 'BATCH-YOG-005', 'quantity': 40, 'price': 2.49, 'alert_days': 2},
    {'name': 'Ground Coffee 250g', 'description': 'Premium roasted coffee beans, ground', 'category': 'Beverages', 'expiry_date': today - timedelta(days=10), 'batch_number': 'BATCH-COF-006', 'quantity': 60, 'price': 6.99, 'alert_days': 5},
    {'name': 'Ice Cream 1L', 'description': 'Vanilla ice cream', 'category': 'Frozen Foods', 'expiry_date': today - timedelta(days=5), 'batch_number': 'BATCH-ICE-007', 'quantity': 25, 'price': 4.49, 'alert_days': 3},

    # ─── EXPIRING TODAY ─────────────────────────────────────────────────
    {'name': 'Fresh Bread 400g', 'description': 'Freshly baked whole wheat bread', 'category': 'Food & Beverages', 'expiry_date': today, 'batch_number': 'BATCH-BRD-008', 'quantity': 35, 'price': 2.99, 'alert_days': 1},
    {'name': 'Orange Juice 1L', 'description': '100% pure squeezed orange juice', 'category': 'Beverages', 'expiry_date': today, 'batch_number': 'BATCH-OJ-009', 'quantity': 45, 'price': 3.49, 'alert_days': 2},
    {'name': 'Face Cream 50ml', 'description': 'Moisturizing face cream', 'category': 'Cosmetics & Beauty', 'expiry_date': today, 'batch_number': 'BATCH-CRM-010', 'quantity': 20, 'price': 14.99, 'alert_days': 3},

    # ─── EXPIRING IN 2 DAYS ─────────────────────────────────────────────
    {'name': 'Cheese 200g', 'description': 'Cheddar cheese block', 'category': 'Dairy Products', 'expiry_date': today + timedelta(days=2), 'batch_number': 'BATCH-CHS-011', 'quantity': 55, 'price': 3.99, 'alert_days': 1},
    {'name': 'Canned Beans 400g', 'description': 'Baked beans in tomato sauce', 'category': 'Canned Goods', 'expiry_date': today + timedelta(days=2), 'batch_number': 'BATCH-BNS-012', 'quantity': 80, 'price': 1.99, 'alert_days': 2},

    # ─── EXPIRING IN 5 DAYS ─────────────────────────────────────────────
    {'name': 'Milk Chocolate Bar 100g', 'description': 'Smooth milk chocolate', 'category': 'Food & Beverages', 'expiry_date': today + timedelta(days=5), 'batch_number': 'BATCH-CHOC-013', 'quantity': 90, 'price': 1.49, 'alert_days': 3},
    {'name': 'Salmon Fillet 200g', 'description': 'Fresh Atlantic salmon fillet', 'category': 'Frozen Foods', 'expiry_date': today + timedelta(days=5), 'batch_number': 'BATCH-SLM-014', 'quantity': 15, 'price': 8.99, 'alert_days': 2},

    # ─── EXPIRING IN 7 DAYS ─────────────────────────────────────────────
    {'name': 'Eggs 6-pack', 'description': 'Free-range large eggs', 'category': 'Dairy Products', 'expiry_date': today + timedelta(days=7), 'batch_number': 'BATCH-EGG-015', 'quantity': 100, 'price': 2.49, 'alert_days': 3},
    {'name': 'Shampoo 500ml', 'description': 'Nourishing hair shampoo', 'category': 'Cosmetics & Beauty', 'expiry_date': today + timedelta(days=7), 'batch_number': 'BATCH-SHP-016', 'quantity': 40, 'price': 6.99, 'alert_days': 5},

    # ─── EXPIRING IN 14 DAYS ────────────────────────────────────────────
    {'name': 'Canned Soup 500ml', 'description': 'Creamy tomato soup', 'category': 'Canned Goods', 'expiry_date': today + timedelta(days=14), 'batch_number': 'BATCH-SOUP-017', 'quantity': 70, 'price': 2.99, 'alert_days': 5},
    {'name': 'Laptop Battery', 'description': 'Replacement laptop battery', 'category': 'Electronics', 'expiry_date': today + timedelta(days=14), 'batch_number': 'BATCH-BAT-018', 'quantity': 10, 'price': 49.99, 'alert_days': 7},

    # ─── EXPIRING IN 20 DAYS ────────────────────────────────────────────
    {'name': 'Chips 150g', 'description': 'Potato chips, salted', 'category': 'Food & Beverages', 'expiry_date': today + timedelta(days=20), 'batch_number': 'BATCH-CHIP-019', 'quantity': 120, 'price': 0.99, 'alert_days': 7},
    {'name': 'Multi-Vitamin 120ct', 'description': 'Complete daily multivitamin supplement', 'category': 'Supplements & Vitamins', 'expiry_date': today + timedelta(days=20), 'batch_number': 'BATCH-MVIT-020', 'quantity': 60, 'price': 19.99, 'alert_days': 14},

    # ─── EXPIRING IN 30 DAYS ────────────────────────────────────────────
    {'name': 'Granola Bar 6-pack', 'description': 'Oats and honey granola bars', 'category': 'Food & Beverages', 'expiry_date': today + timedelta(days=30), 'batch_number': 'BATCH-GRN-021', 'quantity': 85, 'price': 3.99, 'alert_days': 10},
    {'name': 'Toothpaste 100ml', 'description': 'Whitening toothpaste with fluoride', 'category': 'Cosmetics & Beauty', 'expiry_date': today + timedelta(days=30), 'batch_number': 'BATCH-TTH-022', 'quantity': 50, 'price': 2.49, 'alert_days': 14},
    {'name': 'Pasta 500g', 'description': 'Spaghetti pasta, durum wheat', 'category': 'Canned Goods', 'expiry_date': today + timedelta(days=30), 'batch_number': 'BATCH-PST-023', 'quantity': 110, 'price': 0.99, 'alert_days': 10},

    # ─── EXPIRING IN 40 DAYS ────────────────────────────────────────────
    {'name': 'Phone Charger', 'description': 'USB-C fast charging cable', 'category': 'Electronics', 'expiry_date': today + timedelta(days=40), 'batch_number': 'BATCH-CHG-024', 'quantity': 30, 'price': 9.99, 'alert_days': 20},
    {'name': 'Almond Milk 1L', 'description': 'Unsweetened almond milk', 'category': 'Beverages', 'expiry_date': today + timedelta(days=40), 'batch_number': 'BATCH-ALM-025', 'quantity': 65, 'price': 3.49, 'alert_days': 14},

    # ─── ACTIVE / LONG EXPIRY ───────────────────────────────────────────
    {'name': 'Rice 5kg', 'description': 'Premium long grain white rice', 'category': 'Canned Goods', 'expiry_date': today + timedelta(days=180), 'batch_number': 'BATCH-RIC-026', 'quantity': 150, 'price': 7.99, 'alert_days': 30},
    {'name': 'Olive Oil 500ml', 'description': 'Extra virgin olive oil', 'category': 'Food & Beverages', 'expiry_date': today + timedelta(days=365), 'batch_number': 'BATCH-OLI-027', 'quantity': 80, 'price': 12.99, 'alert_days': 60},
]

def seed_categories():
    """Seed categories if they don't exist"""
    print("📂 Seeding categories...")
    created_count = 0
    existing_count = 0
    
    for cat_data in CATEGORIES:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            created_count += 1
            print(f"  ✅ Created: {category.name}")
        else:
            existing_count += 1
    
    print(f"📊 Categories: {created_count} created, {existing_count} already exist")
    return created_count

def seed_products():
    """Seed products if they don't exist (check by batch_number)"""
    print("\n📦 Seeding products...")
    created_count = 0
    skipped_count = 0
    error_count = 0
    
    for product_data in PRODUCTS:
        try:
            # Get or create category
            category, _ = Category.objects.get_or_create(
                name=product_data['category']
            )
            
            # Check if product already exists by batch_number
            product, created = Product.objects.get_or_create(
                batch_number=product_data['batch_number'],
                defaults={
                    'name': product_data['name'],
                    'description': product_data['description'],
                    'category': category,
                    'expiry_date': product_data['expiry_date'],
                    'quantity': product_data['quantity'],
                    'price': product_data['price'],
                    'alert_days': product_data['alert_days'],
                }
            )
            
            if created:
                created_count += 1
                status = "🔴 EXPIRED" if product.expiry_date < today else "🟢 ACTIVE"
                print(f"  ✅ Created: {product.name} | Expiry: {product.expiry_date} | {status}")
            else:
                skipped_count += 1
                # Optionally update existing product
                # product.name = product_data['name']
                # product.save()
                
        except IntegrityError as e:
            error_count += 1
            print(f"  ❌ Error creating {product_data['name']}: {e}")
        except Exception as e:
            error_count += 1
            print(f"  ❌ Unexpected error for {product_data['name']}: {e}")
    
    print(f"📊 Products: {created_count} created, {skipped_count} skipped (already exist), {error_count} errors")
    return created_count

def check_database_connection():
    """Check if database is accessible"""
    try:
        from django.db import connection
        connection.ensure_connection()
        print("✅ Database connection successful!")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def main():
    print("=" * 60)
    print("🚀 SEEDING EXPIRY ALERT SYSTEM DATABASE")
    print("=" * 60)
    
    # Check database connection first
    if not check_database_connection():
        print("❌ Cannot proceed with seeding due to database connection issues.")
        return
    
    try:
        # Seed categories
        categories_created = seed_categories()
        
        # Seed products
        products_created = seed_products()
        
        # Summary
        print("\n" + "=" * 60)
        print("✅ SEEDING COMPLETE!")
        print("=" * 60)
        print(f"📊 Categories: {Category.objects.count()} total")
        print(f"📦 Products: {Product.objects.count()} total")
        print("\n📋 Product Status Summary:")
        print(f"  🔴 Expired: {Product.objects.filter(expiry_date__lt=today).count()}")
        print(f"  🟡 Expiring Today: {Product.objects.filter(expiry_date=today).count()}")
        print(f"  🟢 Active: {Product.objects.filter(expiry_date__gt=today).count()}")
        
        if categories_created == 0 and products_created == 0:
            print("\n⚠️ No new data was seeded. Database already contains data.")
        
    except Exception as e:
        print(f"\n❌ Seeding failed with error: {e}")
        raise

if __name__ == "__main__":
    main()