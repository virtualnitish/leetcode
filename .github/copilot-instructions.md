# Copilot Instructions for LeetCode Jadia

## Project Overview
This is a personal repository for LeetCode solutions and algorithm study materials. It contains Python solutions to problems, reusable patterns, and foundation notes on data structures and algorithms.

## File Structure
- `python/`: Problem solutions in Markdown format (e.g., `0001.two_sum.md`)
- `foundation/`: Algorithm templates and theory notes
- `anki_revision/`: Spaced-repetition study aids
- `tools/`: Utility scripts for management (filename_generate, summary_generate)
- `Makefile`: Entry point for workflow automation (make new, make summary)

## Code Style and Patterns
Follow the established Python patterns from the README.md cheat sheet:

### Data Structures
- Use `collections.deque` for BFS queues: `queue = deque([root]); node = queue.popleft()`
- Use `heapq` for priority queues: `heapq.heappush(heap, (priority, value))`
- Use `defaultdict(int)` for frequency counting
- Prefer dict comprehensions for index maps: `{val: idx for idx, val in enumerate(arr)}`

### Iteration
- Use `enumerate` for index-value pairs: `for i, num in enumerate(nums)`
- Use `zip` for adjacent comparisons: `for w1, w2 in zip(words, words[1:])`
- Prefer iterators over list operations: `preorder_iter = iter(preorder); root_val = next(preorder_iter)`

### Sorting and Strings
- Use `sorted()` for new sorted values, `.sort()` for in-place
- Join lists with `','.join(res)`, split with `.split(',')`
- Use `max()`/`min()` with `map()` for aggregations: `max(map(len, wordSet))`

## Problem Solution Format
Each problem file in `python/` follows this structure:
1. Title with problem number
2. Python code block with solution
3. Explanation of approach and key tricks
4. Time and space complexity analysis
5. Brief tips on Python usage

Example: [python/0001.two_sum.md](python/0001.two_sum.md)

## Filename Convention
Use `make new` to create filenames in format `NNNN.description.md` where NNNN is zero-padded problem number.

## Key References
- [README.md](README.md): Python cheat sheet and repository overview
- [foundation/pattern-templates.md](foundation/pattern-templates.md): Reusable algorithm templates
- [foundation/the-dark-arts-of-dynamic-programming.md](foundation/the-dark-arts-of-dynamic-programming.md): DP patterns
- [foundation/graph.md](foundation/graph.md): Graph algorithms
- [foundation/trees.md](foundation/trees.md): Tree traversals and operations

## Development Workflow
- Edit Markdown files directly for solutions and notes
- Test Python code snippets within the Markdown files
- Use foundation notes for algorithm patterns when solving new problems
- Maintain consistent formatting and include complexity analysis
- Use relative paths for all links in Markdown files (e.g., `[file.md](file.md)` instead of absolute paths)</content>
<parameter name="filePath">/home/nitish/workspace/leetcode/leetcode_jadia/.github/copilot-instructions.md