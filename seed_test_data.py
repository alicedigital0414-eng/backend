import os
import django
from datetime import datetime, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from products.models import Product, Category

User = get_user_model()

today = datetime.now().date()

# Define Categories
CATEGORIES = [
    {'name': 'Prescription Drugs', 'description': 'Prescription medications and pharmaceuticals'},
    {'name': 'Over-the-Counter Drugs', 'description': 'OTC medications and remedies'},
    {'name': 'Antibiotics', 'description': 'Antibiotic medications'},
    {'name': 'Pain Relief', 'description': 'Analgesics and pain management'},
    {'name': 'Vitamins & Supplements', 'description': 'Dietary supplements and vitamins'},
    {'name': 'Herbal & Natural Remedies', 'description': 'Herbal supplements and natural medicines'},
    {'name': 'Medical Supplies', 'description': 'Medical equipment and supplies'},
    {'name': 'First Aid', 'description': 'First aid kits and supplies'},
    {'name': 'Baby & Child Health', 'description': 'Pediatric health products'},
    {'name': 'Frozen Foods', 'description': 'Frozen meals, vegetables, and meats'},
    {'name': 'Dairy Products', 'description': 'Milk, cheese, yogurt and dairy items'},
    {'name': 'Beverages', 'description': 'Drinks and refreshments'},
    {'name': 'Canned Goods', 'description': 'Canned vegetables, soups, and preserved foods'},
    {'name': 'Snacks & Chips', 'description': 'Snack foods and chips'},
    {'name': 'Breakfast Cereals', 'description': 'Cereals and breakfast items'},
    {'name': 'Pasta & Noodles', 'description': 'Pasta, noodles, and grain products'},
    {'name': 'Sauces & Condiments', 'description': 'Sauces, dressings, and condiments'},
    {'name': 'Baking Supplies', 'description': 'Flour, sugar, baking ingredients'},
    {'name': 'Cosmetics & Beauty', 'description': 'Skincare, makeup, and beauty products'},
    {'name': 'Hair Care', 'description': 'Shampoos, conditioners, hair treatments'},
    {'name': 'Oral Care', 'description': 'Toothpaste, mouthwash, dental products'},
    {'name': 'Skin Care', 'description': 'Face creams, lotions, skin treatments'},
    {'name': 'Household Cleaning', 'description': 'Cleaning supplies and detergents'},
    {'name': 'Pet Supplies', 'description': 'Pet food and pet care products'},
]

