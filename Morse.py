import sys

VOWEL_MORSE = {'A': '.-', 'E': '.', 'I': '..', 'O': '---', 'U': '..-'}

def count_vowel_combinations(code):
    n = len(code)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for p in VOWEL_MORSE.values():
            if code.startswith(p, i - len(p)):
                dp[i] += dp[i - len(p)]
    return dp[n]

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        code = lines[1].strip() if len(lines) > 1 else ''
    print(f"File Input: {filename}")
    print(f"The Number of Vowel combinations is: {count_vowel_combinations(code)}")
