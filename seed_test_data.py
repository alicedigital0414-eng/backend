"""
=============================================================================
  PRODUCTS EXPIRY ALERT MANAGEMENT SYSTEM
  Test Data Seeder Script — 1000 Realistic Products
=============================================================================
  HOW TO RUN:
    1. Make sure your virtual environment is activated
    2. Navigate to the backend folder:
           cd expiry-system/backend
    3. Run the script:
           python seed_test_data.py
  
  WHAT IT DOES:
    - Creates 8 product categories (Pharmacy, Food, Cosmetics, etc.)
    - Creates 5 test user accounts
    - Creates 3 alert threshold configurations
    - Seeds 1000 products with varied expiry dates:
        * 120 already EXPIRED (days < 0)
        * 40  expiring TODAY (day 0)
        * 50  expiring in 1–7 days (CRITICAL)
        * 80  expiring in 8–14 days (WARNING)
        * 150 expiring in 15–30 days (NEAR EXPIRY)
        * 560 expiring in 31–730 days (SAFE)
    - All products come from realistic Nigerian/global brands
=============================================================================
"""

import os
import sys
import django
import random
from datetime import date, timedelta

# ── Django setup ──────────────────────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile
from products.models import Category, Product, AlertConfiguration, NotificationLog

# ── Helpers ───────────────────────────────────────────────────────────────────
TODAY = date.today()

def days_from_today(n):
    return TODAY + timedelta(days=n)

def mfg_date(expiry, shelf_life_months=24):
    return expiry - timedelta(days=shelf_life_months * 30)

def rand_sku(prefix, n):
    return f"{prefix}-{str(n).zfill(5)}"

def rand_batch():
    yr = random.randint(22, 25)
    mo = str(random.randint(1, 12)).zfill(2)
    seq = random.randint(100, 999)
    return f"B{yr}{mo}-{seq}"

def pick(lst):
    return random.choice(lst)

# ── Category definitions ──────────────────────────────────────────────────────
CATEGORIES = [
    ("Pharmaceuticals",      "Prescription and OTC drugs, medicines"),
    ("Food & Beverages",     "Packaged foods, drinks, snacks"),
    ("Cosmetics & Beauty",   "Skincare, haircare, personal hygiene"),
    ("Dairy & Perishables",  "Milk, cheese, yogurt, eggs"),
    ("Household Chemicals",  "Disinfectants, cleaning agents, pesticides"),
    ("Medical Supplies",     "Consumables, devices, diagnostics"),
    ("Baby Products",        "Infant formula, diapers, baby food"),
    ("Herbal & Supplements", "Vitamins, herbal remedies, nutraceuticals"),
]

# ── Suppliers ─────────────────────────────────────────────────────────────────
SUPPLIERS = [
    "Lagos Pharma Distributors Ltd", "Emzor Pharmaceutical", "May & Baker Nigeria",
    "GSK Nigeria", "Pfizer Nigeria", "Fidson Healthcare", "Strides Pharma",
    "Shalina Healthcare", "Chi Limited", "Dano Foods Nigeria", "Nestlé Nigeria",
    "Unilever Nigeria", "PZ Cussons Nigeria", "Procter & Gamble Nigeria",
    "NAFDAC Approved Imports Ltd", "Sunridge Foods", "Cadbury Nigeria",
    "Flour Mills Nigeria", "Friesland Campina WAMCO", "Vitafoam Nigeria",
    "Aba Medical Supplies", "Medline Nigeria", "PharmaDeko", "Jawa International",
    "Kopak Limited", "Seven-Up Bottling Company", "Coca-Cola Nigeria",
    "Nigerian Breweries", "TGI Group", "Dangote Sugar Refinery",
]

# ─────────────────────────────────────────────────────────────────────────────
# PRODUCT TEMPLATES per category
# Format: (name_template, unit, shelf_life_months)
# ─────────────────────────────────────────────────────────────────────────────