def generate_drug_products():
    """Generate pharmaceutical and drug products"""
    drugs = [
        # Prescription Drugs
        {'name': 'Amoxicillin 500mg', 'sku': 'RX-AMX-001', 'batch': 'BATCH-AMX-001', 'supplier': 'PharmaCorp Ltd'},
        {'name': 'Ciprofloxacin 500mg', 'sku': 'RX-CIP-002', 'batch': 'BATCH-CIP-002', 'supplier': 'MediPharm Inc'},
        {'name': 'Metformin 850mg', 'sku': 'RX-MET-003', 'batch': 'BATCH-MET-003', 'supplier': 'HealthCare Plus'},
        {'name': 'Lisinopril 10mg', 'sku': 'RX-LIS-004', 'batch': 'BATCH-LIS-004', 'supplier': 'CardioMed Ltd'},
        {'name': 'Omeprazole 20mg', 'sku': 'RX-OME-005', 'batch': 'BATCH-OME-005', 'supplier': 'GastroHealth'},
        {'name': 'Sertraline 50mg', 'sku': 'RX-SER-006', 'batch': 'BATCH-SER-006', 'supplier': 'NeuroPharm'},
        {'name': 'Atorvastatin 20mg', 'sku': 'RX-ATO-007', 'batch': 'BATCH-ATO-007', 'supplier': 'CardioMed Ltd'},
        {'name': 'Levothyroxine 100mcg', 'sku': 'RX-LEV-008', 'batch': 'BATCH-LEV-008', 'supplier': 'ThyroidCare'},
        {'name': 'Losartan 50mg', 'sku': 'RX-LOS-009', 'batch': 'BATCH-LOS-009', 'supplier': 'CardioMed Ltd'},
        {'name': 'Gabapentin 300mg', 'sku': 'RX-GAB-010', 'batch': 'BATCH-GAB-010', 'supplier': 'NeuroPharm'},
        {'name': 'Alprazolam 0.5mg', 'sku': 'RX-ALP-011', 'batch': 'BATCH-ALP-011', 'supplier': 'AnxietyCare'},
        {'name': 'Prednisone 20mg', 'sku': 'RX-PRE-012', 'batch': 'BATCH-PRE-012', 'supplier': 'ImmunoPharm'},
        {'name': 'Tramadol 50mg', 'sku': 'RX-TRA-013', 'batch': 'BATCH-TRA-013', 'supplier': 'PainRelief Inc'},
        {'name': 'Clonazepam 2mg', 'sku': 'RX-CLO-014', 'batch': 'BATCH-CLO-014', 'supplier': 'NeuroPharm'},
        {'name': 'Metoprolol 25mg', 'sku': 'RX-MET-015', 'batch': 'BATCH-MET-015', 'supplier': 'CardioMed Ltd'},
        {'name': 'Pantoprazole 40mg', 'sku': 'RX-PAN-016', 'batch': 'BATCH-PAN-016', 'supplier': 'GastroHealth'},
        {'name': 'Fluoxetine 20mg', 'sku': 'RX-FLU-017', 'batch': 'BATCH-FLU-017', 'supplier': 'NeuroPharm'},
        {'name': 'Amlodipine 5mg', 'sku': 'RX-AML-018', 'batch': 'BATCH-AML-018', 'supplier': 'CardioMed Ltd'},
        {'name': 'Warfarin 5mg', 'sku': 'RX-WAR-019', 'batch': 'BATCH-WAR-019', 'supplier': 'BloodCare Ltd'},
        {'name': 'Diazepam 5mg', 'sku': 'RX-DIA-020', 'batch': 'BATCH-DIA-020', 'supplier': 'NeuroPharm'},
        
        # Over-the-Counter Drugs
        {'name': 'Ibuprofen 400mg', 'sku': 'OTC-IBU-021', 'batch': 'BATCH-IBU-021', 'supplier': 'PainRelief Inc'},
        {'name': 'Paracetamol 500mg', 'sku': 'OTC-PAR-022', 'batch': 'BATCH-PAR-022', 'supplier': 'FeverCare'},
        {'name': 'Aspirin 75mg', 'sku': 'OTC-ASP-023', 'batch': 'BATCH-ASP-023', 'supplier': 'HeartHealth'},
        {'name': 'Naproxen 250mg', 'sku': 'OTC-NAP-024', 'batch': 'BATCH-NAP-024', 'supplier': 'PainRelief Inc'},
        {'name': 'Cetirizine 10mg', 'sku': 'OTC-CET-025', 'batch': 'BATCH-CET-025', 'supplier': 'AllergyCare'},
        {'name': 'Loratadine 10mg', 'sku': 'OTC-LOR-026', 'batch': 'BATCH-LOR-026', 'supplier': 'AllergyCare'},
        {'name': 'Diphenhydramine 25mg', 'sku': 'OTC-DIP-027', 'batch': 'BATCH-DIP-027', 'supplier': 'SleepAid Inc'},
        {'name': 'Loperamide 2mg', 'sku': 'OTC-LOP-028', 'batch': 'BATCH-LOP-028', 'supplier': 'DigestiveCare'},
        {'name': 'Ranitidine 150mg', 'sku': 'OTC-RAN-029', 'batch': 'BATCH-RAN-029', 'supplier': 'GastroHealth'},
        {'name': 'Pseudoephedrine 60mg', 'sku': 'OTC-PSE-030', 'batch': 'BATCH-PSE-030', 'supplier': 'Decongestant Inc'},
        
        # Antibiotics
        {'name': 'Azithromycin 250mg', 'sku': 'ABX-AZI-031', 'batch': 'BATCH-AZI-031', 'supplier': 'PharmaCorp Ltd'},
        {'name': 'Cephalexin 500mg', 'sku': 'ABX-CEP-032', 'batch': 'BATCH-CEP-032', 'supplier': 'MediPharm Inc'},
        {'name': 'Doxycycline 100mg', 'sku': 'ABX-DOX-033', 'batch': 'BATCH-DOX-033', 'supplier': 'PharmaCorp Ltd'},
        {'name': 'Clarithromycin 500mg', 'sku': 'ABX-CLA-034', 'batch': 'BATCH-CLA-034', 'supplier': 'HealthCare Plus'},
        {'name': 'Levofloxacin 500mg', 'sku': 'ABX-LEV-035', 'batch': 'BATCH-LEV-035', 'supplier': 'MediPharm Inc'},
        
        # Pain Relief
        {'name': 'Morphine 10mg', 'sku': 'PR-MOR-036', 'batch': 'BATCH-MOR-036', 'supplier': 'PainRelief Inc'},
        {'name': 'Codeine 30mg', 'sku': 'PR-COD-037', 'batch': 'BATCH-COD-037', 'supplier': 'PainRelief Inc'},
        {'name': 'Oxycodone 5mg', 'sku': 'PR-OXY-038', 'batch': 'BATCH-OXY-038', 'supplier': 'PainRelief Inc'},
        {'name': 'Hydrocodone 5mg', 'sku': 'PR-HYD-039', 'batch': 'BATCH-HYD-039', 'supplier': 'PainRelief Inc'},
        {'name': 'Fentanyl Patch 25mcg', 'sku': 'PR-FEN-040', 'batch': 'BATCH-FEN-040', 'supplier': 'PainRelief Inc'},
    ]
    return drugs

