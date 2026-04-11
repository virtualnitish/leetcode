# LeetCode Jadia

Personal repository for LeetCode solutions, reusable patterns, and foundation notes. The `python/` directory holds problem-wise writeups, while `foundation/` collects algorithm templates and deeper theory notes.

## Repository Layout

- `python/`: LeetCode problem notes and Python solutions.
- `foundation/`: Core algorithm notes for graphs, trees, DP, sorting, search, heaps, matrices, and templates.
- `foundation/deep-dive/`: Longer topic-specific explanations.
- `anki_revision/`: Revision material and spaced-repetition helpers.
- `tools/`: Utility scripts for filename generation and README management.
- `Makefile`: Entry point for workflow automation.

## What Is In Here

- Solved problems with explanations, code, and sometimes visual walkthroughs.
- Reusable templates for BFS, DFS, heaps, binary search, topological sort, and DP.
- Notes on implementation details that are easy to forget during timed problem solving.

## Python Cheat Sheet

These are Python patterns already used in this repo and worth remembering in interviews.

### Sorting

```python
sorted_word = ''.join(sorted(word))
intervals.sort(key=lambda x: x.start)
events.sort(key=lambda x: (x[0], x[1]))
```

- Use `sorted(...)` when you need a new sorted value.
- Use `.sort(...)` when in-place sorting is fine.
- Use `key=lambda ...` for custom ordering.
- Repo examples:
  - [python/0049.group_anagrams.md](python/0049.group_anagrams.md)
  - [python/0252.meeting_rooms.md](python/0252.meeting_rooms.md)
  - [python/0253.meeting_rooms_ii.md](python/0253.meeting_rooms_ii.md)

### Hash Maps And Counting

```python
num_index = {}
freq = defaultdict(int)
inorder_map = {val: idx for idx, val in enumerate(inorder)}
```

- Plain `dict` works for lookups like Two Sum.
- `defaultdict(int)` is convenient for frequency counting.
- Dictionary comprehensions are useful for index maps and last-occurrence maps.
- Repo examples:
  - [python/0001.two_sum.md](python/0001.two_sum.md)
  - [python/0347.top_k_frequent_elements.md](python/0347.top_k_frequent_elements.md)
  - [python/0105-construct-binary-tree-from-preorder-and-inorder-traversal.md](python/0105-construct-binary-tree-from-preorder-and-inorder-traversal.md)
  - [python/0763.partition_lables.md](python/0763.partition_lables.md)

### `enumerate` And `zip`

```python
for i, num in enumerate(nums):
for w1, w2 in zip(words, words[1:]):
for c1, c2 in zip(w1, w2):
```

- `enumerate` gives index and value together.
- `zip(words, words[1:])` is a clean way to compare adjacent elements.
- Nested `zip` is useful for first-difference comparisons between strings.
- Repo examples:
  - [python/0001.two_sum.md](python/0001.two_sum.md)
  - [python/0269.alien_dictionary.md](python/0269.alien_dictionary.md)

### Comprehensions

```python
in_degree = {ch: 0 for word in words for ch in word}
starts = sorted([i.start for i in intervals])
bucket = [[] for _ in range(len(nums) + 1)]
```

- Use list comprehensions for compact derived arrays.
- Use dict comprehensions to initialize maps from nested input.
- Prefer `[[] for _ in range(n)]` over `[[]] * n` when each sub-list must be distinct.
- Repo examples:
  - [python/0269.alien_dictionary.md](python/0269.alien_dictionary.md)
  - [python/0253.meeting_rooms_ii.md](python/0253.meeting_rooms_ii.md)
  - [python/0347.top_k_frequent_elements.md](python/0347.top_k_frequent_elements.md)

### Queue And BFS Helpers

```python
from collections import deque

queue = deque([root])
node = queue.popleft()
queue.append(node.left)
```

- `deque` is the standard queue for BFS.
- Use `popleft()` instead of `pop(0)` for `O(1)` queue operations.
- Repo examples:
  - [python/0297.serialize_and_deserialize_binary_tree.md](python/0297.serialize_and_deserialize_binary_tree.md)
  - [python/0104.maximum-depth-of-binary-tree.md](python/0104.maximum-depth-of-binary-tree.md)
  - [python/0200.number_of_islands.md](python/0200.number_of_islands.md)