PHARMA_PRODUCTS = [
    ("Paracetamol 500mg Tablets",         "tablets",  24),
    ("Paracetamol 250mg Syrup 100ml",     "bottles",  24),
    ("Amoxicillin 250mg Capsules",        "capsules", 24),
    ("Amoxicillin 500mg Capsules",        "capsules", 24),
    ("Amoxicillin-Clavulanate 625mg",     "tablets",  24),
    ("Ibuprofen 200mg Tablets",           "tablets",  36),
    ("Ibuprofen 400mg Tablets",           "tablets",  36),
    ("Diclofenac 50mg Tablets",           "tablets",  36),
    ("Diclofenac Sodium 75mg Injection",  "ml",       24),
    ("Metronidazole 200mg Tablets",       "tablets",  36),
    ("Metronidazole 400mg Tablets",       "tablets",  36),
    ("Metronidazole 500mg Injection",     "ml",       24),
    ("Ciprofloxacin 250mg Tablets",       "tablets",  36),
    ("Ciprofloxacin 500mg Tablets",       "tablets",  36),
    ("Cotrimoxazole 480mg Tablets",       "tablets",  36),
    ("Doxycycline 100mg Capsules",        "capsules", 36),
    ("Erythromycin 250mg Capsules",       "capsules", 24),
    ("Fluconazole 150mg Capsules",        "capsules", 36),
    ("Artemether-Lumefantrine 80/480mg",  "tablets",  24),
    ("Artesunate 100mg Tablets",          "tablets",  24),
    ("Chloroquine 250mg Tablets",         "tablets",  36),
    ("Amlodipine 5mg Tablets",            "tablets",  36),
    ("Amlodipine 10mg Tablets",           "tablets",  36),
    ("Lisinopril 5mg Tablets",            "tablets",  36),
    ("Lisinopril 10mg Tablets",           "tablets",  36),
    ("Atenolol 50mg Tablets",             "tablets",  36),
    ("Atenolol 100mg Tablets",            "tablets",  36),
    ("Metformin 500mg Tablets",           "tablets",  36),
    ("Metformin 850mg Tablets",           "tablets",  36),
    ("Glibenclamide 5mg Tablets",         "tablets",  36),
    ("Insulin Glargine 100IU/ml",         "ml",       24),
    ("Omeprazole 20mg Capsules",          "capsules", 24),
    ("Omeprazole 40mg Capsules",          "capsules", 24),
    ("Ranitidine 150mg Tablets",          "tablets",  36),
    ("Hydroxychloroquine 200mg Tablets",  "tablets",  36),
    ("Prednisolone 5mg Tablets",          "tablets",  36),
    ("Dexamethasone 4mg Injection",       "ml",       24),
    ("Diazepam 5mg Tablets",              "tablets",  36),
    ("Phenobarbitone 30mg Tablets",       "tablets",  36),
    ("Folic Acid 5mg Tablets",            "tablets",  36),
    ("Ferrous Sulphate 200mg Tablets",    "tablets",  36),
    ("Vitamin C 500mg Tablets",           "tablets",  24),
    ("Vitamin B-Complex Tablets",         "tablets",  24),
    ("Zinc Sulphate 20mg Tablets",        "tablets",  24),
    ("Oral Rehydration Salts Sachet",     "packs",    36),
    ("Mebendazole 100mg Tablets",         "tablets",  36),
    ("Albendazole 400mg Tablets",         "tablets",  36),
    ("Tetracycline 250mg Capsules",       "capsules", 36),
    ("Tramadol 50mg Capsules",            "capsules", 36),
    ("Morphine Sulphate 10mg Tablets",    "tablets",  24),
    ("Cetirizine 10mg Tablets",           "tablets",  36),
    ("Loratadine 10mg Tablets",           "tablets",  36),
    ("Salbutamol 100mcg Inhaler",         "pieces",   24),
    ("Fluticasone 125mcg Inhaler",        "pieces",   24),
    ("Gentamicin Eye Drops 0.3%",         "ml",       24),
    ("Chloramphenicol Eye Drops 0.5%",    "ml",       12),
    ("Tetracycline Eye Ointment 1%",      "g",        24),
    ("Clotrimazole Cream 1%",             "g",        36),
    ("Ketoconazole Shampoo 2%",           "ml",       24),
    ("Nystatin Pessary 100,000 IU",       "pieces",   24),
    ("Hydrocortisone Cream 1%",           "g",        36),
    ("Permethrin Cream 5%",               "g",        24),
    ("Silver Sulfadiazine Cream 1%",      "g",        24),
    ("Normal Saline 0.9% 500ml",          "ml",       36),
    ("Dextrose 5% in Water 500ml",        "ml",       36),
    ("Ringers Lactate 500ml",             "ml",       36),
    ("Heparin 5000IU/ml Injection",       "ml",       24),
    ("Warfarin 5mg Tablets",              "tablets",  36),
    ("Atorvastatin 20mg Tablets",         "tablets",  36),
    ("Simvastatin 40mg Tablets",          "tablets",  36),
    ("Levothyroxine 50mcg Tablets",       "tablets",  24),
    ("Carbamazepine 200mg Tablets",       "tablets",  36),
    ("Valproic Acid 200mg Tablets",       "tablets",  36),
    ("Azithromycin 250mg Capsules",       "capsules", 36),
    ("Levofloxacin 500mg Tablets",        "tablets",  36),
    ("Rifampicin 300mg Capsules",         "capsules", 24),
    ("Isoniazid 100mg Tablets",           "tablets",  36),
    ("Pyrazinamide 500mg Tablets",        "tablets",  36),
    ("Ethambutol 400mg Tablets",          "tablets",  36),
    ("Efavirenz 600mg Tablets",           "tablets",  24),
    ("Lamivudine 150mg Tablets",          "tablets",  24),
    ("Tenofovir 300mg Tablets",           "tablets",  24),
    ("Nevirapine 200mg Tablets",          "tablets",  24),
    ("Lopinavir/Ritonavir 200/50mg",      "tablets",  24),
    ("Aspirin 75mg Tablets",              "tablets",  36),
    ("Clopidogrel 75mg Tablets",          "tablets",  36),
    ("Furosemide 40mg Tablets",           "tablets",  36),
    ("Spironolactone 25mg Tablets",       "tablets",  36),
    ("Digoxin 0.25mg Tablets",            "tablets",  36),
    ("Nifedipine 10mg Tablets",           "tablets",  36),
    ("Methyldopa 250mg Tablets",          "tablets",  36),
    ("Promethazine 25mg Tablets",         "tablets",  36),
    ("Hyoscine Butylbromide 20mg",        "tablets",  36),
    ("Magnesium Trisilicate Suspension",  "ml",       24),
    ("Lactulose Syrup 3.35g/5ml",         "ml",       36),
    ("Bisacodyl 5mg Tablets",             "tablets",  36),
    ("Loperamide 2mg Capsules",           "capsules", 36),
    ("Ondansetron 4mg Tablets",           "tablets",  24),
    ("Domperidone 10mg Tablets",          "tablets",  36),
    ("Betamethasone Cream 0.1%",          "g",        36),
]

