from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models import Product
from app.schemas.analysis import AnalysisInput
from app.services.profit import calculate_profit
from app.services.scoring import score_product
from app.services.recommendation import build_recommendation, sort_recommendations

router = APIRouter()


@router.post("/profit")
def profit_analysis(payload: AnalysisInput):
    profit_data = calculate_profit(
        cost=payload.cost,
        price=payload.price,
        weight_kg=payload.weight_kg,
        ad_spend_per_sale=payload.ad_spend_per_sale,
        return_rate=payload.return_rate,
        prep_fee=payload.prep_fee,
        storage_fee=payload.storage_fee,
    )
    return {
        "product": payload.name,
        "profit_analysis": profit_data,
    }


@router.post("/score")
def score_analysis(payload: AnalysisInput):
    profit_data = calculate_profit(
        cost=payload.cost,
        price=payload.price,
        weight_kg=payload.weight_kg,
        ad_spend_per_sale=payload.ad_spend_per_sale,
        return_rate=payload.return_rate,
        prep_fee=payload.prep_fee,
        storage_fee=payload.storage_fee,
    )
    score_data = score_product(
        margin=profit_data["margin"],
        price=payload.price,
        monthly_sales=payload.monthly_sales,
        review_count=payload.review_count,
        rating=payload.rating,
        competition_level=payload.competition_level,
    )
    return {
        "product": payload.name,
        "profit": profit_data,
        "score": score_data,
    }


@router.get("/recommendations")
def recommendations(db: Session = Depends(get_db), limit: int = 10):
    products = db.query(Product).all()
    items = [build_recommendation(p) for p in products]
    items = sort_recommendations(items)
    return items[:limit]


@router.get("/keyword/{keyword}")
def keyword_recommend(keyword: str):
    """
    模拟关键词选品结果，方便毕业设计展示。
    """
    candidates = [
        {
            "name": f"{keyword.title()} Pro",
            "keyword": keyword,
            "category": "General",
            "cost": 4.2,
            "price": 19.99,
            "weight_kg": 0.25,
            "monthly_sales": 1000,
            "review_count": 180,
            "rating": 4.4,
            "competition_level": 0.45,
        },
        {
            "name": f"{keyword.title()} Kit",
            "keyword": keyword,
            "category": "General",
            "cost": 2.9,
            "price": 14.99,
            "weight_kg": 0.18,
            "monthly_sales": 1800,
            "review_count": 420,
            "rating": 4.3,
            "competition_level": 0.58,
        },
        {
            "name": f"Premium {keyword.title()}",
            "keyword": keyword,
            "category": "General",
            "cost": 6.5,
            "price": 29.99,
            "weight_kg": 0.33,
            "monthly_sales": 650,
            "review_count": 90,
            "rating": 4.6,
            "competition_level": 0.32,
        },
    ]

    results = []
    for c in candidates:
        profit = calculate_profit(c["cost"], c["price"], c["weight_kg"])
        score = score_product(
            margin=profit["margin"],
            price=c["price"],
            monthly_sales=c["monthly_sales"],
            review_count=c["review_count"],
            rating=c["rating"],
            competition_level=c["competition_level"],
        )
        results.append({
            **c,
            "profit": profit["profit"],
            "margin": profit["margin"],
            "score": score["score"],
            "level": score["level"],
            "reasons": score["reasons"],
        })

    results.sort(key=lambda x: (x["score"], x["profit"]), reverse=True)
    return results
