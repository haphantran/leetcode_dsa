"""
Let's manually verify the eggeekgbbeg solution step by step
"""


def manual_verification():
    """
    Let's manually trace through the original algorithm to verify
    """
    s = "eggeekgbbeg"
    print(f"Starting with: {s}")
    print("=" * 50)

    s_list = list(s)
    moves = 0
    i, j = 0, len(s_list) - 1

    print(f"Initial: {''.join(s_list)}")
    print(f"Positions: {' '.join(str(x) for x in range(len(s_list)))}")
    print()

    step = 1
    while i < j:
        print(f"Step {step}: i={i}, j={j}")
        print(f"Current: {''.join(s_list)}")
        print(f"Looking for match for s[{i}]='{s_list[i]}'")

        # Find match from right side
        k = j
        while k > i:
            if s_list[i] == s_list[k]:
                print(f"Found '{s_list[k]}' at position {k}")
                # Move k to j
                swaps = j - k
                print(f"Moving from {k} to {j}: {swaps} swaps")
                for m in range(k, j):
                    s_list[m], s_list[m + 1] = s_list[m + 1], s_list[m]
                    moves += 1
                    print(f"  After swap {m}↔{m+1}: {''.join(s_list)}")
                j -= 1
                break
            k -= 1

        if k == i:  # No match found
            middle = len(s_list) // 2
            middle_moves = middle - i
            print(f"No match found. Moving '{s_list[i]}' to middle (pos {middle})")
            print(f"Middle moves: {middle_moves}")
            moves += middle_moves

        print(f"Total moves so far: {moves}")
        print()
        i += 1
        step += 1

    print(f"Final string: {''.join(s_list)}")
    print(f"Total moves: {moves}")
    print(f"Is palindrome: {''.join(s_list) == ''.join(s_list)[::-1]}")


def check_character_frequencies():
    """
    Check what palindromes are possible with eggeekgbbeg
    """
    s = "eggeekgbbeg"
    from collections import Counter

    print("Character frequency analysis:")
    freq = Counter(s)
    print(f"Characters in '{s}':")
    for char, count in sorted(freq.items()):
        print(f"  '{char}': {count}")

    odd_count = sum(1 for count in freq.values() if count % 2 == 1)
    print(f"\nCharacters with odd frequency: {odd_count}")

    if odd_count <= 1:
        print("✓ Can form a palindrome (at most 1 odd frequency)")
    else:
        print("✗ Cannot form a palindrome (more than 1 odd frequency)")

    print("\nPossible palindrome structure:")
    pairs = []
    middle = ""

    for char, count in sorted(freq.items()):
        if count % 2 == 1:
            middle = char
        pairs.extend([char] * (count // 2))

    left_half = "".join(pairs)
    right_half = left_half[::-1]
    palindrome = left_half + middle + right_half

    print(f"One possible palindrome: {palindrome}")
    return palindrome


if __name__ == "__main__":
    manual_verification()
    print("\n" + "=" * 50)
    check_character_frequencies()
