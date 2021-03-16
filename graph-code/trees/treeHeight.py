# The height of a tree is the number of
# edges from the root to the lowest leaf.
def treeHeight(node):
 # Handle empty tree case
 if node == None:
   return -1
 # Identify leaf nodes and return zero
 if node.left == None and node.right == None:
  return 0
 return max(treeHeight(node.left),
 treeHeight(node.right)) + 1

# or
def treeHeight2(node):
 # Handle empty tree case
 if node == None:
   return -1
 return max(treeHeight(node.left),
 treeHeight(node.right)) + 1