FOOD_PRODUCTS = [
    ("Indomie Instant Noodles Chicken 70g",     "packs",   12),
    ("Indomie Instant Noodles Onion 70g",       "packs",   12),
    ("Golden Morn Maize Oats 500g",             "packs",   18),
    ("Milo Chocolate Drink 400g",               "pieces",  24),
    ("Nescafé Classic 200g",                    "pieces",  24),
    ("Peak Milk Powder 400g",                   "pieces",  18),
    ("Dano Full Cream Milk Powder 360g",        "pieces",  18),
    ("Cowbell Milk 400g",                       "pieces",  24),
    ("Bournvita 500g",                          "pieces",  24),
    ("Ovaltine 400g",                           "pieces",  24),
    ("Tomato Paste Taris 70g",                  "pieces",   6),
    ("Tomato Paste Gino 210g",                  "pieces",  12),
    ("Groundnut Oil 1 Litre",                   "litres",  18),
    ("Vegetable Oil Mamador 2L",                "litres",  18),
    ("Palm Oil Oiled Up 1L",                    "litres",  12),
    ("Sugar Dangote 1kg",                       "kg",      36),
    ("Salt Annapurna Iodized 1kg",              "kg",      36),
    ("Spaghetti Dufil 500g",                    "packs",   24),
    ("Macaroni Golden Penny 500g",              "packs",   24),
    ("Rice Uncle Ben's Parboiled 5kg",          "packs",   36),
    ("Semolina Honeywell 1kg",                  "kg",      24),
    ("Cornflour Tata 1kg",                      "kg",      24),
    ("Soy Sauce Kikkoman 250ml",                "ml",      36),
    ("Ketchup Heinz 570g",                      "pieces",  24),
    ("Mayonnaise Bama 500g",                    "pieces",  12),
    ("Sardines Crown in Tomato Sauce 125g",     "pieces",  48),
    ("Mackerel Titus in Oil 400g",              "pieces",  48),
    ("Baked Beans Heinz 415g",                  "pieces",  48),
    ("Corned Beef Exeter 340g",                 "pieces",  48),
    ("Evaporated Milk Carnation 410g",          "pieces",  36),
    ("Evaporated Milk Peak 410g",               "pieces",  36),
    ("Coconut Milk Kara 400ml",                 "ml",      24),
    ("Custard Power Carozzi 1kg",               "kg",      18),
    ("Wheat Flour Honeywell 2kg",               "kg",      12),
    ("Bread Flour Supreme 2kg",                 "kg",      12),
    ("Peanut Butter Skippy 500g",               "pieces",  18),
    ("Jam Strawberry Sundew 450g",              "pieces",  24),
    ("Honey Natural Nestlé 500g",               "pieces",  36),
    ("Oats Quaker 500g",                        "pieces",  18),
    ("Corn Flakes Kellogg's 500g",              "pieces",  18),
    ("Biscuit Cabin 250g",                      "pieces",   6),
    ("Crackers TUC 100g",                       "pieces",   9),
    ("Digestive Biscuit McVitie's 250g",        "pieces",  12),
    ("Chocolate Cadbury Dairy Milk 100g",       "pieces",  18),
    ("Chips Pringles Original 165g",            "pieces",   9),
    ("Plantain Chips Amaize 100g",              "packs",    6),
    ("Popcorn Pop Time 100g",                   "packs",    6),
    ("Groundnut Coaster 150g",                  "packs",   12),
    ("Fruit Juice Chivita 1L",                  "litres",   9),
    ("Fruit Juice Five Alive 500ml",            "ml",       9),
    ("Malta Guinness Can 330ml",                "pieces",  12),
    ("Pepsi Can 330ml",                         "pieces",  12),
    ("Coca-Cola Can 330ml",                     "pieces",  12),
    ("7UP Can 330ml",                           "pieces",  12),
    ("Sprite Bottle 500ml",                     "ml",      12),
    ("Fanta Orange 500ml",                      "ml",      12),
    ("Ribena Blackcurrant 300ml",               "ml",      12),
    ("Volvic Water 1.5L",                       "litres",  24),
    ("Eva Water 1.5L",                          "litres",  24),
    ("Table Salt Cerebos 750g",                 "g",       36),
    ("Crayfish Ground 200g",                    "g",       12),
    ("Knorr Chicken Seasoning Cube x10",        "pieces",  24),
    ("Maggi Seasoning Cubes x10",               "pieces",  24),
    ("Curry Powder Rajah 100g",                 "g",       24),
    ("Turmeric Powder 100g",                    "g",       24),
    ("Pepper Dried Ground 100g",                "g",        6),
    ("Egusi Ground 500g",                       "g",        6),
    ("Crayfish Dried Powder 200g",              "g",        6),
    ("Ogiri Wrap 100g",                         "pieces",   3),
    ("Locust Beans Iru 100g",                   "g",        3),
    ("Agege Bread 600g",                        "pieces",   0),  # 3 days shelf life
    ("Hollandia Yoghurt Strawberry 500ml",      "ml",       1),
    ("Chi Exotic Mango Juice 1L",               "litres",   9),
    ("Lacasera Apple 500ml",                    "ml",       9),
    ("Power Horse Energy Drink 250ml",          "ml",      12),
    ("Burn Energy Drink 250ml",                 "ml",      12),
    ("Tiger Energy Drink 250ml",                "ml",      12),
]

