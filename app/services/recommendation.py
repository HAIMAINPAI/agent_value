from app.services.profit import calculate_profit
from app.services.scoring import score_product


def build_recommendation(product):
    profit_data = calculate_profit(
        cost=product.cost,
        price=product.price,
        weight_kg=product.weight_kg,
        ad_spend_per_sale=getattr(product, "ad_spend_per_sale", 0.0),
        return_rate=getattr(product, "return_rate", 0.03),
        prep_fee=getattr(product, "prep_fee", 0.0),
        storage_fee=getattr(product, "storage_fee", 0.5),
    )
    score_data = score_product(
        margin=profit_data["margin"],
        price=product.price,
        monthly_sales=product.monthly_sales,
        review_count=product.review_count,
        rating=product.rating,
        competition_level=product.competition_level,
    )
    return {
        "name": product.name,
        "keyword": product.keyword,
        "category": product.category,
        "profit": profit_data["profit"],
        "margin": profit_data["margin"],
        "score": score_data["score"],
        "level": score_data["level"],
        "monthly_sales": product.monthly_sales,
        "review_count": product.review_count,
        "rating": product.rating,
    }


def sort_recommendations(items):
    return sorted(items, key=lambda x: (x["score"], x["profit"]), reverse=True)
