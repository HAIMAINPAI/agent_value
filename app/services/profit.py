from dataclasses import asdict, dataclass


@dataclass
class ProfitResult:
    referral_fee: float
    fba_fee: float
    storage_fee: float
    ad_cost: float
    return_loss: float
    total_cost: float
    profit: float
    margin: float


def calculate_profit(
    cost: float,
    price: float,
    weight_kg: float,
    ad_spend_per_sale: float = 0.0,
    return_rate: float = 0.03,
    prep_fee: float = 0.0,
    storage_fee: float = 0.5,
) -> dict:
    """
    简化版 Amazon 利润测算模型。
    你可以后续替换为更精确的 FBA / FNSKU / 头程 / 仓储 / 广告模型。
    """
    referral_fee = price * 0.15
    fba_fee = 3.0 + (weight_kg * 4.5)
    return_loss = price * return_rate
    ad_cost = ad_spend_per_sale
    total_cost = cost + referral_fee + fba_fee + storage_fee + ad_cost + return_loss + prep_fee
    profit = price - total_cost
    margin = profit / price if price else 0

    result = ProfitResult(
        referral_fee=round(referral_fee, 2),
        fba_fee=round(fba_fee, 2),
        storage_fee=round(storage_fee, 2),
        ad_cost=round(ad_cost, 2),
        return_loss=round(return_loss, 2),
        total_cost=round(total_cost, 2),
        profit=round(profit, 2),
        margin=round(margin, 4),
    )
    return asdict(result)
