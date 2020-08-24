def tree(values):
  n = len(values)
  tree = values[:]
  for i in range(1, n):
    j = i + (i & -i)
    if j < n:
      tree[j] += tree[i]
  return tree

def prefix_sum(tree, n):
  sum = 0
  while n:
    sum += tree[n]
    n -= (n & -n)
  return sum

def range_query(tree, a, b):
  return prefix_sum(tree, b) - prefix_sum(tree, a-1)

def point_update(tree, pos, val):
  while pos < len(tree):
    tree[pos] += val
    pos += pos & -pos