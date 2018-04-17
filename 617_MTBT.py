ass Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        p = TreeNode(t1.val if t1 else 0 + t2.val if t2 else 0)
        p.left = mergeTrees(t1.left, t2.left)
        p.right = mergeTrees(t1.right, t2.right)
        return p
