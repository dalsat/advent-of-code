from functools import cache


def coin_change(coins, amount) -> int | None:

    @cache
    def coin_change_rec(amount) -> int | None:
        if amount < 0:
            return None
        if amount == 0:
            return 0
        results = list(
            result + 1
            for each in coins
            if (result := coin_change_rec(amount - each)) is not None
        )
        if results:
            return min(results)

    return coin_change_rec(amount)


examples = [
    # ([1, 2, 5], 11, 3),
    # ([2], 3, -1),
    # ([1], 0, 0),
    # ([1, 2, 3, 5, 10, 15], 200, 3),
    ([1, 2, 3], 331, 3)
]

for coins, amount, expected in examples:
    print(f"{coins}, {amount} -> {expected} vs. {coin_change(coins, amount)}")
