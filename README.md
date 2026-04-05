# LeetCode Jadia

Personal repository for LeetCode solutions, reusable patterns, and foundation notes. The `python/` directory holds problem-wise writeups, while `foundation/` collects algorithm templates and deeper theory notes.

## Repository Layout

- `python/`: LeetCode problem notes and Python solutions.
- `foundation/`: Core algorithm notes for graphs, trees, DP, sorting, search, heaps, matrices, and templates.
- `foundation/deep-dive/`: Longer topic-specific explanations.
- `anki_revision/`: Revision material and spaced-repetition helpers.
- `filename_generate.py`: Utility script for filename generation.

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

## Good Starting Points

- [foundation/pattern-templates.md](foundation/pattern-templates.md)
- [foundation/the-dark-arts-of-dynamic-programming.md](foundation/the-dark-arts-of-dynamic-programming.md)
- [foundation/graph.md](foundation/graph.md)
- [foundation/trees.md](foundation/trees.md)
- [foundation/matrix.md](foundation/matrix.md)
- [foundation/sort.md](foundation/sort.md)
