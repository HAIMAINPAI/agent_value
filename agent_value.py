# -*- coding: utf-8 -*-
"""
AI选品 + 利润测算 Agent（适用于Amazon跨境电商）
技术栈：Python + FastAPI + SQLite + 简单规则引擎

功能：
1. 关键词选品（模拟）
2. 利润测算（FBA模型）
3. 简单AI评分（潜力评分）
4. API接口

运行：
pip install fastapi uvicorn pydantic
uvicorn main:app --reload

访问：http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# ===================== 数据库 =====================
def init_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        cost REAL,
        price REAL,
        weight REAL,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ===================== 数据模型 =====================
class ProductInput(BaseModel):
    name: str
    cost: float
    price: float
    weight: float
    category: str

# ===================== 利润计算 =====================
def calculate_profit(cost, price, weight):
    """
    简化FBA利润模型：
    """
    referral_fee = price * 0.15
    fba_fee = 3 + weight * 0.5
    storage_fee = 0.5

    total_cost = cost + referral_fee + fba_fee + storage_fee
    profit = price - total_cost
    margin = profit / price

    return {
        "profit": round(profit, 2),
        "margin": round(margin, 2),
        "total_cost": round(total_cost, 2)
    }

# ===================== AI评分（简单规则） =====================
def ai_score(margin, price):
    score = 0

    # 利润率评分
    if margin > 0.3:
        score += 40
    elif margin > 0.2:
        score += 30
    else:
        score += 10

    # 价格区间评分
    if 15 <= price <= 50:
        score += 30
    else:
        score += 10

    # 随机竞争难度（模拟）
    import random
    competition = random.uniform(0, 1)
    if competition < 0.3:
        score += 30
    elif competition < 0.6:
        score += 20
    else:
        score += 5

    return score

# ===================== API：添加产品 =====================
@app.post("/add_product")
def add_product(product: ProductInput):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO products (name, cost, price, weight, category)
    VALUES (?, ?, ?, ?, ?)
    """, (product.name, product.cost, product.price, product.weight, product.category))

    conn.commit()
    conn.close()

    return {"msg": "Product added"}

# ===================== API：利润测算 =====================
@app.post("/calculate")
def calculate(product: ProductInput):
    result = calculate_profit(product.cost, product.price, product.weight)
    score = ai_score(result["margin"], product.price)

    return {
        "product": product.name,
        "profit": result["profit"],
        "margin": result["margin"],
        "score": score
    }

# ===================== API：获取推荐产品 =====================
@app.get("/recommend")
def recommend():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, cost, price, weight FROM products")
    rows = cursor.fetchall()

    result = []

    for r in rows:
        profit_data = calculate_profit(r[1], r[2], r[3])
        score = ai_score(profit_data["margin"], r[2])

        result.append({
            "name": r[0],
            "profit": profit_data["profit"],
            "margin": profit_data["margin"],
            "score": score
        })

    # 按评分排序
    result.sort(key=lambda x: x["score"], reverse=True)

    return result[:10]

# ===================== 模拟AI选品 =====================
@app.get("/ai_select")
def ai_select(keyword: str):
    """
    模拟根据关键词选品（后续可接入真实API）
    """
    mock_products = [
        {"name": f"{keyword} bottle", "price": 19.99},
        {"name": f"{keyword} kit", "price": 29.99},
        {"name": f"{keyword} pro", "price": 39.99},
    ]

    return mock_products
