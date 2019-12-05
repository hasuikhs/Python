# 트리(Tree)

> Tree는 프로그래밍 언어와 상관없이 가장 많이 사용되는 자료구조이다. 트리구조에서 사용되는 여러 가지 알고리즘은 다른 알고리즘의 기본이 되는 알고리즘이다.

## 1. 트리의 개념과 용어

### 1.1 트리 구조

![img](트리(Tree).assets/tree-terms.png)

#### 1.1.1 노드(Node)

- 가장 상위에 있는 노드를 **루트(Root)**.
- 자신의 노드보다 상위에 있는 노드를 **부모 노드(Parent Node)**.
- 자신의 노드보다 하위에 있는 노드를 **자식 노드(Child Node)**.
- 최하위 노드를 **리프 노드(Leaf Node)** 혹은 **터미널 노드(Terminal Node)**.

- 같은 부모 노드를 갖는 노드들의 사이를 **형제 노드(Sibling Node)**.
- 자식 노드는 몇개라도 상관없지만 **부모 노드는 2개 이상 존재 불가능**.

#### 1.1.2 레벨(Level)과 높이(Height)

- **레벨**은 루트 노드부터 해당 노드까지 경로를 찾아 오는데 **방문한 총 노드의 수**.
- **높이**는 **트리 구조 내에서 가장 큰 레벨**을 그 트리 구조의 높이라고 함.

### 1.2 트리의 용어

- **차수** : 한 노드에 연결된 서브 트리의 개수(ex: 위의 그림에서 노드 A의 차수는 2)
- 이 중에서 차수가 2개 이하의 트리 구조를 특별히 **이진 트리(Binary Tree)**라고 함.

## 2. 이진 트리(Binary Tree)

- 위에서 언급했듯이 **자식노드를 2개 이하만 갖는 트리**

### 2.1 이진 트리의 구조와 특성

![이진 트리에 대한 이미지 검색결과](트리(Tree).assets/9911BB445C5A844001.png)

- 이진 트리는 자식 노드가 2개만 존재하기 때문에 구현이 간단하다는 장점이 존재.

### 2.2 이진 트리의 종류

- **정 이진 트리(full binary tree)** : 단말 노드가 아닌 모든 노드가 2개의 자식을 가진 트리.

- **포화 이진 트리(perfect binary tree)** : 모든 단말 노드의 깊이가 같은 정 이진 트리.

- **완전 이진 트리(complete binary tree)** : 마지막 레벨을 제외하고 모든 노드가 채워진 이진트리.

  ​						마지막 레벨의 노드들은 왼쪽으로 채워져 있고 마지막 레벨이 다 채워질 수도 있음.

- **균형 이진 트리(balanced binary tree)** : 모든 단말 노드의 깊이 차이가 많아야 1인 트리.

## 3. 트리의 순회 알고리즘

![image-20191205223322809](트리(Tree).assets/image-20191205223322809.png)

- **전위 순회(Pre-Order Traverse)** : A -> B -> D -> E -> C -> F -> G

- **중위 순회(In-Order Traverse)** : D -> B -> E -> A -> F -> C -> G

- **후위 순회(Post-Order Traverse)** : D -> E -> B -> F -> G -> C -> A

- **단계 순위 순회(Level-Order Traverse)** : 위에서부터 차례대로 방문하는 순서

  ​																	   A -> B -> C -> D -> E -> F -> G

### 3.1 트리 선언 코드

- 위의 그림처럼 만들어 보자

```python
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
```

### 3.2 전위 순회(Pre-Order Traverse) 알고리즘

- 트리 구조를 순회하기 위해 반드시 지켜야 할 기본 규칙은 **노드는 오직 한번만 방문**한다.

- A -> B -> D -> E -> C -> F -> G 로 돌아야 한다.

  ![image-20191205223322809](트리(Tree).assets/image-20191205223322809.png)

```python
def preorder_traverse(node):
    if node is None: return
    print(node.data, end = ' -> ')
    preorder_traverse(node.left)
    preorder_traverse(node.right)

if __name__ == '__main__':
    init_tree()
    print('<Preorder Traverse>')
    preorder_traverse(root)
```

```
<Preorder Traverse>
A -> B -> D -> E -> C -> F -> G -> 
```

### 3.3 중위 순회(In-Order Traverse) 알고리즘

- **왼쪽 자식 노드를 방문하고 그 다음 부모 노드를 방무난 후 다시 오른쪽 자식 노드를 방문** 하는 알고리즘

- D -> B -> E -> A -> F -> C -> G

  ![image-20191205223322809](트리(Tree).assets/image-20191205223322809.png)

```python
def inorder_traverse(node):
    if node is None: return
    inorder_traverse(node.left)
    print(node.data, end = ' -> ')
    inorder_traverse(node.right)
    
if __name__ == '__main__':
    init_tree()
    print('<Inorder Traverse>')
    inorder_traverse(root)
```

```
<Inorder Traverse>
D -> B -> E -> A -> F -> C -> G ->
```

### 3.4 후위 순회(Post-Order Taverse) 알고리즘

- **왼쪽 자식 노드르 방문한후 오른쪽 자식 노드를 방문하고 부모 노드를 방문**

- D -> E -> B -> F -> G -> C -> A

  ![image-20191205223322809](트리(Tree).assets/image-20191205223322809.png)

```python
def postorder_traverse(node):
    if node is None: return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end = ' - > ')

if __name__ == '__main__':
    init_tree()
    print('<Postorder Traverse>')
    postorder_traverse(root)
```

```
<Postorder Traverse>
D - > E - > B - > F - > G - > C - > A - >
```

### 3.5 단계 순회(Level-Order Traverse) 알고리즘

- **루트 노드부터 단계 순서대로 왼쪽에서 오른쪽으로 방문**하는 알고리즘

- A -> B -> C -> D -> E -> F -> G

  ![image-20191205223322809](트리(Tree).assets/image-20191205223322809.png)

```python
levelq = []
def levelorder_traverse(node):
    global levelq
    # 먼저 매개 변수로 받은 현재 노드인 node를 큐인 levelq에 저장
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
    print('<Levelorder Traverse>')
    levelorder_traverse(root)
```

```
<Levelorder Traverse>
A -> B -> C -> D -> E -> F -> G ->
```