COSMETICS_PRODUCTS = [
    ("Nivea Moisturizing Cream 200ml",          "ml",      36),
    ("Nivea Body Lotion 400ml",                 "ml",      36),
    ("Dove Beauty Bar Soap 135g",               "g",       36),
    ("Lux Soap White 125g",                     "g",       36),
    ("Dettol Original Soap 100g",               "g",       36),
    ("Lifebuoy Soap Total 10 125g",             "g",       36),
    ("Pears Transparent Soap 125g",             "g",       36),
    ("Tura Papaya Soap 150g",                   "g",       36),
    ("Fair & White So White Body Milk 500ml",   "ml",      36),
    ("Vaseline Intensive Care Lotion 400ml",    "ml",      36),
    ("Jergens Original Scent Lotion 400ml",     "ml",      36),
    ("Palmer's Cocoa Butter Formula 400ml",     "ml",      36),
    ("Cussons Baby Lotion 200ml",               "ml",      36),
    ("Johnson's Baby Oil 300ml",                "ml",      36),
    ("Shea Butter Raw Organic 500g",            "g",       24),
    ("Black Soap Dudu Osun 150g",               "g",       24),
    ("Sunsheen Hair Cream 500g",                "g",       24),
    ("Dark & Lovely Relaxer Kit",               "pieces",  24),
    ("ORS Olive Oil Replenishing Conditioner",  "ml",      36),
    ("Cantu Shea Butter Leave-In Cream 453g",   "g",       36),
    ("Pantene Pro-V Shampoo 400ml",             "ml",      36),
    ("Head & Shoulders Classic Clean 400ml",    "ml",      36),
    ("TRESemmé Keratin Smooth Shampoo 400ml",   "ml",      36),
    ("Luster's Pink Scalp Oil 236ml",           "ml",      36),
    ("African Pride Olive Miracle Oil 237ml",   "ml",      36),
    ("Oral-B Toothpaste 75ml",                  "ml",      24),
    ("Colgate Total Toothpaste 75ml",           "ml",      24),
    ("Close-Up Toothpaste 75ml",                "ml",      24),
    ("Macleans Whitening Toothpaste 75ml",      "ml",      24),
    ("Listerine Mouthwash 500ml",               "ml",      24),
    ("Sure Anti-Perspirant Deodorant 150ml",    "ml",      36),
    ("Dove Deodorant Roll-On 50ml",             "ml",      36),
    ("Rexona Men Sport Deodorant 150ml",        "ml",      36),
    ("Gillette Shaving Gel 200ml",              "ml",      36),
    ("Lux Shower Gel 250ml",                    "ml",      36),
    ("Pears Body Wash 250ml",                   "ml",      36),
    ("Revlon Lipstick Fire Red",                "pieces",  24),
    ("Maybelline Foundation Fit Me",            "pieces",  24),
    ("MAC Studio Fix Powder",                   "pieces",  24),
    ("Neutrogena Sunscreen SPF 50 88ml",        "ml",      24),
    ("Bioderma Micellar Water 250ml",           "ml",      24),
    ("Cetaphil Gentle Skin Cleanser 500ml",     "ml",      36),
    ("CeraVe Moisturizing Cream 340g",          "g",       36),
    ("Eucerin Daily Protection SPF 30 75ml",    "ml",      30),
    ("Fade Out Advanced Brightening Cream",     "g",       24),
    ("Ponds Cream Moisturiser 150ml",           "ml",      36),
    ("Olay Regenerist Serum 50ml",              "ml",      24),
    ("Garnier Vitamin C Serum 30ml",            "ml",      18),
    ("L'Oreal Paris Revitalift Serum 30ml",     "ml",      18),
    ("Himalaya Neem Face Wash 150ml",           "ml",      24),
]

