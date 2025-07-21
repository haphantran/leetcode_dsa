"""
Corrected trace showing actual swaps for eggeekgbbeg
"""


def corrected_trace():
    """
    Show exactly what happens step by step with actual swaps
    """
    s = "eggeekgbbeg"
    print(f"Tracing: {s}")
    print("=" * 60)

    s_list = list(s)
    moves = 0
    i, j = 0, len(s_list) - 1

    print(f"Initial: {''.join(s_list)}")
    print(f"Indices: {' '.join(f'{x:2d}' for x in range(len(s_list)))}")
    print()

    step = 1
    while i < j:
        print(f"--- STEP {step} ---")
        print(f"i={i}, j={j}")
        print(f"Current: {''.join(s_list)}")
        print(f"Need to match s[{i}]='{s_list[i]}'")

        # Find matching character from right
        k = j
        found = False
        while k > i:
            if s_list[i] == s_list[k]:
                found = True
                break
            k -= 1

        if found:
            print(f"Found match '{s_list[k]}' at position {k}")
            swaps_needed = j - k
            print(f"Need {swaps_needed} swaps to move from {k} to {j}")

            # Actually perform the swaps
            for m in range(k, j):
                print(f"  Swap {m}↔{m+1}: '{s_list[m]}' ↔ '{s_list[m+1]}'")
                s_list[m], s_list[m + 1] = s_list[m + 1], s_list[m]
                moves += 1
                print(f"    Result: {''.join(s_list)}")

            j -= 1
            print(f"Move j inward: j={j}")
        else:
            # k == i, this is the middle character case
            print(f"No match found for '{s_list[i]}' - middle character")
            middle_pos = len(s_list) // 2
            current_pos = i
            swaps_for_middle = middle_pos - current_pos

            print(f"Need to move '{s_list[i]}' from position {current_pos} to middle position {middle_pos}")
            print(f"This requires {swaps_for_middle} swaps")

            # Actually perform the swaps to middle
            for m in range(current_pos, middle_pos):
                print(f"  Swap {m}↔{m+1}: '{s_list[m]}' ↔ '{s_list[m+1]}'")
                s_list[m], s_list[m + 1] = s_list[m + 1], s_list[m]
                moves += 1
                print(f"    Result: {''.join(s_list)}")

            moves += swaps_for_middle

        print(f"String after step {step}: {''.join(s_list)}")
        print(f"Total moves: {moves}")
        print()

        i += 1
        step += 1

    print(f"Final result: {''.join(s_list)}")
    print(f"Total moves: {moves}")
    print(f"Is palindrome: {s_list == s_list[::-1]}")


def analyze_original_algorithm():
    """
    Let's trace the ACTUAL algorithm line by line
    """
    print("\n" + "=" * 60)
    print("ANALYZING THE ACTUAL ALGORITHM")
    print("=" * 60)

    s = "eggeekgbbeg"
    s_list = list(s)
    moves = 0
    i, j = 0, len(s_list) - 1

    print("Original algorithm:")
    print("while i < j:")
    print("    k = j")
    print("    while k > i:")
    print("        if s[i] == s[k]:")
    print("            # move k to j, then j--, break")
    print("    if k == i:")
    print("        moves += len(s) // 2 - i")
    print("    i += 1")
    print()

    step = 1
    while i < j:
        print(f"Step {step}: i={i}, j={j}, s[i]='{s_list[i]}'")

        k = j
        while k > i:
            if s_list[i] == s_list[k]:
                print(f"  Found match at k={k}")
                # Move k to j
                for m in range(k, j):
                    s_list[m], s_list[m + 1] = s_list[m + 1], s_list[m]
                    moves += 1
                j -= 1
                print(f"  After moving: {''.join(s_list)}, moves={moves}")
                break
            k -= 1

        if k == i:
            middle_moves = len(s_list) // 2 - i
            print(f"  No match found, adding {middle_moves} moves for middle char")
            moves += middle_moves
            # Note: The original algorithm does NOT actually move the character!
            # It just adds the cost and continues

        i += 1
        step += 1

    print(f"\nFinal: moves={moves}")


if __name__ == "__main__":
    corrected_trace()
    analyze_original_algorithm()
