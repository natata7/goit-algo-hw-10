def find_coins_greedy(amount: int, coins: list[int]) -> dict[int, int]:
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount %= coin
            result[coin] = count
    return result


def find_min_coins(amount: int, coins: list[int]) -> dict[int, int]:
    if amount == 0:
        return {}

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # Реконструкція використаних монет зі списку last_coin
    result = {}
    curr_amount = amount
    while curr_amount > 0:
        coin = last_coin[curr_amount]
        result[coin] = result.get(coin, 0) + 1
        curr_amount -= coin

    return result


if __name__ == "__main__":
    test_amount = 113
    test_coins = [50, 25, 10, 5, 2, 1]

    print(f"Сума: {test_amount}")
    print(f"Номінали: {test_coins}")
    print("Жадібний алгоритм:", find_coins_greedy(test_amount, test_coins))
    print("Динамічне програмування:", find_min_coins(test_amount, test_coins))