DAIRY_PRODUCTS = [
    ("Peak Full Cream Milk 500ml",              "ml",       1),  # ~30 days shelf life
    ("Dano Cool Cow Pasteurized Milk 500ml",    "ml",       1),
    ("Hollandia Full Cream Milk 1L",            "litres",   1),
    ("So Fresh Yoghurt 200ml",                  "ml",       0),  # very short shelf life
    ("Chivita Dairy Yoghurt Vanilla 500ml",     "ml",       0),
    ("Nestle Yoghurt Strawberry 500ml",         "ml",       0),
    ("Cheddar Cheese Kerrygold 200g",           "g",        3),
    ("Mozzarella Cheese Grande 1kg",            "kg",       1),
    ("Butter Lurpak Unsalted 250g",             "g",        3),
    ("Margarine Blue Band 500g",                "g",        6),
    ("Eggs Farm Fresh Large x12",               "pieces",   0),  # 30 days
    ("Greek Yoghurt Total 0% 500g",             "g",        1),
    ("Soured Cream Tesco 300ml",                "ml",       1),
    ("Whipping Cream Elle & Vire 200ml",        "ml",       1),
    ("UHT Milk Almarai 1L",                     "litres",  12),
    ("Condensed Milk Nestlé 397g",              "pieces",  24),
    ("Powdered Milk Friesland 400g",            "pieces",  18),
]

HOUSEHOLD_PRODUCTS = [
    ("Dettol All-In-One Disinfectant 500ml",    "ml",      36),
    ("Harpic Toilet Cleaner 500ml",             "ml",      36),
    ("Vim Dishwashing Liquid 500ml",            "ml",      36),
    ("Ariel Detergent Powder 1kg",              "kg",      36),
    ("Omo Multiactive Detergent 1kg",           "kg",      36),
    ("Sunlight Dishwashing Liquid 500ml",       "ml",      36),
    ("Izal Disinfectant 1L",                    "litres",  36),
    ("Jik Bleach Original 750ml",               "ml",      24),
    ("Flash All-Purpose Spray 500ml",           "ml",      36),
    ("Mortein Mosquito Coil",                   "pieces",  36),
    ("Baygon Insecticide Spray 400ml",          "ml",      36),
    ("Rambo Rodenticide Poison 100g",           "g",       36),
    ("Air Freshener Glade 300ml",               "ml",      36),
    ("Toilet Paper Anosike x9",                 "packs",   36),
    ("Dishwashing Soap Bar Ajax 1kg",           "kg",      36),
    ("Fabric Softener Comfort Blue 500ml",      "ml",      36),
    ("Stain Remover Vanish Oxi Action 500g",    "g",       24),
    ("Glass Cleaner Mr Muscle 500ml",           "ml",      36),
    ("Mold Remover HG 500ml",                   "ml",      36),
    ("Cockroach Chalk Golden Cat",              "pieces",  24),
]

MEDICAL_SUPPLIES = [
    ("Surgical Gloves Latex Size M x100",       "pieces",  60),
    ("Surgical Gloves Latex Size L x100",       "pieces",  60),
    ("Nitrile Gloves Blue Size M x100",         "pieces",  60),
    ("Face Mask Surgical 3-Ply x50",            "packs",   36),
    ("N95 Respirator Mask x10",                 "packs",   60),
    ("Syringe 2ml Disposable x100",             "pieces",  60),
    ("Syringe 5ml Disposable x100",             "pieces",  60),
    ("Syringe 10ml Disposable x100",            "pieces",  60),
    ("IV Cannula 18G x50",                      "pieces",  60),
    ("IV Cannula 22G x50",                      "pieces",  60),
    ("Urinary Catheter Foley 14Fr x10",         "pieces",  60),
    ("Nasogastric Tube 14Fr x10",               "pieces",  60),
    ("Blood Glucose Test Strip x50",            "pieces",  24),
    ("Lancets for Glucometer x100",             "pieces",  36),
    ("Urine Dipstick 10-Parameter x100",        "pieces",  24),
    ("Malaria RDT Test Kit x25",                "pieces",  24),
    ("Pregnancy Test Strip x50",                "pieces",  24),
    ("HIV Rapid Test Determine x25",            "pieces",  24),
    ("Hepatitis B RDT x25",                     "pieces",  24),
    ("Wound Dressing Non-Stick 10x10 x10",      "packs",   60),
    ("Gauze Bandage 10cm x50",                  "pieces",  60),
    ("Plaster Elastic Bandage 10cm",            "pieces",  60),
    ("Cotton Wool Absorbent 500g",              "g",       60),
    ("Micropore Tape 1inch x10",                "pieces",  60),
    ("Hydrogen Peroxide 3% 500ml",              "ml",      24),
    ("Methylated Spirit 500ml",                 "ml",      36),
    ("Povidone Iodine Solution 500ml",          "ml",      24),
    ("Tongue Depressors Wooden x100",           "pieces",  60),
    ("Specimen Container 60ml x50",             "pieces",  60),
    ("Cord Clamp Disposable x50",               "pieces",  60),
    ("Suction Catheter 14Fr x10",               "pieces",  60),
    ("Sterile Water for Injection 10ml x10",    "pieces",  36),
    ("Absorbable Suture Vicryl 2-0 x12",        "pieces",  36),
    ("Non-Absorbable Suture Silk 2-0 x12",      "pieces",  36),
    ("Thermometer Digital",                     "pieces",  60),
    ("Pulse Oximeter Finger",                   "pieces",  36),
    ("Stethoscope Littmann Classic",            "pieces",  120),
    ("Blood Pressure Cuff Adult",               "pieces",  60),
    ("Nebulizer Mask Adult x10",                "pieces",  36),
    ("Oxygen Nasal Cannula Adult x10",          "pieces",  60),
]

