#  Binary Tree Paths

## 问题描述

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。


## 代码实现

1.
``` C
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int Path(struct TreeNode* root);
void Connect(struct TreeNode* root, char** array, char* spre, int* pindex);
char* stringAdd(char* s, int val);
char** binaryTreePaths(struct TreeNode* root, int* returnSize);

int Path(struct TreeNode* root){
    if (root == NULL)  return 0;
    if (root->left == NULL && root->right == NULL)  return 1;
    return Path(root->left) + Path(root->right);
}
void Connect(struct TreeNode* root, char** array, char* spre, int* pindex){
    char* s;
    if (root->left == NULL && root->right == NULL){
        s = stringAdd(spre, root->val);
        array[(*pindex)++] = s;
    }
    if (root->left != NULL){
        s = stringAdd(spre, root->val);
        Connect(root->left, array, s, pindex);
        free(s);
    }
    if (root->right != NULL){
        s = stringAdd(spre, root->val);
        Connect(root->right, array, s, pindex);
        free(s);
    }
}
char* stringAdd(char* s, int val){
    char temp[10];
    if (s == "")  sprintf(temp, "%d", val);
          else  sprintf(temp, "->%d", val);
    char* new = (char*)calloc(strlen(s) + strlen(temp) + 1, sizeof(char));
    strcpy(new, s);
    strcat(new, temp);
    return new;
}
char** binaryTreePaths(struct TreeNode* root, int* returnSize) {
    int index = 0;
    if (root == NULL)  return NULL;
    *returnSize = Path(root);
    int paths = *returnSize;
    char** pathsArray = (char**)calloc(paths, sizeof(char*));
    Connect(root, pathsArray, "", &index);
    return pathsArray;
}
```


2.递归法
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def allPaths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    allPaths(root.left, path)
                    allPaths(root.right, path)

        paths = []
        allPaths(root, '')
        return paths
```

3.迭代
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        if not root:
            return []

        paths = []
        stack = [(root,str(root.val))]

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path+'->'+str(node.left.val)))
            if node.right:
                stack.append((node.right, path+'->'+str(node.right.val)))

        return paths
```

## 思考总结

本题主要考察二叉树遍历操作，输出二叉树由根节点到叶子节点的所有路径。

在算法设计上，主要判断某一条根节点到叶子节点路径的长度，调用Path函数采用递归方法。其次用Connect函数遍历左子树和右子树，添加节点。最后将得到的二维指针返回，得到所求的所有路径。

递归法  
最直观的方法是使用递归。在递归遍历二叉树时，需要考虑当前的节点和它的孩子节点。如果当前的节点不是叶子节点，则在当前的路径末尾添加该节点，并递归遍历该节点的每一个孩子节点。如果当前的节点是叶子节点，则在当前的路径末尾添加该节点后，就得到了一条从根节点到叶子节点的路径，可以把该路径加入到答案中。

使用迭代（广度优先搜索）的方法实现。我们维护一个队列，存储节点以及根到该节点的路径。一开始这个队列里只有根节点。在每一步迭代中，我们取出队列中的首节点，如果它是一个叶子节点，则将它对应的路径加入到答案中。如果它不是一个叶子节点，则将它的所有孩子节点加入到队列的末尾。当队列为空时，迭代结束。
