"""
Script to generate all missing DSA problem files
"""

import os

# Define the structure with topics and their problems
problems_structure = {
    "fast_slow_pointers": [
        (
            "linked_list_cycle.py",
            "LeetCode #141",
            "Linked List Cycle",
            "https://leetcode.com/problems/linked-list-cycle/",
        ),
        (
            "middle_linked_list.py",
            "LeetCode #876",
            "Middle of the Linked List",
            "https://leetcode.com/problems/middle-of-the-linked-list/",
        ),
        (
            "circular_array_loop.py",
            "LeetCode #457",
            "Circular Array Loop",
            "https://leetcode.com/problems/circular-array-loop/",
        ),
        (
            "find_duplicate_number.py",
            "LeetCode #287",
            "Find the Duplicate Number",
            "https://leetcode.com/problems/find-the-duplicate-number/",
        ),
        (
            "palindrome_linked_list.py",
            "LeetCode #234",
            "Palindrome Linked List",
            "https://leetcode.com/problems/palindrome-linked-list/",
        ),
        (
            "max_twin_sum.py",
            "LeetCode #2130",
            "Maximum Twin Sum of a Linked List",
            "https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/",
        ),
        (
            "split_circular_list.py",
            "LeetCode #708",
            "Split a Circular Linked List",
            "https://leetcode.com/problems/split-array-into-consecutive-subsequences/",
        ),
        ("linked_list_cycle_iii.py", "Custom Problem", "Linked List Cycle III", "Custom Problem"),
        ("linked_list_cycle_iv.py", "Custom Problem", "Linked List Cycle IV", "Custom Problem"),
    ],
    "sliding_window": [
        (
            "repeated_dna_sequences.py",
            "LeetCode #187",
            "Repeated DNA Sequences",
            "https://leetcode.com/problems/repeated-dna-sequences/",
        ),
        (
            "sliding_window_maximum.py",
            "LeetCode #239",
            "Sliding Window Maximum",
            "https://leetcode.com/problems/sliding-window-maximum/",
        ),
        (
            "min_window_subsequence.py",
            "LeetCode #727",
            "Minimum Window Subsequence",
            "https://leetcode.com/problems/minimum-window-subsequence/",
        ),
        (
            "longest_repeating_char_replacement.py",
            "LeetCode #424",
            "Longest Repeating Character Replacement",
            "https://leetcode.com/problems/longest-repeating-character-replacement/",
        ),
        (
            "min_window_substring.py",
            "LeetCode #76",
            "Minimum Window Substring",
            "https://leetcode.com/problems/minimum-window-substring/",
        ),
        (
            "longest_substring_no_repeat.py",
            "LeetCode #3",
            "Longest Substring without Repeating Characters",
            "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
        ),
        (
            "min_size_subarray_sum.py",
            "LeetCode #209",
            "Minimum Size Subarray Sum",
            "https://leetcode.com/problems/minimum-size-subarray-sum/",
        ),
        (
            "max_average_subarray.py",
            "LeetCode #643",
            "Maximum Average Subarray I",
            "https://leetcode.com/problems/maximum-average-subarray-i/",
        ),
        (
            "diet_plan_performance.py",
            "LeetCode #1176",
            "Diet Plan Performance",
            "https://leetcode.com/problems/diet-plan-performance/",
        ),
        (
            "fruit_into_baskets.py",
            "LeetCode #904",
            "Fruit Into Baskets",
            "https://leetcode.com/problems/fruit-into-baskets/",
        ),
        (
            "contains_duplicate_ii.py",
            "LeetCode #219",
            "Contains Duplicate II",
            "https://leetcode.com/problems/contains-duplicate-ii/",
        ),
        (
            "frequency_most_frequent.py",
            "LeetCode #1838",
            "Frequency of the Most Frequent Element",
            "https://leetcode.com/problems/frequency-of-the-most-frequent-element/",
        ),
        (
            "subarrays_k_different.py",
            "LeetCode #992",
            "Subarrays with K Different Integers",
            "https://leetcode.com/problems/subarrays-with-k-different-integers/",
        ),
        (
            "count_subarrays_score.py",
            "LeetCode #2302",
            "Count Subarrays With Score Less Than K",
            "https://leetcode.com/problems/count-subarrays-with-score-less-than-k/",
        ),
    ],
    "merge_intervals": [
        ("merge_intervals.py", "LeetCode #56", "Merge Intervals", "https://leetcode.com/problems/merge-intervals/"),
        ("insert_interval.py", "LeetCode #57", "Insert Interval", "https://leetcode.com/problems/insert-interval/"),
        (
            "interval_intersections.py",
            "LeetCode #986",
            "Interval List Intersections",
            "https://leetcode.com/problems/interval-list-intersections/",
        ),
        (
            "employee_free_time.py",
            "LeetCode #759",
            "Employee Free Time",
            "https://leetcode.com/problems/employee-free-time/",
        ),
        ("count_days_without_meetings.py", "Custom Problem", "Count Days Without Meetings", "Custom Problem"),
        (
            "remove_covered_intervals.py",
            "LeetCode #1288",
            "Remove Covered Intervals",
            "https://leetcode.com/problems/remove-covered-intervals/",
        ),
        ("meeting_rooms_ii.py", "LeetCode #253", "Meeting Rooms II", "https://leetcode.com/problems/meeting-rooms-ii/"),
    ],
    "in_place_linked_list": [
        (
            "reverse_linked_list.py",
            "LeetCode #206",
            "Reverse Linked List",
            "https://leetcode.com/problems/reverse-linked-list/",
        ),
        (
            "reverse_nodes_k_group.py",
            "LeetCode #25",
            "Reverse Nodes in k-Group",
            "https://leetcode.com/problems/reverse-nodes-in-k-group/",
        ),
        (
            "reverse_linked_list_ii.py",
            "LeetCode #92",
            "Reverse Linked List II",
            "https://leetcode.com/problems/reverse-linked-list-ii/",
        ),
        ("reorder_list.py", "LeetCode #143", "Reorder List", "https://leetcode.com/problems/reorder-list/"),
        (
            "swapping_nodes.py",
            "LeetCode #1721",
            "Swapping Nodes in a Linked List",
            "https://leetcode.com/problems/swapping-nodes-in-a-linked-list/",
        ),
        (
            "reverse_even_groups.py",
            "LeetCode #2074",
            "Reverse Nodes in Even Length Groups",
            "https://leetcode.com/problems/reverse-nodes-in-even-length-groups/",
        ),
        (
            "remove_duplicates.py",
            "LeetCode #83",
            "Remove Duplicates from Sorted List",
            "https://leetcode.com/problems/remove-duplicates-from-sorted-list/",
        ),
        (
            "remove_elements.py",
            "LeetCode #203",
            "Remove Linked List Elements",
            "https://leetcode.com/problems/remove-linked-list-elements/",
        ),
        (
            "split_list_parts.py",
            "LeetCode #725",
            "Split Linked List in Parts",
            "https://leetcode.com/problems/split-linked-list-in-parts/",
        ),
        (
            "delete_n_after_m.py",
            "LeetCode #1474",
            "Delete N Nodes After M Nodes",
            "https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/",
        ),
        (
            "insert_circular_list.py",
            "LeetCode #708",
            "Insert into Sorted Circular Linked List",
            "https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/",
        ),
        (
            "swap_nodes_pairs.py",
            "LeetCode #24",
            "Swap Nodes in Pairs",
            "https://leetcode.com/problems/swap-nodes-in-pairs/",
        ),
    ],
    "heaps": [
        ("ipo.py", "LeetCode #502", "IPO", "https://leetcode.com/problems/ipo/"),
        (
            "find_median_data_stream.py",
            "LeetCode #295",
            "Find Median from Data Stream",
            "https://leetcode.com/problems/find-median-from-data-stream/",
        ),
        (
            "sliding_window_median.py",
            "LeetCode #480",
            "Sliding Window Median",
            "https://leetcode.com/problems/sliding-window-median/",
        ),
        ("schedule_tasks_machines.py", "Custom Problem", "Schedule Tasks on Minimum Machines", "Custom Problem"),
        (
            "meeting_rooms_iii.py",
            "LeetCode #2402",
            "Meeting Rooms III",
            "https://leetcode.com/problems/meeting-rooms-iii/",
        ),
        (
            "largest_number_digit_swaps.py",
            "LeetCode #2231",
            "Largest Number After Digit Swaps by Parity",
            "https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/",
        ),
        (
            "find_right_interval.py",
            "LeetCode #436",
            "Find Right Interval",
            "https://leetcode.com/problems/find-right-interval/",
        ),
        (
            "min_cost_connect_sticks.py",
            "LeetCode #1167",
            "Minimum Cost to Connect Sticks",
            "https://leetcode.com/problems/minimum-cost-to-connect-sticks/",
        ),
        (
            "longest_happy_string.py",
            "LeetCode #1405",
            "Longest Happy String",
            "https://leetcode.com/problems/longest-happy-string/",
        ),
        (
            "max_average_pass_ratio.py",
            "LeetCode #1792",
            "Maximum Average Pass Ratio",
            "https://leetcode.com/problems/maximum-average-pass-ratio/",
        ),
        (
            "smallest_unoccupied_chair.py",
            "LeetCode #1942",
            "The Number of the Smallest Unoccupied Chair",
            "https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/",
        ),
    ],
    "k_way_merge": [
        (
            "merge_sorted_array.py",
            "LeetCode #88",
            "Merge Sorted Array",
            "https://leetcode.com/problems/merge-sorted-array/",
        ),
        ("kth_smallest_m_lists.py", "Custom Problem", "Kth Smallest Number in M Sorted Lists", "Custom Problem"),
        (
            "k_pairs_smallest_sums.py",
            "LeetCode #373",
            "Find K Pairs with Smallest Sums",
            "https://leetcode.com/problems/find-k-pairs-with-smallest-sums/",
        ),
        (
            "merge_k_sorted_lists.py",
            "LeetCode #23",
            "Merge K Sorted Lists",
            "https://leetcode.com/problems/merge-k-sorted-lists/",
        ),
        (
            "kth_smallest_sorted_matrix.py",
            "LeetCode #378",
            "Kth Smallest Element in a Sorted Matrix",
            "https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/",
        ),
        (
            "kth_smallest_prime_fraction.py",
            "LeetCode #786",
            "Kth Smallest Prime Fraction",
            "https://leetcode.com/problems/k-th-smallest-prime-fraction/",
        ),
        (
            "super_ugly_number.py",
            "LeetCode #313",
            "Super Ugly Number",
            "https://leetcode.com/problems/super-ugly-number/",
        ),
    ],
    "top_k_elements": [
        (
            "kth_largest_stream.py",
            "LeetCode #703",
            "Kth Largest Element in a Stream",
            "https://leetcode.com/problems/kth-largest-element-in-a-stream/",
        ),
        (
            "reorganize_string.py",
            "LeetCode #767",
            "Reorganize String",
            "https://leetcode.com/problems/reorganize-string/",
        ),
        (
            "k_closest_points.py",
            "LeetCode #973",
            "K Closest Points to Origin",
            "https://leetcode.com/problems/k-closest-points-to-origin/",
        ),
        (
            "top_k_frequent.py",
            "LeetCode #347",
            "Top K Frequent Elements",
            "https://leetcode.com/problems/top-k-frequent-elements/",
        ),
        (
            "kth_largest_array.py",
            "LeetCode #215",
            "Kth Largest Element in an Array",
            "https://leetcode.com/problems/kth-largest-element-in-an-array/",
        ),
        (
            "third_maximum.py",
            "LeetCode #414",
            "Third Maximum Number",
            "https://leetcode.com/problems/third-maximum-number/",
        ),
        (
            "subsequence_k_largest_sum.py",
            "LeetCode #2099",
            "Find Subsequence of Length K with the Largest Sum",
            "https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/",
        ),
        (
            "min_cost_hire_k_workers.py",
            "LeetCode #857",
            "Minimum Cost to Hire K Workers",
            "https://leetcode.com/problems/minimum-cost-to-hire-k-workers/",
        ),
    ],
    "modified_binary_search": [
        ("binary_search.py", "LeetCode #704", "Binary Search", "https://leetcode.com/problems/binary-search/"),
        (
            "search_rotated_array.py",
            "LeetCode #33",
            "Search in Rotated Sorted Array",
            "https://leetcode.com/problems/search-in-rotated-sorted-array/",
        ),
        (
            "first_bad_version.py",
            "LeetCode #278",
            "First Bad Version",
            "https://leetcode.com/problems/first-bad-version/",
        ),
        (
            "random_pick_weight.py",
            "LeetCode #528",
            "Random Pick with Weight",
            "https://leetcode.com/problems/random-pick-with-weight/",
        ),
        (
            "find_k_closest.py",
            "LeetCode #658",
            "Find K Closest Elements",
            "https://leetcode.com/problems/find-k-closest-elements/",
        ),
        (
            "single_element_sorted.py",
            "LeetCode #540",
            "Single Element in a Sorted Array",
            "https://leetcode.com/problems/single-element-in-a-sorted-array/",
        ),
        (
            "max_value_bounded_array.py",
            "LeetCode #1802",
            "Maximum Value at a Given Index in a Bounded Array",
            "https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/",
        ),
    ],
    "subsets": [
        ("subsets.py", "LeetCode #78", "Subsets", "https://leetcode.com/problems/subsets/"),
        ("permutations.py", "LeetCode #46", "Permutations", "https://leetcode.com/problems/permutations/"),
        (
            "letter_combinations.py",
            "LeetCode #17",
            "Letter Combinations of a Phone Number",
            "https://leetcode.com/problems/letter-combinations-of-a-phone-number/",
        ),
        (
            "generate_parentheses.py",
            "LeetCode #22",
            "Generate Parentheses",
            "https://leetcode.com/problems/generate-parentheses/",
        ),
        (
            "letter_case_permutation.py",
            "LeetCode #784",
            "Letter Case Permutation",
            "https://leetcode.com/problems/letter-case-permutation/",
        ),
        (
            "letter_tile_possibilities.py",
            "LeetCode #1079",
            "Letter Tile Possibilities",
            "https://leetcode.com/problems/letter-tile-possibilities/",
        ),
        ("find_k_sum_subsets.py", "Custom Problem", "Find K-Sum Subsets", "Custom Problem"),
    ],
    "greedy": [
        ("jump_game.py", "LeetCode #55", "Jump Game", "https://leetcode.com/problems/jump-game/"),
        (
            "boats_save_people.py",
            "LeetCode #881",
            "Boats to Save People",
            "https://leetcode.com/problems/boats-to-save-people/",
        ),
        ("gas_station.py", "LeetCode #134", "Gas Station", "https://leetcode.com/problems/gas-station/"),
        (
            "two_city_scheduling.py",
            "LeetCode #1029",
            "Two City Scheduling",
            "https://leetcode.com/problems/two-city-scheduling/",
        ),
        (
            "min_refueling_stops.py",
            "LeetCode #871",
            "Minimum Number of Refueling Stops",
            "https://leetcode.com/problems/minimum-number-of-refueling-stops/",
        ),
        (
            "largest_palindromic_number.py",
            "LeetCode #2384",
            "Largest Palindromic Number",
            "https://leetcode.com/problems/largest-palindromic-number/",
        ),
        ("assign_cookies.py", "LeetCode #455", "Assign Cookies", "https://leetcode.com/problems/assign-cookies/"),
    ],
    "backtracking": [
        ("n_queens.py", "LeetCode #51", "N-Queens", "https://leetcode.com/problems/n-queens/"),
        ("word_search.py", "LeetCode #79", "Word Search", "https://leetcode.com/problems/word-search/"),
        ("sudoku_solver.py", "LeetCode #37", "Sudoku Solver", "https://leetcode.com/problems/sudoku-solver/"),
        ("combination_sum.py", "LeetCode #39", "Combination Sum", "https://leetcode.com/problems/combination-sum/"),
        (
            "palindrome_partitioning.py",
            "LeetCode #131",
            "Palindrome Partitioning",
            "https://leetcode.com/problems/palindrome-partitioning/",
        ),
        ("n_queens_ii.py", "LeetCode #52", "N-Queens II", "https://leetcode.com/problems/n-queens-ii/"),
        (
            "combination_sum_ii.py",
            "LeetCode #40",
            "Combination Sum II",
            "https://leetcode.com/problems/combination-sum-ii/",
        ),
        (
            "combination_sum_iii.py",
            "LeetCode #216",
            "Combination Sum III",
            "https://leetcode.com/problems/combination-sum-iii/",
        ),
        (
            "factor_combinations.py",
            "LeetCode #254",
            "Factor Combinations",
            "https://leetcode.com/problems/factor-combinations/",
        ),
        (
            "split_string_palindrome.py",
            "LeetCode #1593",
            "Split a String Into the Max Number of Unique Substrings",
            "https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/",
        ),
        (
            "maximum_compatibility_score.py",
            "LeetCode #1947",
            "Maximum Compatibility Score Sum",
            "https://leetcode.com/problems/maximum-compatibility-score-sum/",
        ),
        ("flood_fill.py", "LeetCode #733", "Flood Fill", "https://leetcode.com/problems/flood-fill/"),
        (
            "count_number_text_words.py",
            "LeetCode #996",
            "Number of Squareful Arrays",
            "https://leetcode.com/problems/number-of-squareful-arrays/",
        ),
    ],
    "dynamic_programming": [
        ("fibonacci_number.py", "LeetCode #509", "Fibonacci Number", "https://leetcode.com/problems/fibonacci-number/"),
        ("climbing_stairs.py", "LeetCode #70", "Climbing Stairs", "https://leetcode.com/problems/climbing-stairs/"),
        (
            "n_tribonacci.py",
            "LeetCode #1137",
            "N-th Tribonacci Number",
            "https://leetcode.com/problems/n-th-tribonacci-number/",
        ),
        ("house_robber.py", "LeetCode #198", "House Robber", "https://leetcode.com/problems/house-robber/"),
        ("house_robber_ii.py", "LeetCode #213", "House Robber II", "https://leetcode.com/problems/house-robber-ii/"),
        ("word_break.py", "LeetCode #139", "Word Break", "https://leetcode.com/problems/word-break/"),
        ("coin_change.py", "LeetCode #322", "Coin Change", "https://leetcode.com/problems/coin-change/"),
        (
            "maximum_product_subarray.py",
            "LeetCode #152",
            "Maximum Product Subarray",
            "https://leetcode.com/problems/maximum-product-subarray/",
        ),
        (
            "longest_palindromic_substring.py",
            "LeetCode #5",
            "Longest Palindromic Substring",
            "https://leetcode.com/problems/longest-palindromic-substring/",
        ),
        (
            "palindromic_substrings.py",
            "LeetCode #647",
            "Palindromic Substrings",
            "https://leetcode.com/problems/palindromic-substrings/",
        ),
        (
            "longest_palindromic_subsequence.py",
            "LeetCode #516",
            "Longest Palindromic Subsequence",
            "https://leetcode.com/problems/longest-palindromic-subsequence/",
        ),
        (
            "longest_common_subsequence.py",
            "LeetCode #1143",
            "Longest Common Subsequence",
            "https://leetcode.com/problems/longest-common-subsequence/",
        ),
        (
            "min_cost_climbing_stairs.py",
            "LeetCode #746",
            "Min Cost Climbing Stairs",
            "https://leetcode.com/problems/min-cost-climbing-stairs/",
        ),
        (
            "maximum_alternating_subsequence_sum.py",
            "LeetCode #1911",
            "Maximum Alternating Subsequence Sum",
            "https://leetcode.com/problems/maximum-alternating-subsequence-sum/",
        ),
        (
            "partition_equal_subset_sum.py",
            "LeetCode #416",
            "Partition Equal Subset Sum",
            "https://leetcode.com/problems/partition-equal-subset-sum/",
        ),
    ],
    "cyclic_sort": [
        ("cyclic_sort.py", "Custom Problem", "Cyclic Sort", "Custom Problem"),
        ("find_missing_number.py", "LeetCode #268", "Missing Number", "https://leetcode.com/problems/missing-number/"),
        (
            "find_duplicate_number.py",
            "LeetCode #287",
            "Find the Duplicate Number",
            "https://leetcode.com/problems/find-the-duplicate-number/",
        ),
        ("find_corrupt_nums.py", "LeetCode #645", "Set Mismatch", "https://leetcode.com/problems/set-mismatch/"),
        (
            "first_smallest_missing_positive.py",
            "LeetCode #41",
            "First Missing Positive",
            "https://leetcode.com/problems/first-missing-positive/",
        ),
        (
            "find_k_missing_positive.py",
            "LeetCode #1539",
            "Kth Missing Positive Number",
            "https://leetcode.com/problems/kth-missing-positive-number/",
        ),
    ],
    "topological_sort": [
        (
            "compilation_order.py",
            "LeetCode #210",
            "Course Schedule II",
            "https://leetcode.com/problems/course-schedule-ii/",
        ),
        ("alien_dictionary.py", "LeetCode #269", "Alien Dictionary", "https://leetcode.com/problems/alien-dictionary/"),
        (
            "find_all_recipes.py",
            "LeetCode #2115",
            "Find All Possible Recipes from Given Supplies",
            "https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/",
        ),
        (
            "course_schedule_ii.py",
            "LeetCode #210",
            "Course Schedule II",
            "https://leetcode.com/problems/course-schedule-ii/",
        ),
        ("course_schedule.py", "LeetCode #207", "Course Schedule", "https://leetcode.com/problems/course-schedule/"),
    ],
    "matrices": [
        (
            "set_matrix_zeros.py",
            "LeetCode #73",
            "Set Matrix Zeroes",
            "https://leetcode.com/problems/set-matrix-zeroes/",
        ),
        ("rotate_image.py", "LeetCode #48", "Rotate Image", "https://leetcode.com/problems/rotate-image/"),
        ("spiral_matrix.py", "LeetCode #54", "Spiral Matrix", "https://leetcode.com/problems/spiral-matrix/"),
        (
            "where_will_ball_fall.py",
            "LeetCode #1706",
            "Where Will the Ball Fall",
            "https://leetcode.com/problems/where-will-the-ball-fall/",
        ),
    ],
    "stacks": [
        (
            "valid_parentheses.py",
            "LeetCode #20",
            "Valid Parentheses",
            "https://leetcode.com/problems/valid-parentheses/",
        ),
        (
            "longest_valid_parentheses.py",
            "LeetCode #32",
            "Longest Valid Parentheses",
            "https://leetcode.com/problems/longest-valid-parentheses/",
        ),
        (
            "remove_duplicates.py",
            "LeetCode #1047",
            "Remove All Adjacent Duplicates In String",
            "https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/",
        ),
        (
            "min_remove_valid_parentheses.py",
            "LeetCode #1249",
            "Minimum Remove to Make Valid Parentheses",
            "https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/",
        ),
        (
            "exclusive_time_functions.py",
            "LeetCode #636",
            "Exclusive Time of Functions",
            "https://leetcode.com/problems/exclusive-time-of-functions/",
        ),
        ("basic_calculator.py", "LeetCode #224", "Basic Calculator", "https://leetcode.com/problems/basic-calculator/"),
        ("remove_k_digits.py", "LeetCode #402", "Remove K Digits", "https://leetcode.com/problems/remove-k-digits/"),
        (
            "daily_temperatures.py",
            "LeetCode #739",
            "Daily Temperatures",
            "https://leetcode.com/problems/daily-temperatures/",
        ),
        (
            "next_greater_element.py",
            "LeetCode #496",
            "Next Greater Element I",
            "https://leetcode.com/problems/next-greater-element-i/",
        ),
    ],
    "graphs": [
        (
            "find_if_path_exists.py",
            "LeetCode #1971",
            "Find if Path Exists in Graph",
            "https://leetcode.com/problems/find-if-path-exists-in-graph/",
        ),
        (
            "number_of_islands.py",
            "LeetCode #200",
            "Number of Islands",
            "https://leetcode.com/problems/number-of-islands/",
        ),
        ("clone_graph.py", "LeetCode #133", "Clone Graph", "https://leetcode.com/problems/clone-graph/"),
        (
            "all_paths_source_target.py",
            "LeetCode #797",
            "All Paths From Source to Target",
            "https://leetcode.com/problems/all-paths-from-source-to-target/",
        ),
        ("word_ladder.py", "LeetCode #127", "Word Ladder", "https://leetcode.com/problems/word-ladder/"),
        (
            "number_connected_components.py",
            "LeetCode #323",
            "Number of Connected Components in an Undirected Graph",
            "https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/",
        ),
        (
            "minimum_vertices_reach_nodes.py",
            "LeetCode #1557",
            "Minimum Number of Vertices to Reach All Nodes",
            "https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/",
        ),
        (
            "find_town_judge.py",
            "LeetCode #997",
            "Find the Town Judge",
            "https://leetcode.com/problems/find-the-town-judge/",
        ),
        (
            "regions_cut_slashes.py",
            "LeetCode #959",
            "Regions Cut By Slashes",
            "https://leetcode.com/problems/regions-cut-by-slashes/",
        ),
    ],
    "tree_depth_first_search": [
        (
            "binary_tree_paths.py",
            "LeetCode #257",
            "Binary Tree Paths",
            "https://leetcode.com/problems/binary-tree-paths/",
        ),
        ("same_tree.py", "LeetCode #100", "Same Tree", "https://leetcode.com/problems/same-tree/"),
        (
            "invert_binary_tree.py",
            "LeetCode #226",
            "Invert Binary Tree",
            "https://leetcode.com/problems/invert-binary-tree/",
        ),
        (
            "binary_tree_diameter.py",
            "LeetCode #543",
            "Diameter of Binary Tree",
            "https://leetcode.com/problems/diameter-of-binary-tree/",
        ),
        (
            "serialize_deserialize_binary_tree.py",
            "LeetCode #297",
            "Serialize and Deserialize Binary Tree",
            "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/",
        ),
        ("mirror_binary_tree.py", "Custom Problem", "Mirror Binary Tree", "Custom Problem"),
        (
            "binary_tree_max_path_sum.py",
            "LeetCode #124",
            "Binary Tree Maximum Path Sum",
            "https://leetcode.com/problems/binary-tree-maximum-path-sum/",
        ),
        (
            "convert_sorted_array_bst.py",
            "LeetCode #108",
            "Convert Sorted Array to Binary Search Tree",
            "https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/",
        ),
        (
            "build_tree_preorder_inorder.py",
            "LeetCode #105",
            "Construct Binary Tree from Preorder and Inorder Traversal",
            "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/",
        ),
        (
            "validate_binary_search_tree.py",
            "LeetCode #98",
            "Validate Binary Search Tree",
            "https://leetcode.com/problems/validate-binary-search-tree/",
        ),
        (
            "kth_smallest_element_bst.py",
            "LeetCode #230",
            "Kth Smallest Element in a BST",
            "https://leetcode.com/problems/kth-smallest-element-in-a-bst/",
        ),
        (
            "lowest_common_ancestor_bst.py",
            "LeetCode #235",
            "Lowest Common Ancestor of a Binary Search Tree",
            "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/",
        ),
        (
            "lowest_common_ancestor_bt.py",
            "LeetCode #236",
            "Lowest Common Ancestor of a Binary Tree",
            "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/",
        ),
        (
            "sum_path_numbers.py",
            "LeetCode #129",
            "Sum Root to Leaf Numbers",
            "https://leetcode.com/problems/sum-root-to-leaf-numbers/",
        ),
        (
            "sum_root_leaf_numbers.py",
            "LeetCode #129",
            "Sum Root to Leaf Numbers",
            "https://leetcode.com/problems/sum-root-to-leaf-numbers/",
        ),
        (
            "binary_tree_right_side_view.py",
            "LeetCode #199",
            "Binary Tree Right Side View",
            "https://leetcode.com/problems/binary-tree-right-side-view/",
        ),
    ],
    "tree_breadth_first_search": [
        (
            "binary_tree_level_order.py",
            "LeetCode #102",
            "Binary Tree Level Order Traversal",
            "https://leetcode.com/problems/binary-tree-level-order-traversal/",
        ),
        (
            "binary_tree_level_order_ii.py",
            "LeetCode #107",
            "Binary Tree Level Order Traversal II",
            "https://leetcode.com/problems/binary-tree-level-order-traversal-ii/",
        ),
        (
            "binary_tree_zigzag_level_order.py",
            "LeetCode #103",
            "Binary Tree Zigzag Level Order Traversal",
            "https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/",
        ),
        (
            "populate_next_right_pointers.py",
            "LeetCode #116",
            "Populating Next Right Pointers in Each Node",
            "https://leetcode.com/problems/populating-next-right-pointers-in-each-node/",
        ),
        (
            "populate_next_right_pointers_ii.py",
            "LeetCode #117",
            "Populating Next Right Pointers in Each Node II",
            "https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/",
        ),
        (
            "minimum_depth_binary_tree.py",
            "LeetCode #111",
            "Minimum Depth of Binary Tree",
            "https://leetcode.com/problems/minimum-depth-of-binary-tree/",
        ),
        (
            "level_averages_binary_tree.py",
            "LeetCode #637",
            "Average of Levels in Binary Tree",
            "https://leetcode.com/problems/average-of-levels-in-binary-tree/",
        ),
        (
            "minimum_depth_of_binary_tree.py",
            "LeetCode #111",
            "Minimum Depth of Binary Tree",
            "https://leetcode.com/problems/minimum-depth-of-binary-tree/",
        ),
        ("word_ladder.py", "LeetCode #127", "Word Ladder", "https://leetcode.com/problems/word-ladder/"),
        ("connect_all_siblings.py", "Custom Problem", "Connect All Level Order Siblings", "Custom Problem"),
    ],
    "trie": [
        (
            "implement_trie.py",
            "LeetCode #208",
            "Implement Trie (Prefix Tree)",
            "https://leetcode.com/problems/implement-trie-prefix-tree/",
        ),
        (
            "index_pairs_string.py",
            "LeetCode #1065",
            "Index Pairs of a String",
            "https://leetcode.com/problems/index-pairs-of-a-string/",
        ),
        (
            "design_add_search_words.py",
            "LeetCode #211",
            "Design Add and Search Words Data Structure",
            "https://leetcode.com/problems/design-add-and-search-words-data-structure/",
        ),
        (
            "extra_characters_string.py",
            "LeetCode #2707",
            "Extra Characters in a String",
            "https://leetcode.com/problems/extra-characters-in-a-string/",
        ),
        (
            "search_suggestions_system.py",
            "LeetCode #1268",
            "Search Suggestions System",
            "https://leetcode.com/problems/search-suggestions-system/",
        ),
        ("replace_words.py", "LeetCode #648", "Replace Words", "https://leetcode.com/problems/replace-words/"),
        (
            "implement_magic_dictionary.py",
            "LeetCode #676",
            "Implement Magic Dictionary",
            "https://leetcode.com/problems/implement-magic-dictionary/",
        ),
        ("word_search_ii.py", "LeetCode #212", "Word Search II", "https://leetcode.com/problems/word-search-ii/"),
    ],
    "hash_maps": [
        ("design_hashmap.py", "LeetCode #706", "Design HashMap", "https://leetcode.com/problems/design-hashmap/"),
        (
            "fraction_recurring_decimal.py",
            "LeetCode #166",
            "Fraction to Recurring Decimal",
            "https://leetcode.com/problems/fraction-to-recurring-decimal/",
        ),
        (
            "max_frequency_stack.py",
            "LeetCode #895",
            "Maximum Frequency Stack",
            "https://leetcode.com/problems/maximum-frequency-stack/",
        ),
        (
            "insert_delete_getrandom.py",
            "LeetCode #380",
            "Insert Delete GetRandom O(1)",
            "https://leetcode.com/problems/insert-delete-getrandom-o1/",
        ),
        (
            "time_based_key_value.py",
            "LeetCode #981",
            "Time Based Key-Value Store",
            "https://leetcode.com/problems/time-based-key-value-store/",
        ),
        (
            "logger_rate_limiter.py",
            "LeetCode #359",
            "Logger Rate Limiter",
            "https://leetcode.com/problems/logger-rate-limiter/",
        ),
        (
            "next_greater_element_i.py",
            "LeetCode #496",
            "Next Greater Element I",
            "https://leetcode.com/problems/next-greater-element-i/",
        ),
        (
            "isomorphic_strings.py",
            "LeetCode #205",
            "Isomorphic Strings",
            "https://leetcode.com/problems/isomorphic-strings/",
        ),
        (
            "longest_palindrome.py",
            "LeetCode #409",
            "Longest Palindrome",
            "https://leetcode.com/problems/longest-palindrome/",
        ),
        ("ransom_note.py", "LeetCode #383", "Ransom Note", "https://leetcode.com/problems/ransom-note/"),
    ],
    "knowing_what_to_track": [
        (
            "palindrome_permutation.py",
            "LeetCode #266",
            "Palindrome Permutation",
            "https://leetcode.com/problems/palindrome-permutation/",
        ),
        ("valid_anagram.py", "LeetCode #242", "Valid Anagram", "https://leetcode.com/problems/valid-anagram/"),
        (
            "design_tic_tac_toe.py",
            "LeetCode #348",
            "Design Tic-Tac-Toe",
            "https://leetcode.com/problems/design-tic-tac-toe/",
        ),
        ("group_anagrams.py", "LeetCode #49", "Group Anagrams", "https://leetcode.com/problems/group-anagrams/"),
        (
            "maximum_frequency_stack.py",
            "LeetCode #895",
            "Maximum Frequency Stack",
            "https://leetcode.com/problems/maximum-frequency-stack/",
        ),
        (
            "first_unique_character.py",
            "LeetCode #387",
            "First Unique Character in a String",
            "https://leetcode.com/problems/first-unique-character-in-a-string/",
        ),
        (
            "find_all_anagrams.py",
            "LeetCode #438",
            "Find All Anagrams in a String",
            "https://leetcode.com/problems/find-all-anagrams-in-a-string/",
        ),
        (
            "longest_substring_k_distinct.py",
            "LeetCode #340",
            "Longest Substring with At Most K Distinct Characters",
            "https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/",
        ),
        (
            "fraction_recurring_decimal.py",
            "LeetCode #166",
            "Fraction to Recurring Decimal",
            "https://leetcode.com/problems/fraction-to-recurring-decimal/",
        ),
    ],
    "union_find": [
        (
            "redundant_connection.py",
            "LeetCode #684",
            "Redundant Connection",
            "https://leetcode.com/problems/redundant-connection/",
        ),
        (
            "number_of_islands.py",
            "LeetCode #200",
            "Number of Islands",
            "https://leetcode.com/problems/number-of-islands/",
        ),
        (
            "last_stone_weight.py",
            "LeetCode #1046",
            "Last Stone Weight",
            "https://leetcode.com/problems/last-stone-weight/",
        ),
        (
            "minimize_malware_spread.py",
            "LeetCode #924",
            "Minimize Malware Spread",
            "https://leetcode.com/problems/minimize-malware-spread/",
        ),
        (
            "optimize_water_distribution.py",
            "LeetCode #1168",
            "Optimize Water Distribution in a Village",
            "https://leetcode.com/problems/optimize-water-distribution-in-a-village/",
        ),
        ("accounts_merge.py", "LeetCode #721", "Accounts Merge", "https://leetcode.com/problems/accounts-merge/"),
    ],
    "custom_data_structures": [
        ("snapshot_array.py", "LeetCode #1146", "Snapshot Array", "https://leetcode.com/problems/snapshot-array/"),
        (
            "time_based_key_value_store.py",
            "LeetCode #981",
            "Time Based Key-Value Store",
            "https://leetcode.com/problems/time-based-key-value-store/",
        ),
        (
            "insert_delete_getrandom.py",
            "LeetCode #380",
            "Insert Delete GetRandom O(1)",
            "https://leetcode.com/problems/insert-delete-getrandom-o1/",
        ),
        ("lru_cache.py", "LeetCode #146", "LRU Cache", "https://leetcode.com/problems/lru-cache/"),
        (
            "serialize_deserialize_binary_tree.py",
            "LeetCode #297",
            "Serialize and Deserialize Binary Tree",
            "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/",
        ),
        (
            "find_median_data_stream.py",
            "LeetCode #295",
            "Find Median from Data Stream",
            "https://leetcode.com/problems/find-median-from-data-stream/",
        ),
        (
            "implement_queue_using_stacks.py",
            "LeetCode #232",
            "Implement Queue using Stacks",
            "https://leetcode.com/problems/implement-queue-using-stacks/",
        ),
    ],
    "bitwise_manipulation": [
        (
            "find_difference.py",
            "LeetCode #389",
            "Find the Difference",
            "https://leetcode.com/problems/find-the-difference/",
        ),
        (
            "complement_base_10.py",
            "LeetCode #1009",
            "Complement of Base 10 Integer",
            "https://leetcode.com/problems/complement-of-base-10-integer/",
        ),
        ("flipping_image.py", "LeetCode #832", "Flipping an Image", "https://leetcode.com/problems/flipping-an-image/"),
        ("single_number.py", "LeetCode #136", "Single Number", "https://leetcode.com/problems/single-number/"),
        (
            "two_single_numbers.py",
            "LeetCode #260",
            "Single Number III",
            "https://leetcode.com/problems/single-number-iii/",
        ),
        (
            "find_duplicate.py",
            "LeetCode #287",
            "Find the Duplicate Number",
            "https://leetcode.com/problems/find-the-duplicate-number/",
        ),
        ("reverse_bits.py", "LeetCode #190", "Reverse Bits", "https://leetcode.com/problems/reverse-bits/"),
        ("swap_odd_even_bits.py", "Custom Problem", "Swap Odd and Even Bits", "Custom Problem"),
    ],
}