BABY_PRODUCTS = [
    ("Nestle Nan Optipro 1 Infant Formula 400g","pieces",  24),
    ("Similac Advance Stage 1 900g",            "pieces",  24),
    ("Enfamil Premium Stage 1 900g",            "pieces",  24),
    ("Aptamil Follow On Stage 2 900g",          "pieces",  24),
    ("SMA Gold Stage 1 900g",                   "pieces",  24),
    ("Cerelac Wheat 250g",                      "pieces",  24),
    ("Cerelac Rice 250g",                       "pieces",  24),
    ("Heinz Vegetable Baby Food 120g",          "pieces",  24),
    ("Gerber Mixed Fruit Puree 120g",           "pieces",  18),
    ("Earth's Best Organic Baby Food 113g",     "pieces",  24),
    ("Pampers Active Baby Diapers S3 x44",      "pieces",  36),
    ("Huggies Gold Diapers S4 x40",             "pieces",  36),
    ("Molfix Baby Diapers S5 x36",              "pieces",  36),
    ("Baby Love Wipes 80 Sheets",               "pieces",  36),
    ("Cussons Baby Shampoo 200ml",              "ml",      36),
    ("Johnson's Baby Powder 200g",              "g",       36),
    ("Vaseline Baby Lotion 400ml",              "ml",      36),
    ("Dettol Baby Soap 75g",                    "g",       36),
    ("Luvs Baby Wipes 64 Sheets",               "pieces",  36),
    ("Gripe Water Woodward's 150ml",            "ml",      36),
    ("Calpol Infant Suspension 100ml",          "ml",      24),
    ("Dentinox Infant Colic Drops 100ml",       "ml",      24),
    ("Infacol Wind Drops 50ml",                 "ml",      24),
    ("Baby Vicks VapoRub 50ml",                 "ml",      36),
    ("Infant Vitamin D3 Drops 50ml",            "ml",      24),
]

HERBAL_PRODUCTS = [
    ("Forever Living Aloe Vera Gel 1L",         "litres",  24),
    ("Nature's Way Vitamin C 1000mg x100",      "pieces",  24),
    ("Holland & Barrett Vitamin D3 x60",        "pieces",  24),
    ("Pharmaton Vitality Capsules x30",         "pieces",  24),
    ("Seven Seas Cod Liver Oil 100ml",          "ml",      24),
    ("Omega-3 Fish Oil 1000mg x60",             "pieces",  24),
    ("Centrum Multivitamin Adults x30",         "pieces",  24),
    ("Calcium + Vitamin D3 Tablets x60",        "pieces",  36),
    ("Zinc 50mg Tablets x100",                  "pieces",  36),
    ("Iron Supplement Ferrous Fumarate x30",    "pieces",  36),
    ("Folic Acid 400mcg x90",                   "pieces",  36),
    ("Biotin 5000mcg x60",                      "pieces",  36),
    ("Magnesium 375mg x60",                     "pieces",  36),
    ("Glucosamine & Chondroitin x60",           "pieces",  36),
    ("Ginger Root Extract 500mg x60",           "pieces",  36),
    ("Turmeric Curcumin 500mg x60",             "pieces",  36),
    ("Black Seed Oil 500mg x60",                "pieces",  24),
    ("Moringa Leaf Powder 400g",                "g",       12),
    ("Spirulina Powder 200g",                   "g",       24),
    ("Ashwagandha Root 500mg x60",              "pieces",  36),
    ("Echinacea Immune Support x30",            "pieces",  24),
    ("Garlic Extract 1000mg x60",               "pieces",  36),
    ("Evening Primrose Oil 500mg x60",          "pieces",  24),
    ("St. John's Wort Extract x60",             "pieces",  36),
    ("Valerian Root Sleep Aid x30",             "pieces",  24),
    ("Melatonin 5mg Tablets x30",               "pieces",  36),
    ("Probiotics 10 Billion CFU x30",           "pieces",  12),
    ("Apple Cider Vinegar 500ml",               "ml",      36),
    ("Noni Juice Morinda 1L",                   "litres",  24),
    ("Shilajit Resin 30g",                      "g",       36),
    ("Royal Jelly 1000mg x30",                  "pieces",  24),
    ("Aloe Vera Juice 500ml",                   "ml",      12),
    ("Soursop Leaf Tea x20 bags",               "pieces",  18),
    ("Zobo Hibiscus Extract 200g",              "g",       12),
    ("Moringa Tea x20 bags",                    "pieces",  18),
    ("Bitter Leaf Extract Capsules x60",        "pieces",  24),
    ("Scent Leaf (Efirin) Oil 50ml",            "ml",      18),
    ("Neem Leaf Extract 500mg x60",             "pieces",  24),
    ("Dandelion Root Tea x20 bags",             "pieces",  18),
    ("Green Tea Extract 400mg x60",             "pieces",  24),
]