### Heap / Priority Queue

```python
import heapq

heapq.heappush(min_heap, (count, num))
count, num = heapq.heappop(min_heap)
```

- Python `heapq` is a min-heap.
- Push tuples like `(priority, value)` when you need ordering by weight, count, or time.
- Repo examples:
  - [python/0347.top_k_frequent_elements.md](python/0347.top_k_frequent_elements.md)
  - [python/0253.meeting_rooms_ii.md](python/0253.meeting_rooms_ii.md)
  - [python/1584.min_cost_to_connect_all_points.md](python/1584.min_cost_to_connect_all_points.md)

### Strings

```python
return ','.join(res)
nodes = data.split(',')
result_str = ''.join(map(str, result[::-1]))
```

- `','.join(...)` is the standard way to serialize lists of strings.
- `.split(',')` is the inverse when parsing.
- `map(str, ...)` is handy when converting digits or values before joining.
- Repo examples:
  - [python/0297.serialize_and_deserialize_binary_tree.md](python/0297.serialize_and_deserialize_binary_tree.md)
  - [python/0043.multiply_strings.md](python/0043.multiply_strings.md)

### Useful Built-ins

```python
max_len = max(max_len, r - l + 1)
maxWordLength = max(map(len, wordSet)) if wordSet else 0
return max(robhouse(nums[1:]), robhouse(nums[:-1]))
```

- `max(...)` and `min(...)` are everywhere in sliding window, DP, greedy, and interval problems.
- `map(len, wordSet)` is a concise way to transform before aggregation.
- Slicing like `nums[1:]` and `nums[:-1]` is useful, but remember it creates copies.
- Repo examples:
  - [python/0424.longest_repeating_character_replacement.md](python/0424.longest_repeating_character_replacement.md)
  - [python/0139.word_break.md](python/0139.word_break.md)
  - [python/0213.house_robber_ii.md](python/0213.house_robber_ii.md)

### Iterators Instead Of Costly List Operations

```python
preorder_iter = iter(preorder)
root_val = next(preorder_iter)
```

- Prefer an iterator over repeated `pop(0)` on a list.
- This avoids linear-time shifts and keeps traversal code clean.
- Repo example:
  - [python/0105-construct-binary-tree-from-preorder-and-inorder-traversal.md](python/0105-construct-binary-tree-from-preorder-and-inorder-traversal.md)

## Solved Problems

