#  Binary Tree Paths

## 问题分析
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

## 代码实现
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

## 总结体会

本题主要考察二叉树遍历操作，输出二叉树由根节点到叶子节点的所有路径。

在算法设计上，主要判断某一条根节点到叶子节点路径的长度，调用Path函数采用递归方法。其次用Connect函数遍历左子树和右子树，添加节点。最后将得到的二维指针返回，得到所求的所有路径。