def generate_supplement_products():
    """Generate vitamin and supplement products"""
    supplements = [
        # Vitamins & Supplements
        {'name': 'Vitamin C 1000mg', 'sku': 'VIT-C-041', 'batch': 'BATCH-VTC-041', 'supplier': 'NutriHealth Ltd'},
        {'name': 'Vitamin D3 5000IU', 'sku': 'VIT-D3-042', 'batch': 'BATCH-VTD-042', 'supplier': 'SunshineVitamins'},
        {'name': 'Vitamin B12 1000mcg', 'sku': 'VIT-B12-043', 'batch': 'BATCH-VTB-043', 'supplier': 'EnergyPlus'},
        {'name': 'Vitamin E 400IU', 'sku': 'VIT-E-044', 'batch': 'BATCH-VTE-044', 'supplier': 'SkinHealth'},
        {'name': 'Vitamin A 10000IU', 'sku': 'VIT-A-045', 'batch': 'BATCH-VTA-045', 'supplier': 'VisionCare'},
        {'name': 'Zinc 50mg', 'sku': 'SUP-ZNC-046', 'batch': 'BATCH-ZNC-046', 'supplier': 'ImmuneBoost'},
        {'name': 'Magnesium 400mg', 'sku': 'SUP-MAG-047', 'batch': 'BATCH-MAG-047', 'supplier': 'BoneHealth'},
        {'name': 'Calcium 600mg', 'sku': 'SUP-CAL-048', 'batch': 'BATCH-CAL-048', 'supplier': 'BoneHealth'},
        {'name': 'Iron 65mg', 'sku': 'SUP-IRN-049', 'batch': 'BATCH-IRN-049', 'supplier': 'EnergyPlus'},
        {'name': 'Omega-3 1000mg', 'sku': 'SUP-OMG-050', 'batch': 'BATCH-OMG-050', 'supplier': 'HeartHealth'},
        {'name': 'Multivitamin Complete', 'sku': 'SUP-MVI-051', 'batch': 'BATCH-MVI-051', 'supplier': 'NutriHealth Ltd'},
        {'name': 'Probiotic 50B', 'sku': 'SUP-PRB-052', 'batch': 'BATCH-PRB-052', 'supplier': 'DigestiveCare'},
        {'name': 'Glucosamine 1500mg', 'sku': 'SUP-GLU-053', 'batch': 'BATCH-GLU-053', 'supplier': 'JointCare'},
        {'name': 'Coenzyme Q10 200mg', 'sku': 'SUP-COQ-054', 'batch': 'BATCH-COQ-054', 'supplier': 'HeartHealth'},
        {'name': 'Melatonin 5mg', 'sku': 'SUP-MEL-055', 'batch': 'BATCH-MEL-055', 'supplier': 'SleepAid Inc'},
        
        # Herbal & Natural Remedies
        {'name': 'Echinacea 400mg', 'sku': 'HER-ECH-056', 'batch': 'BATCH-ECH-056', 'supplier': 'HerbalLife'},
        {'name': 'Ginseng 500mg', 'sku': 'HER-GIN-057', 'batch': 'BATCH-GIN-057', 'supplier': 'HerbalLife'},
        {'name': 'Ginkgo Biloba 120mg', 'sku': 'HER-GNK-058', 'batch': 'BATCH-GNK-058', 'supplier': 'BrainBoost'},
        {'name': 'St Johns Wort 300mg', 'sku': 'HER-STJ-059', 'batch': 'BATCH-STJ-059', 'supplier': 'MoodBalance'},
        {'name': 'Valerian Root 500mg', 'sku': 'HER-VAL-060', 'batch': 'BATCH-VAL-060', 'supplier': 'SleepAid Inc'},
        {'name': 'Turmeric 1000mg', 'sku': 'HER-TUR-061', 'batch': 'BATCH-TUR-061', 'supplier': 'AntiInflammatory'},
        {'name': 'Garlic 500mg', 'sku': 'HER-GAR-062', 'batch': 'BATCH-GAR-062', 'supplier': 'HeartHealth'},
        {'name': 'Ashwagandha 600mg', 'sku': 'HER-ASH-063', 'batch': 'BATCH-ASH-063', 'supplier': 'StressRelief'},
        {'name': 'CBD Oil 500mg', 'sku': 'HER-CBD-064', 'batch': 'BATCH-CBD-064', 'supplier': 'NaturalRemedies'},
        {'name': 'Collagen Peptides', 'sku': 'SUP-CLG-065', 'batch': 'BATCH-CLG-065', 'supplier': 'SkinHealth'},
        
        # Medical Supplies
        {'name': 'Blood Glucose Monitor', 'sku': 'MED-BGM-066', 'batch': 'BATCH-BGM-066', 'supplier': 'DiabetesCare'},
        {'name': 'Blood Pressure Monitor', 'sku': 'MED-BPM-067', 'batch': 'BATCH-BPM-067', 'supplier': 'CardioMed Ltd'},
        {'name': 'Nebulizer Machine', 'sku': 'MED-NEB-068', 'batch': 'BATCH-NEB-068', 'supplier': 'RespiratoryCare'},
        {'name': 'Pulse Oximeter', 'sku': 'MED-POX-069', 'batch': 'BATCH-POX-069', 'supplier': 'VitalMonitor'},
        {'name': 'Medical Thermometer', 'sku': 'MED-THM-070', 'batch': 'BATCH-THM-070', 'supplier': 'FeverCare'},
        {'name': 'Insulin Syringes', 'sku': 'MED-INS-071', 'batch': 'BATCH-INS-071', 'supplier': 'DiabetesCare'},
        {'name': 'Lancets 100ct', 'sku': 'MED-LAN-072', 'batch': 'BATCH-LAN-072', 'supplier': 'DiabetesCare'},
        {'name': 'Surgical Masks 50ct', 'sku': 'MED-MSK-073', 'batch': 'BATCH-MSK-073', 'supplier': 'SafetyFirst'},
        {'name': 'Nitrile Gloves 100ct', 'sku': 'MED-GLO-074', 'batch': 'BATCH-GLO-074', 'supplier': 'SafetyFirst'},
        {'name': 'Wound Dressing Kit', 'sku': 'MED-WND-075', 'batch': 'BATCH-WND-075', 'supplier': 'FirstAidPro'},
        
        # First Aid
        {'name': 'First Aid Kit Deluxe', 'sku': 'FAC-DLX-076', 'batch': 'BATCH-DLX-076', 'supplier': 'FirstAidPro'},
        {'name': 'Bandage Assortment', 'sku': 'FAC-BND-077', 'batch': 'BATCH-BND-077', 'supplier': 'FirstAidPro'},
        {'name': 'Antiseptic Wipes', 'sku': 'FAC-ANT-078', 'batch': 'BATCH-ANT-078', 'supplier': 'SafetyFirst'},
        {'name': 'Hydrogen Peroxide', 'sku': 'FAC-HYP-079', 'batch': 'BATCH-HYP-079', 'supplier': 'FirstAidPro'},
        {'name': 'Burn Cream 30g', 'sku': 'FAC-BRN-080', 'batch': 'BATCH-BRN-080', 'supplier': 'BurnCare'},
        
        # Baby & Child Health
        {'name': 'Baby Multivitamin Drops', 'sku': 'BAB-VIT-081', 'batch': 'BATCH-BVT-081', 'supplier': 'BabyHealth'},
        {'name': 'Baby Paracetamol', 'sku': 'BAB-PAR-082', 'batch': 'BATCH-BPA-082', 'supplier': 'BabyHealth'},
        {'name': 'Baby Teething Gel', 'sku': 'BAB-TTH-083', 'batch': 'BATCH-BTT-083', 'supplier': 'DentalCare'},
        {'name': 'Childrens Vitamin C', 'sku': 'BAB-VTC-084', 'batch': 'BATCH-BVC-084', 'supplier': 'ImmunityKids'},
        {'name': 'Calcium Kids Gummies', 'sku': 'BAB-CAL-085', 'batch': 'BATCH-BCL-085', 'supplier': 'KidHealth'},
    ]
    return supplements

