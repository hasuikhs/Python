class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def init_tree():
    global root

    # A 노드를 root로
    new_node = Node('A')
    root = new_node
    # B 노드를 만들고 A노드의 왼쪽으로
    new_node = Node('B')
    root.left = new_node
    # C 노드를 만들고 A노드의 오른쪽으로
    new_node = Node('C')
    root.right = new_node

    # D, E 노드를 만들고
    new_node_1 = Node('D')
    new_node_2 = Node('E')
    # B 노드를 불러오고 D, E를 위치로
    node = root.left
    node.left = new_node_1
    node.right = new_node_2

    # D, E 노드를 만들고
    new_node_1 = Node('F')
    new_node_2 = Node('G')
    # B 노드를 불러오고 D, E를 위치로
    node = root.right
    node.left = new_node_1
    node.right = new_node_2

def preorder_traverse(node):
    if node is None: 
        return
    print(node.data, end = ' -> ')
    preorder_traverse(node.left)
    preorder_traverse(node.right)

def inorder_traverse(node):
    if node is None: return
    inorder_traverse(node.left)
    print(node.data, end = ' -> ')
    inorder_traverse(node.right)

def postorder_traverse(node):
    if node is None: return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end = ' - > ')

levelq = []
def levelorder_traverse(node):
    global levelq
    levelq.append(node)
    while len(levelq) != 0:
        # visit
        visit_node = levelq.pop(0)
        print(visit_node.data, end = ' -> ')
        # child put
        if visit_node.left != None:
            levelq.append(visit_node.left)
        if visit_node.right != None:
            levelq.append(visit_node.right)

if __name__ == '__main__':
    init_tree()
    print('<Preorder Traverse>')
    preorder_traverse(root)

    print('<Inorder Traverse>')
    inorder_traverse(root)

    print('<Postorder Traverse>')
    postorder_traverse(root)

    print('<Levelorser Traverse>')
    levelorder_traverse(root)