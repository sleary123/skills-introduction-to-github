import sys

def longest_alternating_increasing(A, B):
    items = [('A', i, v) for i, v in enumerate(A)] + [('B', j, v) for j, v in enumerate(B)]
    items.sort(key=lambda t: t[1])  

    n = len(items)
    dp, prev = [1]*n, [-1]*n

    for i in range(n):
        for j in range(i):
            if items[i][0] != items[j][0] and items[i][1] > items[j][1] and items[i][2] > items[j][2]:
                if dp[j] + 1 > dp[i]:
                    dp[i], prev[i] = dp[j] + 1, j

    end = max(range(n), key=lambda k: dp[k])
    seq = []
    while end != -1:
        seq.append(items[end][2])
        end = prev[end]
    seq.reverse()

    return len(seq), seq


if __name__ == "__main__":
    f = sys.argv[1]
    lines = open(f).read().strip().splitlines()
    A = list(map(int, lines[2].split()))
    B = list(map(int, lines[3].split()))
    length, seq = longest_alternating_increasing(A, B)
    print(f"Longest Sequence: {length}")