# ─────────────────────────────────────────────────────────────────────────────
# Build master product list with (category_name, name, unit, shelf_months)
# ─────────────────────────────────────────────────────────────────────────────
ALL_PRODUCTS = (
    [("Pharmaceuticals",      p[0], p[1], p[2]) for p in PHARMA_PRODUCTS] +
    [("Food & Beverages",     p[0], p[1], p[2]) for p in FOOD_PRODUCTS] +
    [("Cosmetics & Beauty",   p[0], p[1], p[2]) for p in COSMETICS_PRODUCTS] +
    [("Dairy & Perishables",  p[0], p[1], p[2]) for p in DAIRY_PRODUCTS] +
    [("Household Chemicals",  p[0], p[1], p[2]) for p in HOUSEHOLD_PRODUCTS] +
    [("Medical Supplies",     p[0], p[1], p[2]) for p in MEDICAL_SUPPLIES] +
    [("Baby Products",        p[0], p[1], p[2]) for p in BABY_PRODUCTS] +
    [("Herbal & Supplements", p[0], p[1], p[2]) for p in HERBAL_PRODUCTS]
)


def make_expiry_dates():
    """
    Returns a list of 1000 expiry days_offset from today, carefully distributed:
      - 120 already expired  (days < 0)
      -  40 expiring today   (day = 0)
      -  50 in 1-7 days      (CRITICAL)
      -  80 in 8-14 days     (WARNING)
      - 150 in 15-30 days    (NEAR EXPIRY)
      - 560 in 31-730 days   (SAFE)
    """
    dates = []

    # 120 expired — spread from -1 to -730 days ago
    expired_ranges = (
        list(range(-1, -8, -1)) * 5 +     # 1-7 days expired (most common, urgent)
        list(range(-8, -31, -1)) +         # 8-30 days expired
        list(range(-31, -181, -2)) +       # 31-180 days expired
        list(range(-181, -731, -7))        # 181-730 days expired (old stock)
    )
    dates += random.choices(expired_ranges, k=120)

    # 40 expiring today
    dates += [0] * 40

    # 50 in 1-7 days (CRITICAL)
    dates += [random.randint(1, 7) for _ in range(50)]

    # 80 in 8-14 days (WARNING)
    dates += [random.randint(8, 14) for _ in range(80)]

    # 150 in 15-30 days (NEAR EXPIRY)
    dates += [random.randint(15, 30) for _ in range(150)]

    # 560 in 31-730 days (SAFE)
    safe_days = (
        [random.randint(31, 60) for _ in range(80)] +
        [random.randint(61, 90) for _ in range(80)] +
        [random.randint(91, 180) for _ in range(120)] +
        [random.randint(181, 365) for _ in range(180)] +
        [random.randint(366, 730) for _ in range(100)]
    )
    dates += safe_days

    random.shuffle(dates)
    return dates[:1000]


