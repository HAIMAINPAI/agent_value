def get_score_level(score: int) -> str:
    if score >= 80:
        return "A"
    if score >= 65:
        return "B"
    if score >= 50:
        return "C"
    return "D"


def score_product(
    margin: float,
    price: float,
    monthly_sales: int = 0,
    review_count: int = 0,
    rating: float = 0.0,
    competition_level: float = 0.5,
) -> dict:
    """
    规则版 AI 评分：
    - 利润率
    - 价格带
    - 销量
    - 评论门槛
    - 星级
    - 竞争程度
    """
    score = 0
    reasons = []

    if margin >= 0.35:
        score += 25
        reasons.append("利润率优秀")
    elif margin >= 0.25:
        score += 20
        reasons.append("利润率较好")
    elif margin >= 0.15:
        score += 10
        reasons.append("利润率一般")
    else:
        reasons.append("利润率偏低")

    if 15 <= price <= 45:
        score += 15
        reasons.append("价格带适合跨境电商")
    elif 10 <= price < 15 or 45 < price <= 60:
        score += 8
        reasons.append("价格带可接受")
    else:
        reasons.append("价格带不够理想")

    if monthly_sales >= 2000:
        score += 15
        reasons.append("市场需求较强")
    elif monthly_sales >= 800:
        score += 10
        reasons.append("市场有稳定需求")
    elif monthly_sales > 0:
        score += 5
        reasons.append("有一定需求信号")

    if review_count <= 300:
        score += 15
        reasons.append("评论门槛较低")
    elif review_count <= 1000:
        score += 8
        reasons.append("评论门槛中等")
    else:
        reasons.append("评论壁垒较高")

    if rating >= 4.5:
        score += 10
        reasons.append("评分表现优秀")
    elif rating >= 4.2:
        score += 6
        reasons.append("评分表现不错")
    elif rating > 0:
        score += 2
        reasons.append("评分存在提升空间")

    if competition_level <= 0.35:
        score += 20
        reasons.append("竞争较低")
    elif competition_level <= 0.6:
        score += 10
        reasons.append("竞争可控")
    else:
        reasons.append("竞争偏高")

    score = min(score, 100)
    return {
        "score": score,
        "level": get_score_level(score),
        "reasons": reasons,
    }
