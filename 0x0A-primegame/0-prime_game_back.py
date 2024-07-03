def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for multiple in range(p * p, max_num + 1, p):
                is_prime[multiple] = False
        p += 1
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_game = [p for p in primes if p <= n]
        # False means losing position, True means winning position
        round_result = [False] * (n + 1)

        for i in range(1, n + 1):
            if i in primes_in_game:
                round_result[i] = not round_result[i]
            for p in primes_in_game:
                if i - p >= 0 and not round_result[i - p]:
                    round_result[i] = True
                    break

        if round_result[n]:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
