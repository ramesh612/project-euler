#!/usr/bin/env python3
def S(N, s, f, u, memo):
    if N == 0:
        return s
    if (N, s, f, u) in memo:
        return memo[(N, s, f, u)]

    P_fair = 1 / 2
    P_unfair = 3 / 4

    result = (
        20 * P_fair +
        (s - 1) * P_fair * S(N - 1, s - 1, f - 1, u, memo) +
        (s - 1) * P_unfair * S(N - 1, s - 1, f, u - 1, memo) +
        (-30) * P_fair * S(N - 1, s - 1, f - 1, u, memo) +
        (-30) * P_unfair * S(N - 1, s - 1, f, u - 1, memo)
    ) / (f + u)

    memo[(N, s, f, u)] = result
    return result

result = S(50, 0, 50, 50, {})
print(round(result, 6))