def generate_problem_file(topic_dir, filename, leetcode_num, problem_name, url):
    """Generate a problem file with standard template."""

    file_path = os.path.join(topic_dir, filename)

    # Create function name from filename
    func_name = filename.replace(".py", "").replace("-", "_")

    # Create test function name
    test_func_name = f"test_{func_name}"

    content = f'''"""
{leetcode_num}: {problem_name}
{url}

Problem Statement:
[Add problem statement here]

Example 1:
Input: [Add example]
Output: [Add example]

Example 2:
Input: [Add example]
Output: [Add example]

Constraints:
[Add constraints here]
"""


def {func_name}():
    """
    [Add description here]
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    # Replace this placeholder return statement with your code
    return None


def {test_func_name}():
    """Test cases for {problem_name.lower()} function."""
    test_inputs = [
        # Add test cases here
        # (input, expected_output),
    ]

    for i, (input_data, expected_output) in enumerate(test_inputs):
        result = {func_name}(input_data)
        print(f"Test {{i + 1}} - Input: {{input_data}}, Output: {{result}}")
        assert result == expected_output, f"Test case {{i + 1}} failed"

    print("All test cases passed!")


if __name__ == "__main__":
    {test_func_name}()
'''

    with open(file_path, "w") as f:
        f.write(content)

    print(f"Created: {file_path}")


def main():
    """Generate all missing problem files."""
    base_path = "/Users/haphan/dsa_learn"

    for topic, problems in problems_structure.items():
        topic_dir = os.path.join(base_path, topic)

        # Create directory if it doesn't exist
        if not os.path.exists(topic_dir):
            os.makedirs(topic_dir)
            print(f"Created directory: {topic_dir}")

        # Generate files for each problem
        for filename, leetcode_num, problem_name, url in problems:
            file_path = os.path.join(topic_dir, filename)
            if not os.path.exists(file_path):
                generate_problem_file(topic_dir, filename, leetcode_num, problem_name, url)


if __name__ == "__main__":
    main()
