"""
Comparison: Right-only vs Bidirectional approach
"""


def min_moves_right_only(s):
    """Original approach - always move to right"""
    s = list(s)
    moves = 0
    i, j = 0, len(s) - 1

    while i < j:
        k = j
        while k > i:
            if s[i] == s[k]:
                moves += j - k  # Count moves to bring k to j
                # Simulate the moves
                for m in range(k, j):
                    s[m], s[m + 1] = s[m + 1], s[m]
                j -= 1
                break
            k -= 1
        if k == i:  # No match found
            moves += len(s) // 2 - i
        i += 1

    return moves


def min_moves_bidirectional(s):
    """Bidirectional approach - choose optimal direction"""
    s = list(s)
    moves = 0
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue

        # Find match for s[i] on right side
        right_match = -1
        for k in range(j - 1, i, -1):
            if s[i] == s[k]:
                right_match = k
                break

        # Find match for s[j] on left side
        left_match = -1
        for k in range(i + 1, j):
            if s[j] == s[k]:
                left_match = k
                break

        if right_match == -1 and left_match == -1:
            # One character must go to middle
            moves += len(s) // 2 - i
            i += 1
        elif right_match == -1:
            # Only left match available
            cost = left_match - i
            moves += cost
            # Move left_match to position i
            for m in range(left_match, i, -1):
                s[m], s[m - 1] = s[m - 1], s[m]
            i += 1
            j -= 1
        elif left_match == -1:
            # Only right match available
            cost = j - right_match
            moves += cost
            # Move right_match to position j
            for m in range(right_match, j):
                s[m], s[m + 1] = s[m + 1], s[m]
            i += 1
            j -= 1
        else:
            # Both matches available - choose cheaper option
            left_cost = left_match - i
            right_cost = j - right_match

            if left_cost <= right_cost:
                moves += left_cost
                # Move left_match to position i
                for m in range(left_match, i, -1):
                    s[m], s[m - 1] = s[m - 1], s[m]
            else:
                moves += right_cost
                # Move right_match to position j
                for m in range(right_match, j):
                    s[m], s[m + 1] = s[m + 1], s[m]
            i += 1
            j -= 1

    return moves


def test_both_approaches():
    """Test both approaches on various inputs"""
    test_cases = ["aabb", "letelt", "eggeekgbbeg", "abcdefg", "racecar", "aabaa"]

    print("Comparing Right-Only vs Bidirectional approaches:")
    print("=" * 50)

    for test in test_cases:
        right_only = min_moves_right_only(test)
        bidirectional = min_moves_bidirectional(test)

        print(f"Input: '{test}'")
        print(f"  Right-only:     {right_only}")
        print(f"  Bidirectional:  {bidirectional}")
        print(f"  Difference:     {abs(right_only - bidirectional)}")
        print()


if __name__ == "__main__":
    test_both_approaches()
