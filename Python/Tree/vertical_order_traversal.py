# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        #LEVEL-ORDER TRAVERSAL
        queue = []
        #RESULT STORED IN A MAP
        map_vertical_levels = {}
        result = []

        if not root:
            return result

        #ADD INITIAL VALUE: NODE, VERTICAL, LEVEL
        queue.append((root, 0, 1))

        while queue:
            current, vertical, level = queue.pop(0)

            #ADD TO VERTICAL'S LEVEL
            if vertical not in map_vertical_levels:
                map_vertical_levels[vertical] = {}
            #ADD TO VERTICAL'S LEVEL
            if level not in map_vertical_levels[vertical]:
                map_vertical_levels[vertical][level] = []
            
            map_vertical_levels[vertical][level].append(current.val)
            if current.left:
                queue.append((current.left, vertical - 1, level + 1))
            if current.right:
                queue.append((current.right, vertical + 1, level + 1))
            
        #ITERATE THROUGH THE MAP
        for vertical, level_dictionary in sorted(map_vertical_levels.items()):
            vert = []
            for level, data_list in sorted(level_dictionary.items()):
                for i in sorted(data_list):
                    vert.append(i)

            result.append(vert)
        
        return result
