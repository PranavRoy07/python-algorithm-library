def max_profit(prices: list[int]) -> int:
    """Find the maximum profit from buying and selling stock once.

    You must buy before you sell. If no profit is possible,
    return 0.

    Args:
        prices: A list of stock prices, one per day.

    Returns:
        The maximum profit achievable, or 0 if none.
    """
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        best_profit = max(best_profit, profit)

    return best_profit