def generate_food_products():
    """Generate food products"""
    foods = [
        # Frozen Foods
        {'name': 'Frozen Mixed Vegetables 1kg', 'sku': 'FRZ-VEG-086', 'batch': 'BATCH-FVEG-086', 'supplier': 'FreshFrozen'},
        {'name': 'Frozen Chicken Breast 2kg', 'sku': 'FRZ-CHK-087', 'batch': 'BATCH-FCHK-087', 'supplier': 'QualityMeats'},
        {'name': 'Frozen Fish Fillet 500g', 'sku': 'FRZ-FSH-088', 'batch': 'BATCH-FFSH-088', 'supplier': 'SeafoodDirect'},
        {'name': 'Frozen Pizza Margherita', 'sku': 'FRZ-PIZ-089', 'batch': 'BATCH-FPIZ-089', 'supplier': 'PizzaLover'},
        {'name': 'Frozen French Fries 1kg', 'sku': 'FRZ-FRY-090', 'batch': 'BATCH-FFRY-090', 'supplier': 'PotatoFresh'},
        {'name': 'Frozen Ice Cream Vanilla 1L', 'sku': 'FRZ-ICE-091', 'batch': 'BATCH-FICE-091', 'supplier': 'SweetTreats'},
        {'name': 'Frozen Berries Mix 500g', 'sku': 'FRZ-BRY-092', 'batch': 'BATCH-FBRY-092', 'supplier': 'FruitFresh'},
        {'name': 'Frozen Spring Rolls 20ct', 'sku': 'FRZ-SPR-093', 'batch': 'BATCH-FSPR-093', 'supplier': 'AsianDelight'},
        
        # Dairy Products
        {'name': 'Fresh Milk 2L', 'sku': 'DRY-MLK-094', 'batch': 'BATCH-DMLK-094', 'supplier': 'DairyFarm'},
        {'name': 'Greek Yogurt 500g', 'sku': 'DRY-YOG-095', 'batch': 'BATCH-DYOG-095', 'supplier': 'DairyFarm'},
        {'name': 'Cheddar Cheese 250g', 'sku': 'DRY-CHS-096', 'batch': 'BATCH-DCHS-096', 'supplier': 'CheeseMaster'},
        {'name': 'Butter 500g', 'sku': 'DRY-BUT-097', 'batch': 'BATCH-DBUT-097', 'supplier': 'DairyFarm'},
        {'name': 'Cream Cheese 200g', 'sku': 'DRY-CRM-098', 'batch': 'BATCH-DCRM-098', 'supplier': 'CheeseMaster'},
        {'name': 'Parmesan Cheese 100g', 'sku': 'DRY-PRM-099', 'batch': 'BATCH-DPRM-099', 'supplier': 'CheeseMaster'},
        
        # Beverages
        {'name': 'Orange Juice 1L', 'sku': 'BEV-OJ-100', 'batch': 'BATCH-BOJ-100', 'supplier': 'JuicePress'},
        {'name': 'Apple Juice 1L', 'sku': 'BEV-AJ-101', 'batch': 'BATCH-BAJ-101', 'supplier': 'JuicePress'},
        {'name': 'Cola 2L', 'sku': 'BEV-COL-102', 'batch': 'BATCH-BCOL-102', 'supplier': 'FizzyDrinks'},
        {'name': 'Mineral Water 500ml', 'sku': 'BEV-WTR-103', 'batch': 'BATCH-BWTR-103', 'supplier': 'PureWater'},
        {'name': 'Coffee Beans 250g', 'sku': 'BEV-COF-104', 'batch': 'BATCH-BCOF-104', 'supplier': 'CoffeeRoast'},
        {'name': 'Green Tea 20ct', 'sku': 'BEV-TEA-105', 'batch': 'BATCH-BTEA-105', 'supplier': 'TeaHouse'},
        {'name': 'Energy Drink 500ml', 'sku': 'BEV-ENG-106', 'batch': 'BATCH-BENG-106', 'supplier': 'EnergyBoost'},
        {'name': 'Coconut Water 1L', 'sku': 'BEV-COC-107', 'batch': 'BATCH-BCOC-107', 'supplier': 'NaturalHydration'},
        
        # Canned Goods
        {'name': 'Baked Beans 400g', 'sku': 'CAN-BNS-108', 'batch': 'BATCH-CBNS-108', 'supplier': 'CanFoods'},
        {'name': 'Corn 340g', 'sku': 'CAN-CRN-109', 'batch': 'BATCH-CRRN-109', 'supplier': 'CanFoods'},
        {'name': 'Peas 340g', 'sku': 'CAN-PEA-110', 'batch': 'BATCH-CPEA-110', 'supplier': 'CanFoods'},
        {'name': 'Tuna 185g', 'sku': 'CAN-TUN-111', 'batch': 'BATCH-CTUN-111', 'supplier': 'SeafoodDirect'},
        {'name': 'Tomato Soup 400g', 'sku': 'CAN-SOU-112', 'batch': 'BATCH-CSOU-112', 'supplier': 'SoupKitchen'},
        {'name': 'Spaghetti 400g', 'sku': 'CAN-SPA-113', 'batch': 'BATCH-CSPA-113', 'supplier': 'PastaItalian'},
        {'name': 'Pineapple 432g', 'sku': 'CAN-PIN-114', 'batch': 'BATCH-CPIN-114', 'supplier': 'FruitFresh'},
        {'name': 'Mushroom Soup 400g', 'sku': 'CAN-MSH-115', 'batch': 'BATCH-CMSH-115', 'supplier': 'SoupKitchen'},
        
        # Snacks
        {'name': 'Potato Chips Classic 150g', 'sku': 'SNK-CHP-116', 'batch': 'BATCH-SCHP-116', 'supplier': 'SnackTime'},
        {'name': 'Cheese Puffs 100g', 'sku': 'SNK-CPU-117', 'batch': 'BATCH-SCPU-117', 'supplier': 'SnackTime'},
        {'name': 'Pretzel Sticks 200g', 'sku': 'SNK-PRT-118', 'batch': 'BATCH-SPRT-118', 'supplier': 'BakeryFresh'},
        {'name': 'Trail Mix 250g', 'sku': 'SNK-TRM-119', 'batch': 'BATCH-STRM-119', 'supplier': 'HealthySnacks'},
        {'name': 'Granola Bar 40g x6', 'sku': 'SNK-GRN-120', 'batch': 'BATCH-SGRN-120', 'supplier': 'HealthySnacks'},
        {'name': 'Popcorn 100g', 'sku': 'SNK-POP-121', 'batch': 'BATCH-SPOP-121', 'supplier': 'CinemaTreats'},
        
        # Breakfast Cereals
        {'name': 'Corn Flakes 500g', 'sku': 'BRK-CRN-122', 'batch': 'BATCH-BCRN-122', 'supplier': 'BreakfastKing'},
        {'name': 'Oats 1kg', 'sku': 'BRK-OAT-123', 'batch': 'BATCH-BOAT-123', 'supplier': 'HealthyGrains'},
        {'name': 'Muesli 750g', 'sku': 'BRK-MUS-124', 'batch': 'BATCH-BMUS-124', 'supplier': 'HealthyGrains'},
        {'name': 'Wheat Biscuits 450g', 'sku': 'BRK-WHT-125', 'batch': 'BATCH-BWHT-125', 'supplier': 'BreakfastKing'},
        
        # Pasta & Noodles
        {'name': 'Spaghetti 500g', 'sku': 'PST-SPA-126', 'batch': 'BATCH-PSPA-126', 'supplier': 'PastaItalian'},
        {'name': 'Macaroni 500g', 'sku': 'PST-MAC-127', 'batch': 'BATCH-PMAC-127', 'supplier': 'PastaItalian'},
        {'name': 'Instant Noodles 60g x5', 'sku': 'PST-NOD-128', 'batch': 'BATCH-PNOD-128', 'supplier': 'AsianDelight'},
        {'name': 'Brown Rice Pasta 400g', 'sku': 'PST-BRP-129', 'batch': 'BATCH-PBRP-129', 'supplier': 'HealthyGrains'},
        
        # Sauces & Condiments
        {'name': 'Ketchup 500ml', 'sku': 'SAU-KET-130', 'batch': 'BATCH-SKET-130', 'supplier': 'FlavorMaster'},
        {'name': 'Mayonnaise 500ml', 'sku': 'SAU-MAY-131', 'batch': 'BATCH-SMAY-131', 'supplier': 'FlavorMaster'},
        {'name': 'Soy Sauce 250ml', 'sku': 'SAU-SOY-132', 'batch': 'BATCH-SSOY-132', 'supplier': 'AsianDelight'},
        {'name': 'Olive Oil 500ml', 'sku': 'SAU-OLI-133', 'batch': 'BATCH-SOLI-133', 'supplier': 'Mediterranean'},
        {'name': 'Vinegar 500ml', 'sku': 'SAU-VIN-134', 'batch': 'BATCH-SVIN-134', 'supplier': 'FlavorMaster'},
    ]
    return foods

