# TreeNode object structure.
class TreeNode:
  # Unique integer id to identify this node.
  id: int;
 # Pointer to parent TreeNode reference. Only the
 # root node has a None parent TreeNode reference.
  parent: TreeNode 
 # List of pointers to child TreeNodes.
  children: TreeNode[]


# g is the graph/tree represented as an adjacency
# list with undirected edges. If there’s an edge between
# (u, v) there’s also an edge between (v, u).
# rootId is the id of the node to root the tree from.
def rootTree(g, rootId = 0):
 root = TreeNode(rootId, None, [])
 return buildTree(g, root, None)
# Build tree recursively depth first.
function buildTree(g, node, parent):
 for childId in g[node.id]:
 # Avoid adding an edge pointing back to the parent.
 if parent != None and childId == parent.id:
 continue
 child = TreeNode(childId, node, [])
 node.children.add(child)
 buildTree(g, child, node)
 return node