from sqlalchemy.orm import Session

from app.db.init_db import init_db
from app.db.session import SessionLocal
from app.db.models import Product


SEED_PRODUCTS = [
    {
        "name": "Silicone Travel Bottle Set",
        "keyword": "travel bottle",
        "category": "Travel Accessories",
        "cost": 3.2,
        "price": 15.99,
        "weight_kg": 0.18,
        "monthly_sales": 1200,
        "review_count": 380,
        "rating": 4.5,
        "competition_level": 0.55,
    },
    {
        "name": "Fogless Shower Mirror",
        "keyword": "shower mirror",
        "category": "Bathroom",
        "cost": 4.8,
        "price": 19.99,
        "weight_kg": 0.35,
        "monthly_sales": 860,
        "review_count": 210,
        "rating": 4.4,
        "competition_level": 0.42,
    },
    {
        "name": "Kitchen Sink Strainer",
        "keyword": "sink strainer",
        "category": "Kitchen",
        "cost": 1.4,
        "price": 9.99,
        "weight_kg": 0.09,
        "monthly_sales": 3200,
        "review_count": 980,
        "rating": 4.6,
        "competition_level": 0.73,
    },
    {
        "name": "Reusable Lunch Bag",
        "keyword": "lunch bag",
        "category": "Kitchen",
        "cost": 2.9,
        "price": 13.99,
        "weight_kg": 0.22,
        "monthly_sales": 1400,
        "review_count": 500,
        "rating": 4.3,
        "competition_level": 0.48,
    },
]


def seed_db():
    init_db()
    db: Session = SessionLocal()
    try:
        existing = db.query(Product).count()
        if existing > 0:
            return

        for item in SEED_PRODUCTS:
            db.add(Product(**item))
        db.commit()
    finally:
        db.close()
