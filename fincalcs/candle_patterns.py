def gravestone_doji(
    open: float, close: float, high: float, low: float
) -> bool:
    return (
        close == open and high > open and (close - low) * 1.2 < (high - close)
    )


def four_price_doji(
    open: float, close: float, high: float, low: float
) -> bool:
    return close == open == high == low