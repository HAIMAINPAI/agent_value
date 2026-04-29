from pydantic import BaseModel, Field
from typing import Optional


class AnalysisInput(BaseModel):
    name: str = Field(..., examples=["Fogless Shower Mirror"])
    keyword: str = Field(..., examples=["shower mirror"])
    category: str = Field(..., examples=["Bathroom"])
    cost: float = Field(..., ge=0)
    price: float = Field(..., gt=0)
    weight_kg: float = Field(..., ge=0)
    monthly_sales: int = Field(0, ge=0)
    review_count: int = Field(0, ge=0)
    rating: float = Field(0.0, ge=0, le=5)
    competition_level: float = Field(0.5, ge=0, le=1)

    ad_spend_per_sale: float = Field(0.0, ge=0)
    return_rate: float = Field(0.03, ge=0, le=1)
    prep_fee: float = Field(0.0, ge=0)
    storage_fee: float = Field(0.5, ge=0)


class ProfitResult(BaseModel):
    referral_fee: float
    fba_fee: float
    storage_fee: float
    ad_cost: float
    return_loss: float
    total_cost: float
    profit: float
    margin: float


class ScoreResult(BaseModel):
    score: int
    level: str
    reasons: list[str]


class RecommendationItem(BaseModel):
    name: str
    keyword: str
    category: str
    profit: float
    margin: float
    score: int
    level: str
    monthly_sales: int
    review_count: int
    rating: float
