class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree :

    def __init__(self):
        self.root = None


    def append(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._append_recursive(self.root, data)
    def _append_recursive(self,node,data):
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else :
                self._append_recursive(node.right,data)
        elif data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._append_recursive(node.left, data)


    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None:
            return str(data)+" verisi bulunmuyor"
        elif node.data == data:
            return str(data)+" verisi bulunuyor"
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def delete(self,data):
        self.delete_func(self.root,self.root,data)

    def delete_func(self,prev,node,data):
        if node is None:
            return node
        if data > node.data:
            self.delete_func(node,node.right,data)
        elif data < node.data:
            self.delete_func(node,node.left, data)
        else:
            if node.left is None:
                if prev.right == node:
                    prev.right = node.right
                    return prev
                else:
                    prev.left = node.right
                    return prev
            elif node.right is None:
                if prev.right == node:
                    prev.right = node.left
                    return prev
                else:
                    prev.left = node.left
                    return prev
            new_data = self.find_left_max(node.left)
            node.data = new_data.data
            self.delete_func(node,node.left,node.data)

    def find_left_max(self, node):
        while node.right is not None:
            node = node.right
        return node
    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, depth):
        if node is not None:
            self._print_tree_recursive(node.right, depth + 1)
            print("   " * depth + str(node.data))
            self._print_tree_recursive(node.left, depth + 1)




tree = BinarySearchTree()
tree.append(6)
tree.append(2)
tree.append(12)
tree.append(8)
tree.append(7)
tree.append(14)
tree.append(10)
tree.append(13)
tree.append(16)
print(tree.search(12))
tree.delete(12)
print(tree.search(12))
tree.print_tree()
