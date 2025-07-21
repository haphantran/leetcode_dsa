"""
Analysis of why the "always move to right" approach is still optimal
"""


def analyze_both_directions(s):
    """
    Let's manually trace both approaches for a test case
    """
    print(f"Analyzing string: {s}")
    s_list = list(s)

    # Let's say we're at position i=1, j=6 in "abcdefg"
    # We want to match s[1]='b'

    # Option 1: Find 'b' on the right side and move it to position j
    # Option 2: Find matching char for s[j] on left side and move it to position i

    # The key insight: In a palindrome, EVERY character must have its pair
    # So whether we move left->right or right->left, we'll eventually need
    # the same total number of swaps for the entire string

    return


def demonstrate_equivalence():
    """
    Mathematical proof that both approaches yield the same result
    """
    print("=== Mathematical Reasoning ===")
    print()
    print("Consider any palindrome formation:")
    print("- Every character (except possibly one middle char) needs a pair")
    print("- The total 'displacement' of all characters from their final positions is FIXED")
    print("- Whether we move A to match B, or B to match A, the total work is the same")
    print()

    print("Example with 'abcba':")
    print("Initial:  a b c b a")
    print("          0 1 2 3 4")
    print("Target:   a b c b a  (already a palindrome)")
    print()

    print("Example with 'abcab':")
    print("Initial:  a b c a b")
    print("          0 1 2 3 4")
    print("Final:    a b a c b  or  b c a c b  or other valid palindromes")
    print()

    print("Key insight: The MINIMUM total displacement is invariant!")
    print("It doesn't matter which direction we choose for each pair.")


def detailed_eggeekgbbeg_trace():
    """
    Complete step-by-step trace of eggeekgbbeg
    """
    s = "eggeekgbbeg"
    print(f"\n{'='*60}")
    print(f"DETAILED TRACE: {s}")
    print(f"{'='*60}")
    print("Goal: Transform into a palindrome using minimum adjacent swaps")
    print()

    s_list = list(s)
    moves = 0

    # Show initial state with positions
    print("Initial state:")
    print(f"String: {' '.join(s_list)}")
    print(f"Index:  {' '.join(str(i) for i in range(len(s_list)))}")
    print()

    i, j = 0, len(s_list) - 1
    step = 1

    while i < j:
        print(f"--- STEP {step} ---")
        print(f"Left pointer i={i}, Right pointer j={j}")
        print(f"Current string: {''.join(s_list)}")
        print(f"Need to match: s[{i}]='{s_list[i]}' with something on the right")

        # Visualize the search area
        search_area = ["_"] * len(s_list)
        for idx in range(i, j + 1):
            search_area[idx] = s_list[idx]
        search_area[i] = f"[{s_list[i]}]"  # Mark left character
        search_area[j] = f"({s_list[j]})"  # Mark right boundary
        print(f"Search area: {' '.join(search_area)}")

        # Find matching character from right side
        k = j
        found = False
        print(f"Searching for '{s_list[i]}' from right to left...")

        while k > i:
            print(f"  Checking position {k}: '{s_list[k]}' ", end="")
            if s_list[i] == s_list[k]:
                print("✓ MATCH FOUND!")
                found = True
                break
            else:
                print("✗")
            k -= 1

        if found:
            swaps_needed = j - k
            print(f"Need to move '{s_list[k]}' from position {k} to position {j}")
            print(f"This requires {swaps_needed} adjacent swaps")

            # Show each individual swap
            if swaps_needed > 0:
                print("Performing swaps:")
                for m in range(k, j):
                    print(f"  Swap positions {m} and {m+1}: ", end="")
                    print(f"'{s_list[m]}' ↔ '{s_list[m+1]}'")
                    s_list[m], s_list[m + 1] = s_list[m + 1], s_list[m]
                    print(f"    Result: {''.join(s_list)}")
                    moves += 1

            j -= 1
            print(f"Right pointer moves inward: j={j}")

        else:
            print(f"No match found for '{s_list[i]}' - this must be the middle character")
            middle_pos = len(s_list) // 2
            middle_moves = abs(middle_pos - i)
            print(f"Moving '{s_list[i]}' to middle position {middle_pos}")
            print(f"This requires {middle_moves} moves")
            moves += middle_moves

        print(f"String after step {step}: {''.join(s_list)}")
        print(f"Total moves so far: {moves}")
        print()

        i += 1
        step += 1

        if step > 10:  # Safety break
            break

    print(f"{'='*60}")
    print(f"FINAL RESULT: {moves} total moves")
    print(f"Final string: {''.join(s_list)}")
    print(f"Is palindrome? {is_palindrome(''.join(s_list))}")
    print(f"{'='*60}")


def is_palindrome(s):
    """Check if string is a palindrome"""
    return s == s[::-1]


def test_with_detailed_trace():
    """
    Let's trace through eggeekgbbeg to see why right-only works
    """
    detailed_eggeekgbbeg_trace()


if __name__ == "__main__":
    demonstrate_equivalence()
    test_with_detailed_trace()
