import random
import string
import time
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from hvlcs import solve


def gen_input(alphabet_size, len_a, len_b, seed=None):
    if seed is not None:
        random.seed(seed)

    chars = list(string.ascii_lowercase[:alphabet_size])
    vals = {c: random.randint(1, 20) for c in chars}

    A = "".join(random.choices(chars, k=len_a))
    B = "".join(random.choices(chars, k=len_b))

    lines = [str(alphabet_size)]
    for c in chars:
        lines.append(f"{c} {vals[c]}")
    lines.append(A)
    lines.append(B)

    return "\n".join(lines)


def main():
    configs = [
        # (len_A, len_B)
        (25,   50),
        (50,  100),
        (75,  150),
        (100, 100),
        (200, 150),
        (200, 200),
        (300, 400),
        (400, 400),
        (500, 750),
        (750, 750),
        (1000, 1000),
        (1000, 1500),
    ]

    os.makedirs("data", exist_ok=True)

    print(f"{'Test':<6} {'Len A':<8} {'Len B':<8} {'m*n':<12} {'Time (s)':<10}")
    print("-" * 44)

    for i, (len_a, len_b) in enumerate(configs):
        input_text = gen_input(12, len_a, len_b, seed=42 + i)

        start = time.perf_counter()
        solve(input_text)
        elapsed = time.perf_counter() - start

        print(f"{i+1:<6} {len_a:<8} {len_b:<8} {len_a*len_b:<12} {elapsed:.4f}")


if __name__ == "__main__":
    main()