def lcaOfThreeNodes(root, node1, node2, node3):
    
    # Write your code here.
    if root is None:
        return None
        
    if root.data == node1 or root.data == node2 or root.data == node3:
        return root.data

    Leftlca = lcaOfThreeNodes(root.left, node1, node2, node3)
    Rightlca = lcaOfThreeNodes(root.right, node1, node2, node3)

    if Leftlca and Rightlca:
        return root.data

    if Leftlca is None:
        return Rightlca

    if Rightlca is None:
        return Leftlca

    return root.data
