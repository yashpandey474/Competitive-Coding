def longestUnivaluePath(node):
    # Write your code here.

    #STORE LENGTH OF MAX UNIVALUE PATH
    result = 0

    def dfs(root):
        nonlocal result
        #NONE
        if not root:
            return 0

        #CHECK LEFT AND RIGHT
        left_length = dfs(root.left)
        right_length = dfs(root.right)

        #UNIVALUE PATHS THROUGH CURRENT NODE
        left_arrow = right_arrow = 0

        #CHECK WITH LEFT
        if root.left and root.left.data == root.data:
            left_arrow = 1 + left_length

        #CHECK WITH RIGHT
        if root.right and root.right.data == root.data:
            right_arrow = 1 + right_length

        #UPDATE RESULT
        result = max(result, left_arrow + right_arrow)

        #RETURN
        return max(left_arrow, right_arrow)

    dfs(node)
    return result
        
        
