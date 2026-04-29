from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from app.db.session import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    keyword = Column(String(255), nullable=False, index=True)
    category = Column(String(100), nullable=False, index=True)

    cost = Column(Float, nullable=False)               # 到手成本
    price = Column(Float, nullable=False)              # 售价
    weight_kg = Column(Float, nullable=False)          # 重量（kg）
    monthly_sales = Column(Integer, default=0)         # 月销量估计
    review_count = Column(Integer, default=0)          # 评论数
    rating = Column(Float, default=0.0)               # 评分
    competition_level = Column(Float, default=0.5)    # 竞争程度 0~1

    created_at = Column(DateTime(timezone=True), server_default=func.now())