def run():
    print("\n" + "="*65)
    print("  PRODUCTS EXPIRY ALERT MANAGEMENT SYSTEM — Test Data Seeder")
    print("="*65)

    # ── 1. Categories ──────────────────────────────────────────────────────
    print("\n[1/5] Creating categories...")
    cat_map = {}
    for name, desc in CATEGORIES:
        obj, created = Category.objects.get_or_create(name=name, defaults={"description": desc})
        cat_map[name] = obj
        print(f"      {'✚ Created' if created else '✓ Exists '} → {name}")

    # ── 2. Alert Configurations ────────────────────────────────────────────
    print("\n[2/5] Creating alert threshold configurations...")
    thresholds = [
        (30, "INFO"),
        (14, "WARNING"),
        (7,  "CRITICAL"),
    ]
    for days, level in thresholds:
        obj, created = AlertConfiguration.objects.get_or_create(
            threshold_days=days,
            defaults={"alert_level": level, "is_active": True}
        )
        print(f"      {'✚ Created' if created else '✓ Exists '} → {level} alert at {days} days before expiry")

    # ── 3. Test Users ──────────────────────────────────────────────────────
    print("\n[3/5] Creating test user accounts...")
    test_users = [
        ("admin",    "admin@expiryalert.com",    "Admin@1234",    "ADMIN",   True),
        ("manager1", "manager@expiryalert.com",  "Manager@1234",  "MANAGER", True),
        ("staff1",   "staff1@expiryalert.com",   "Staff@1234",    "STAFF",   True),
        ("staff2",   "staff2@expiryalert.com",   "Staff@1234",    "STAFF",   True),
        ("auditor",  "auditor@expiryalert.com",  "Auditor@1234",  "STAFF",   False),
    ]
    user_objs = []
    for uname, email, pwd, role, is_super in test_users:
        if User.objects.filter(username=uname).exists():
            u = User.objects.get(username=uname)
            print(f"      ✓ Exists  → {uname} ({role})")
        else:
            if is_super and role == "ADMIN":
                u = User.objects.create_superuser(uname, email, pwd)
            else:
                u = User.objects.create_user(uname, email, pwd)
            UserProfile.objects.update_or_create(
                user=u,
                defaults={"role": role, "receive_email_alerts": True}
            )
            print(f"      ✚ Created → {uname} ({role}) | password: {pwd}")
        user_objs.append(u)

    # ── 4. Products ────────────────────────────────────────────────────────
    print("\n[4/5] Seeding 1000 test products...")
    print("      (This may take 10-30 seconds...)\n")

    # Clear existing non-essential products to avoid duplicates on re-run
    existing_count = Product.objects.count()
    if existing_count > 10:
        confirm = input(f"      ⚠ Found {existing_count} existing products. Clear them and reseed? [y/N]: ").strip().lower()
        if confirm == 'y':
            Product.objects.all().delete()
            NotificationLog.objects.all().delete()
            print("      ✓ Cleared existing products.\n")
        else:
            print("      ✓ Keeping existing products. Adding new ones...\n")

    expiry_offsets = make_expiry_dates()
    products_to_create = []
    admin_user = User.objects.filter(username='admin').first() or user_objs[0]

    counts = {"expired": 0, "today": 0, "critical": 0, "warning": 0, "near_expiry": 0, "safe": 0}

    for i, offset in enumerate(expiry_offsets):
        # Pick a product template (cycle through all, then repeat)
        template = ALL_PRODUCTS[i % len(ALL_PRODUCTS)]
        cat_name, prod_name, unit, shelf_months = template

        # If shelf_months == 0, it's ultra-perishable (3-day life)
        actual_shelf = 3 if shelf_months == 0 else shelf_months * 30

        expiry = days_from_today(offset)
        mfg = expiry - timedelta(days=actual_shelf)

        sku = rand_sku(cat_name[:3].upper(), i + 1)
        batch = rand_batch()
        qty = random.choice([10, 20, 25, 30, 50, 60, 100, 120, 150, 200, 250, 300, 500])
        supplier = pick(SUPPLIERS)
        added_by = pick(user_objs)

        # Vary product name slightly for uniqueness
        suffixes = ["", " (Import)", " (Local)", " — Batch A", " — Batch B", " (Restock)", " (Emergency Stock)"]
        display_name = prod_name + (pick(suffixes) if i % 7 == 0 else "")

        products_to_create.append(Product(
            product_name=display_name,
            category=cat_map[cat_name],
            sku=sku,
            batch_number=batch,
            quantity=qty,
            unit=unit,
            manufacture_date=mfg,
            expiry_date=expiry,
            supplier_name=supplier,
            description=f"Test product {i+1} — {cat_name}. Seeded by test script.",
            added_by=admin_user,
            is_active=True,
        ))

        # Count by status
        if offset < 0:     counts["expired"] += 1
        elif offset == 0:  counts["today"] += 1
        elif offset <= 7:  counts["critical"] += 1
        elif offset <= 14: counts["warning"] += 1
        elif offset <= 30: counts["near_expiry"] += 1
        else:              counts["safe"] += 1

        # Progress indicator
        if (i + 1) % 100 == 0:
            print(f"      ► {i+1}/1000 products prepared...")

    Product.objects.bulk_create(products_to_create, ignore_conflicts=True)

    # ── 5. Summary ─────────────────────────────────────────────────────────
    total = Product.objects.count()
    print(f"\n[5/5] Done! Summary:\n")
    print(f"  ✅  Total products in database : {total}")
    print(f"  🚫  Expired (past date)        : {counts['expired']}")
    print(f"  🟥  Expiring today             : {counts['today']}")
    print(f"  🔴  Critical (1–7 days)        : {counts['critical']}")
    print(f"  🟡  Warning  (8–14 days)       : {counts['warning']}")
    print(f"  🔵  Near Expiry (15–30 days)   : {counts['near_expiry']}")
    print(f"  ✅  Safe (31+ days)            : {counts['safe']}")
    print(f"\n  📋  Categories: {Category.objects.count()}")
    print(f"  👤  Users:      {User.objects.count()}")
    print(f"  🔔  Alert configs: {AlertConfiguration.objects.count()}")
    print(f"\n{'='*65}")
    print(f"  🚀  Login at http://localhost:5173")
    print(f"  👤  Username: admin   Password: Admin@1234")
    print(f"{'='*65}\n")


if __name__ == "__main__":
    run()