def generate_household_products():
    """Generate household and personal care products"""
    household = [
        # Baking Supplies
        {'name': 'All-Purpose Flour 2kg', 'sku': 'BAK-FLR-135', 'batch': 'BATCH-BFLR-135', 'supplier': 'BakingGoods'},
        {'name': 'White Sugar 2kg', 'sku': 'BAK-SUG-136', 'batch': 'BATCH-BSUG-136', 'supplier': 'BakingGoods'},
        {'name': 'Brown Sugar 1kg', 'sku': 'BAK-BSU-137', 'batch': 'BATCH-BBSU-137', 'supplier': 'BakingGoods'},
        {'name': 'Baking Powder 100g', 'sku': 'BAK-BPW-138', 'batch': 'BATCH-BBPW-138', 'supplier': 'BakingGoods'},
        {'name': 'Cocoa Powder 250g', 'sku': 'BAK-COC-139', 'batch': 'BATCH-BCOC-139', 'supplier': 'BakingGoods'},
        
        # Cosmetics & Beauty
        {'name': 'Foundation 30ml', 'sku': 'COS-FND-140', 'batch': 'BATCH-CFND-140', 'supplier': 'BeautyPro'},
        {'name': 'Concealer 15ml', 'sku': 'COS-CNC-141', 'batch': 'BATCH-CCNC-141', 'supplier': 'BeautyPro'},
        {'name': 'Lipstick Red', 'sku': 'COS-LIP-142', 'batch': 'BATCH-CLIP-142', 'supplier': 'ColorCosmetics'},
        {'name': 'Mascara 10ml', 'sku': 'COS-MSC-143', 'batch': 'BATCH-CMSC-143', 'supplier': 'BeautyPro'},
        {'name': 'Eyeshadow Palette', 'sku': 'COS-EYE-144', 'batch': 'BATCH-CEYE-144', 'supplier': 'ColorCosmetics'},
        {'name': 'Blush Powder', 'sku': 'COS-BLU-145', 'batch': 'BATCH-CBLU-145', 'supplier': 'ColorCosmetics'},
        {'name': 'Face Cream 50ml', 'sku': 'COS-FCR-146', 'batch': 'BATCH-CFCR-146', 'supplier': 'SkinCarePro'},
        
        # Hair Care
        {'name': 'Shampoo 500ml', 'sku': 'HCR-SHP-147', 'batch': 'BATCH-HSHP-147', 'supplier': 'HairCarePro'},
        {'name': 'Conditioner 500ml', 'sku': 'HCR-CON-148', 'batch': 'BATCH-HCON-148', 'supplier': 'HairCarePro'},
        {'name': 'Hair Oil 200ml', 'sku': 'HCR-OIL-149', 'batch': 'BATCH-HOIL-149', 'supplier': 'NaturalCare'},
        {'name': 'Hair Spray 300ml', 'sku': 'HCR-SPR-150', 'batch': 'BATCH-HSPR-150', 'supplier': 'HairCarePro'},
        
        # Oral Care
        {'name': 'Toothpaste 100ml', 'sku': 'ORC-TPT-151', 'batch': 'BATCH-OTPT-151', 'supplier': 'DentalCare'},
        {'name': 'Mouthwash 500ml', 'sku': 'ORC-MOU-152', 'batch': 'BATCH-OMOU-152', 'supplier': 'DentalCare'},
        {'name': 'Dental Floss 50m', 'sku': 'ORC-FLS-153', 'batch': 'BATCH-OFLS-153', 'supplier': 'DentalCare'},
        {'name': 'Toothbrush Soft', 'sku': 'ORC-TBR-154', 'batch': 'BATCH-OTBR-154', 'supplier': 'DentalCare'},
        
        # Skin Care
        {'name': 'Facial Cleanser 200ml', 'sku': 'SKN-CLS-155', 'batch': 'BATCH-SCLS-155', 'supplier': 'SkinCarePro'},
        {'name': 'Moisturizer 100ml', 'sku': 'SKN-MST-156', 'batch': 'BATCH-SMST-156', 'supplier': 'SkinCarePro'},
        {'name': 'Sunscreen SPF50', 'sku': 'SKN-SUN-157', 'batch': 'BATCH-SSUN-157', 'supplier': 'SunProtect'},
        {'name': 'Eye Cream 30ml', 'sku': 'SKN-EYE-158', 'batch': 'BATCH-SEYE-158', 'supplier': 'SkinCarePro'},
        
        # Household Cleaning
        {'name': 'All-Purpose Cleaner 1L', 'sku': 'CLN-APC-159', 'batch': 'BATCH-CAPC-159', 'supplier': 'CleanHouse'},
        {'name': 'Dish Soap 500ml', 'sku': 'CLN-DSH-160', 'batch': 'BATCH-CDSH-160', 'supplier': 'CleanHouse'},
        {'name': 'Laundry Detergent 2L', 'sku': 'CLN-LDR-161', 'batch': 'BATCH-CLDR-161', 'supplier': 'LaundryCare'},
        {'name': 'Floor Cleaner 1L', 'sku': 'CLN-FLR-162', 'batch': 'BATCH-CFLR-162', 'supplier': 'CleanHouse'},
        {'name': 'Glass Cleaner 500ml', 'sku': 'CLN-GLS-163', 'batch': 'BATCH-CGLS-163', 'supplier': 'CleanHouse'},
        
        # Pet Supplies
        {'name': 'Dog Food 15kg', 'sku': 'PET-DOG-164', 'batch': 'BATCH-PDOG-164', 'supplier': 'PetCare'},
        {'name': 'Cat Food 10kg', 'sku': 'PET-CAT-165', 'batch': 'BATCH-PCAT-165', 'supplier': 'PetCare'},
        {'name': 'Pet Treats 500g', 'sku': 'PET-TRT-166', 'batch': 'BATCH-PTRT-166', 'supplier': 'PetCare'},
        {'name': 'Cat Litter 10L', 'sku': 'PET-LTR-167', 'batch': 'BATCH-PLTR-167', 'supplier': 'PetCare'},
    ]
    return household