| # | Title | Solution |
|---|-------|----------|
| 1 | Two Sum | [Solution](python/0001.two_sum.md) |
| 2 | Add Two Numbers | [Solution](python/0002.add_two_numbers.md) |
| 3 | Longest Substring Without Repeating Characters | [Solution](python/0003.longest_substring_without_repeating_characterrs.md) |
| 4 | Median of Two Sorted Arrays | [Solution](python/0004.median_of_two_sorted_arrays.md) |
| 5 | Longest Palindromic Substring | [Solution](python/0005.longest_palindrome_substring.md) |
| 7 | Reverse Integer | [Solution](python/0007.reverse_integer.md) |
| 9 | Palindrome Number | [Solution](python/0009.palindrome_number.md) |
| 11 | Container With Most Water | [Solution](python/0011.container_with_most_water.md) |
| 39 | Combination Sum | [Solution](python/0039.combination_sum.md) |
| 43 | Multiply Strings | [Solution](python/0043.multiply_strings.md) |
| 49 | Group Anagrams | [Solution](python/0049.group_anagrams.md) |
| 53 | Maximum Subarray | [Solution](python/0053.maximum_subarray.md) |
| 70 | Climbing Stairs | [Solution](python/0070.climbing_stairs.md) |
| 76 | Minimum Window Substring | [Solution](python/0076.minimum_window_substring.md) |
| 79 | Word Search | [Solution](python/0079.word_search.md) |
| 91 | Decode Ways | [Solution](python/0091.decode_ways.md) |
| 98 | Validate Binary Search Tree | [Solution](python/0098.validate_binary_search_tree.md) |
| 100 | Same Tree | [Solution](python/0100.same_tree.md) |
| 102 | Binary Tree Level Order Traversal | [Solution](python/0102.binary_tree_level_order_traversal.md) |
| 104 | Maximum Depth of Binary Tree | [Solution](python/0104.maximum-depth-of-binary-tree.md) |
| 105 | Construct Binary Tree from Preorder and Inorder Traversal | [Solution](python/0105-construct-binary-tree-from-preorder-and-inorder-traversal.md) |
| 124 | Binary Tree Maximum Path Sum | [Solution](python/0124.binary_tree_maximum_path_sum.md) |
| 128 | Longest Consecutive Sequence | [Solution](python/0128.longest_consecutive_sequence.md) |
| 133 | Clone Graph | [Solution](python/0133.clone_graph.md) |
| 139 | Word Break | [Solution](python/0139.word_break.md) |
| 152 | Maximum Product Subarray | [Solution](python/0152.maximum_product_subarray.md) |
| 198 | House Robber | [Solution](python/0198.house_robber.md) |
| 200 | Number of Islands | [Solution](python/0200.number_of_islands.md) |
| 207 | Course Schedule | [Solution](python/0207.course_schedule.md) |
| 213 | House Robber II | [Solution](python/0213.house_robber_ii.md) |
| 217 | Contains Duplicate | [Solution](python/0217.contains_duplicate.md) |
| 226 | Invert Binary Tree | [Solution](python/0226.invert_binary_tree.md) |
| 230 | Kth Smallest Element in a BST | [Solution](python/0230.kth_smallest_element_in_tree.md) |
| 235 | Lowest Common Ancestor of a Binary Search Tree | [Solution](python/0235.lowest_common_ancestor_of_binary_search_tree.md) |
| 252 | Meeting Rooms | [Solution](python/0252.meeting_rooms.md) |
| 253 | Meeting Rooms II | [Solution](python/0253.meeting_rooms_ii.md) |
| 261 | Graph Valid Tree | [Solution](python/0261.graph_valid_tree.md) |
| 269 | Alien Dictionary | [Solution](python/0269.alien_dictionary.md) |
| 297 | Serialize and Deserialize Binary Tree | [Solution](python/0297.serialize_and_deserialize_binary_tree.md) |
| 300 | Longest Increasing Subsequence | [Solution](python/0300.longest_increasing_subsequence.md) |
| 322 | Coin Change | [Solution](python/0322.coin_change.md) |
| 323 | Number of Connected Components in an Undirected Graph | [Solution](python/0323.number_of_connected_components_in_an_undirected_graph.md) |
| 347 | Top K Frequent Elements | [Solution](python/0347.top_k_frequent_elements.md) |
| 417 | Pacific Atlantic Water Flow | [Solution](python/0417.pacific_atlantic_water_flow.md) |
| 424 | Longest Repeating Character Replacement | [Solution](python/0424.longest_repeating_character_replacement.md) |
| 509 | Fibonacci number | [Solution](python/0509.fibonacci.md) |
| 572 | Subtree of Another Tree | [Solution](python/0572.subtree_of_another_tree.md) |
| 647 | Palindromic Substrings | [Solution](python/0647.palindromic_substrings.md) |
| 739 | Daily Temperatures | [Solution](python/0739.daily_temperatures.md) |
| 768 | Partition Lables | [Solution](python/0763.partition_lables.md) |
| 787 | Cheapest Flights Within K Stops | [Solution](python/0787.cheapest_flight_within_k_stops.md) |
| 1475 | Final Prices With a Special Discount in a Shop | [Solution](python/1475.final_prices_with_a_special_discount_in_a_shop.md) |
| 1584 | Min Cost to Connect All Points | [Solution](python/1584.min_cost_to_connect_all_points.md) |

## Good Starting Points

- [foundation/pattern-templates.md](foundation/pattern-templates.md)
- [foundation/the-dark-arts-of-dynamic-programming.md](foundation/the-dark-arts-of-dynamic-programming.md)
- [foundation/graph.md](foundation/graph.md)
- [foundation/trees.md](foundation/trees.md)
- [foundation/matrix.md](foundation/matrix.md)
- [foundation/sort.md](foundation/sort.md)
