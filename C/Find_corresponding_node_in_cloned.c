/*
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
*/


void preOrder(TreeNode* root, TreeNode* &ref, TreeNode* target){
        if(root == NULL){
            return;
        }
        if(root->val == target->val){
            ref = root;
        }

        preOrder(root->left, ref, target);
        preOrder(root->right, ref, target);
    }
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        TreeNode* ref = NULL;
        preOrder(cloned, ref, target);
        return ref;
    }