def get_random_expiry_date():
    """Generate random expiry date for realistic data"""
    # 30% chance of expired products
    if random.random() < 0.3:
        # Expired between 1-90 days ago
        return today - timedelta(days=random.randint(1, 90))
    else:
        # Expiring between 0-365 days from now
        return today + timedelta(days=random.randint(0, 365))

def get_random_manufacture_date(expiry_date):
    """Generate manufacture date before expiry date"""
    # Manufactured between 30-730 days before expiry
    days_before = random.randint(30, 730)
    return expiry_date - timedelta(days=days_before)

def get_random_quantity():
    """Generate random quantity"""
    quantities = [10, 15, 20, 25, 30, 40, 50, 60, 75, 80, 100, 120, 150, 200, 250, 300, 500, 1000]
    return float(random.choice(quantities))

def get_unit_for_category(category_name):
    """Get appropriate unit based on category"""
    unit_map = {
        'Prescription Drugs': 'tablets',
        'Over-the-Counter Drugs': 'tablets',
        'Antibiotics': 'tablets',
        'Pain Relief': 'tablets',
        'Vitamins & Supplements': 'tablets',
        'Herbal & Natural Remedies': 'tablets',
        'Medical Supplies': 'pieces',
        'First Aid': 'pieces',
        'Baby & Child Health': 'ml',
        'Frozen Foods': 'kg',
        'Dairy Products': 'litres',
        'Beverages': 'litres',
        'Canned Goods': 'g',
        'Snacks & Chips': 'g',
        'Breakfast Cereals': 'g',
        'Pasta & Noodles': 'g',
        'Sauces & Condiments': 'ml',
        'Baking Supplies': 'g',
        'Cosmetics & Beauty': 'ml',
        'Hair Care': 'ml',
        'Oral Care': 'ml',
        'Skin Care': 'ml',
        'Household Cleaning': 'ml',
        'Pet Supplies': 'kg',
    }
    return unit_map.get(category_name, 'pieces')

