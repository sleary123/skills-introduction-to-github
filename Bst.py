import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, cur, value):
        if value < cur.value:
            if cur.left:
                self._add(cur.left, value)
            else:
                cur.left = Node(value)
        elif value > cur.value:
            if cur.right:
                self._add(cur.right, value)
            else:
                cur.right = Node(value)

    def find_node(self, value):
        return self._find(self.root, value)

    def _find(self, cur, value):
        if not cur:
            return False
        if cur.value == value:
            return True
        return self._find(cur.left, value) if value < cur.value else self._find(cur.right, value)

    def delete_node(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, cur, value):
        if not cur:
            return None
        if value < cur.value:
            cur.left = self._delete(cur.left, value)
        elif value > cur.value:
            cur.right = self._delete(cur.right, value)
        else:
            if not cur.left:
                return cur.right
            if not cur.right:
                return cur.left
            min_val = self._min(cur.right)
            cur.value = min_val
            cur.right = self._delete(cur.right, min_val)
        return cur

    def _min(self, node):
        while node.left:
            node = node.left
        return node.value

    def print_tree(self):
        vals = []
        self._inorder(self.root, vals)
        print("Tree:", vals)

    def _inorder(self, node, vals):
        if node:
            self._inorder(node.left, vals)
            vals.append(node.value)
            self._inorder(node.right, vals)

if __name__ == "__main__":
    bst = BST()
    size = random.randint(5, 50)
    nums = random.sample(range(1, 1001), size)
    print("Input Set:", nums)

    for n in nums:
        bst.add_node(n)
    print("\nInitial:")
    bst.print_tree()

    new_val = random.randint(1, 1000)
    print(f"\nAdd {new_val}:")
    bst.add_node(new_val)
    bst.print_tree()

    del_val = random.choice(nums)
    print(f"\nDelete {del_val}:")
    bst.delete_node(del_val)
    bst.print_tree()

    find_exist = random.choice(nums)
    find_missing = random.randint(1, 1000)
    while find_missing in nums:
        find_missing = random.randint(1, 1000)
    print(f"\nFind {find_exist}: {'Found' if bst.find_node(find_exist) else 'Not Found'}")
    print(f"Find {find_missing}: {'Found' if bst.find_node(find_missing) else 'Not Found'}")
