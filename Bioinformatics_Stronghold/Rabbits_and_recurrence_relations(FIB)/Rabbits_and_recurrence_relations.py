
with open('') as sample:
    rabbits_months = sample


def rabbits_pairs(n, k):
    prev_month = 1
    current_month = 1

    for _ in range(2, n):
        children = prev_month*k
        prev_month, current_month = current_month, current_month + children

    return current_month