def get_category_for_product(product_name, category_objects):
    """Get category object for product based on name"""
    category_map = {}
    for cat in category_objects:
        category_map[cat.name] = cat
    
    # Determine category based on product name
    if any(word in product_name for word in ['Amoxicillin', 'Ciprofloxacin', 'Metformin', 'Lisinopril', 'Omeprazole', 
                                            'Sertraline', 'Atorvastatin', 'Levothyroxine', 'Losartan', 'Gabapentin',
                                            'Alprazolam', 'Prednisone', 'Tramadol', 'Clonazepam', 'Metoprolol',
                                            'Pantoprazole', 'Fluoxetine', 'Amlodipine', 'Warfarin', 'Diazepam']):
        return category_map.get('Prescription Drugs')
    elif any(word in product_name for word in ['Ibuprofen', 'Paracetamol', 'Aspirin', 'Naproxen', 'Cetirizine',
                                               'Loratadine', 'Diphenhydramine', 'Loperamide', 'Ranitidine', 'Pseudoephedrine']):
        return category_map.get('Over-the-Counter Drugs')
    elif any(word in product_name for word in ['Azithromycin', 'Cephalexin', 'Doxycycline', 'Clarithromycin', 'Levofloxacin']):
        return category_map.get('Antibiotics')
    elif any(word in product_name for word in ['Morphine', 'Codeine', 'Oxycodone', 'Hydrocodone', 'Fentanyl']):
        return category_map.get('Pain Relief')
    elif any(word in product_name for word in ['Vitamin', 'Zinc', 'Magnesium', 'Calcium', 'Iron', 'Omega', 'Multivitamin',
                                               'Probiotic', 'Glucosamine', 'Coenzyme', 'Melatonin']):
        return category_map.get('Vitamins & Supplements')
    elif any(word in product_name for word in ['Echinacea', 'Ginseng', 'Ginkgo', 'St Johns', 'Valerian', 'Turmeric',
                                               'Garlic', 'Ashwagandha', 'CBD', 'Collagen']):
        return category_map.get('Herbal & Natural Remedies')
    elif any(word in product_name for word in ['Glucose', 'Pressure', 'Nebulizer', 'Pulse', 'Thermometer', 'Syringes',
                                               'Lancets', 'Surgical', 'Gloves', 'Dressing']):
        return category_map.get('Medical Supplies')
    elif any(word in product_name for word in ['First Aid', 'Bandage', 'Antiseptic', 'Hydrogen', 'Burn']):
        return category_map.get('First Aid')
    elif any(word in product_name for word in ['Baby', 'Childrens', 'Kids']):
        return category_map.get('Baby & Child Health')
    elif any(word in product_name for word in ['Frozen']):
        return category_map.get('Frozen Foods')
    elif any(word in product_name for word in ['Milk', 'Yogurt', 'Cheese', 'Butter', 'Cream']):
        return category_map.get('Dairy Products')
    elif any(word in product_name for word in ['Juice', 'Cola', 'Water', 'Coffee', 'Tea', 'Energy', 'Coconut']):
        return category_map.get('Beverages')
    elif any(word in product_name for word in ['Baked', 'Corn', 'Peas', 'Tuna', 'Soup', 'Spaghetti', 'Pineapple', 'Mushroom']):
        return category_map.get('Canned Goods')
    elif any(word in product_name for word in ['Chips', 'Puffs', 'Pretzel', 'Trail', 'Granola', 'Popcorn']):
        return category_map.get('Snacks & Chips')
    elif any(word in product_name for word in ['Corn Flakes', 'Oats', 'Muesli', 'Wheat']):
        return category_map.get('Breakfast Cereals')
    elif any(word in product_name for word in ['Spaghetti', 'Macaroni', 'Noodles', 'Pasta']):
        return category_map.get('Pasta & Noodles')
    elif any(word in product_name for word in ['Ketchup', 'Mayonnaise', 'Soy', 'Olive', 'Vinegar']):
        return category_map.get('Sauces & Condiments')
    elif any(word in product_name for word in ['Flour', 'Sugar', 'Baking', 'Cocoa']):
        return category_map.get('Baking Supplies')
    elif any(word in product_name for word in ['Foundation', 'Concealer', 'Lipstick', 'Mascara', 'Eyeshadow', 'Blush', 'Face Cream']):
        return category_map.get('Cosmetics & Beauty')
    elif any(word in product_name for word in ['Shampoo', 'Conditioner', 'Hair Oil', 'Hair Spray']):
        return category_map.get('Hair Care')
    elif any(word in product_name for word in ['Toothpaste', 'Mouthwash', 'Dental', 'Toothbrush']):
        return category_map.get('Oral Care')
    elif any(word in product_name for word in ['Cleanser', 'Moisturizer', 'Sunscreen', 'Eye Cream']):
        return category_map.get('Skin Care')
    elif any(word in product_name for word in ['Cleaner', 'Dish', 'Laundry', 'Floor', 'Glass']):
        return category_map.get('Household Cleaning')
    elif any(word in product_name for word in ['Dog', 'Cat', 'Pet']):
        return category_map.get('Pet Supplies')
    else:
        return None

