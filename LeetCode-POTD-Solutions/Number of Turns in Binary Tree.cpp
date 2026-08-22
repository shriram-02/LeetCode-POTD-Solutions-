/* Structure of Binary Tree Node
class Node {
  public:
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
}; */

  class Solution {
    public:

      // Finds LCA of two given nodes
      Node* findLCA(Node* root, int p, int q) {
          if (root == nullptr)
              return nullptr;

          if (root->data == p || root->data == q)
              return root;

          Node* left = findLCA(root->left, p, q);
          Node* right = findLCA(root->right, p, q);

          if (left && right)
              return root;

          return left ? left : right;
      }

      // Stores path from root to target node using L/R directions
      bool findPath(Node* root, int target, string& path) {
          if (root == nullptr)
              return false;

          if (root->data == target)
              return true;

          // Try going left
          path.push_back('L');
          if (findPath(root->left, target, path))
              return true;
          path.pop_back();

          // Try going right
          path.push_back('R');
          if (findPath(root->right, target, path))
              return true;
          path.pop_back();

          return false;
      }

      // Counts direction changes in a path
      int countTurns(string& path) {
          int turns = 0;

          for (int i = 1; i < path.length(); i++) {
              if (path[i] != path[i - 1])
                  turns++;
          }

          return turns;
      }

      // Returns number of turns required from first node to second node
      int numberOfTurns(Node* root, int p, int q) {

          Node* lca = findLCA(root, p, q);

          if (lca == nullptr)
              return -1;

          string pathFirst = "";
          string pathSecond = "";

          // Paths from LCA to both nodes
          findPath(lca, p, pathFirst);
          findPath(lca, q, pathSecond);

          int turns = 0;

          /*
          If LCA is one of the nodes, there is no extra
          turn at LCA because we start from that node.
          */
          if (lca->data == p || lca->data == q) {

              string path = (lca->data == p) ? pathSecond : pathFirst;

              turns = countTurns(path);
          }

          else {

              /*
              We go:
              first -> LCA -> second

              At LCA, we change direction from one subtree
              to another, so it contributes one turn.
              */
              turns = countTurns(pathFirst) + countTurns(pathSecond) + 1;
          }

          // No turns means both nodes lie on a straight path
          return turns == 0 ? -1 : turns;
      }
  };