from pydantic import BaseModel, Field


class ProductBase(BaseModel):
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


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int

    class Config:
        from_attributes = True