def get_all_products():
    """Combine all product lists and add random expiry dates"""
    all_products = []
    
    # Get all product data
    drug_products = generate_drug_products()
    supplement_products = generate_supplement_products()
    food_products = generate_food_products()
    household_products = generate_household_products()
    
    # Combine all
    all_product_data = drug_products + supplement_products + food_products + household_products
    
    # Add random expiry and manufacture dates
    for product in all_product_data:
        expiry_date = get_random_expiry_date()
        manufacture_date = get_random_manufacture_date(expiry_date)
        quantity = get_random_quantity()
        # Determine unit later in seeding
        all_products.append({
            'product_name': product['name'],
            'description': f"{product['name']} - Premium quality product",
            'sku': product['sku'],
            'batch_number': product['batch'],
            'quantity': quantity,
            'unit': 'pieces',  # Will be updated based on category
            'manufacture_date': manufacture_date,
            'expiry_date': expiry_date,
            'supplier_name': product['supplier'],
            'is_active': True,
            'category_name': product.get('category', '')  # Will be mapped later
        })
    
    return all_products

def seed_categories():
    """Seed categories into database"""
    print("=" * 60)
    print("SEEDING CATEGORIES")
    print("=" * 60)
    created_count = 0
    existing_count = 0
    
    for cat_data in CATEGORIES:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            created_count += 1
            print(f"  Created: {category.name}")
        else:
            existing_count += 1
            print(f"  Exists: {category.name}")
            
    print(f"\nCategories: {created_count} created, {existing_count} already exist")
    return created_count

def seed_products():
    """Seed products into database"""
    print("\n" + "=" * 60)
    print("SEEDING PRODUCTS")
    print("=" * 60)
    
    created_count = 0
    existing_count = 0
    error_count = 0
    
    # Get admin user for added_by field
    try:
        admin_user = User.objects.get(username='admin')
    except User.DoesNotExist:
        print("  Warning: Admin user not found")
        admin_user = None
    
    # Get all categories
    categories = list(Category.objects.all())
    category_dict = {cat.name: cat for cat in categories}
    
    # Get all products with random data
    all_products = get_all_products()
    
    # Map each product to a category
    for product_data in all_products:
        # Find appropriate category
        category = get_category_for_product(product_data['product_name'], categories)
        
        if not category:
            # Assign to a random category if no match found
            category = random.choice(categories)
        
        # Update unit based on category
        product_data['unit'] = get_unit_for_category(category.name)
        
        # Prepare product data
        product_dict = {
            'product_name': product_data['product_name'],
            'description': product_data['description'],
            'sku': product_data['sku'],
            'batch_number': product_data['batch_number'],
            'quantity': product_data['quantity'],
            'unit': product_data['unit'],
            'manufacture_date': product_data['manufacture_date'],
            'expiry_date': product_data['expiry_date'],
            'supplier_name': product_data['supplier_name'],
            'is_active': product_data['is_active'],
        }
        
        if admin_user:
            product_dict['added_by'] = admin_user
        
        try:
            product, created = Product.objects.get_or_create(
                sku=product_dict['sku'],
                defaults=product_dict
            )
            
            # Set category
            product.category = category
            product.save()
            
            if created:
                created_count += 1
                days = (product.expiry_date - today).days
                status = "EXPIRED" if days < 0 else "ACTIVE"
                print(f"  Created: {product.product_name[:30]}... | Expiry: {product.expiry_date} | Days: {days} | Status: {status}")
            else:
                existing_count += 1
                if existing_count <= 5:  # Only show first 5 existing products to reduce output
                    print(f"  Exists: {product.product_name[:30]}... (SKU: {product.sku})")
                
        except IntegrityError as e:
            error_count += 1
            print(f"  Error creating {product_data['product_name'][:30]}: {str(e)}")
        except Exception as e:
            error_count += 1
            print(f"  Unexpected error: {str(e)}")
    
    if existing_count > 5:
        print(f"  ... and {existing_count - 5} more existing products")
    
    print(f"\nProducts: {created_count} created, {existing_count} already exist, {error_count} errors")
    return created_count, existing_count, error_count

def main():
    """Main seeding function"""
    print("=" * 60)
    print("EXPIRY ALERT SYSTEM - DATABASE SEEDING")
    print("=" * 60)
    
    # Test database connection
    try:
        from django.db import connection
        connection.ensure_connection()
        print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")
        return
    
    # Get or create admin user
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
        print("Admin user created with username 'admin'")
    else:
        print("Admin user already exists with username 'admin'")
    
    # Seed categories
    categories_created = seed_categories()
    
    # Seed products
    products_created, products_existing, products_errors = seed_products()
    
    # Final summary
    print("\n" + "=" * 60)
    print("SEEDING COMPLETE - SUMMARY")
    print("=" * 60)
    
    total_categories = Category.objects.count()
    total_products = Product.objects.count()
    
    print(f"Total Categories: {total_categories}")
    print(f"Total Products: {total_products}")
    print("\nProduct Status Summary:")
    print(f"  Expired: {Product.objects.filter(expiry_date__lt=today).count()}")
    print(f"  Expiring Today: {Product.objects.filter(expiry_date=today).count()}")
    print(f"  Active: {Product.objects.filter(expiry_date__gt=today).count()}")
    
    if products_errors > 0:
        print(f"\nWarning: {products_errors} errors occurred during seeding")
    
    print("\nLogin Credentials:")
    print("  Username: admin")
    print("  Password: admin123")

if __name__ == "__main__":
    main()