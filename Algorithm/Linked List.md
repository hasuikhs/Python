## Linked List

- 노드(Node)

  ```python
  class Node:
      def __init__(self, data, next=None):
          self.data = data
          self.next = next
  ```

- Linked List의 특징

  - 배열의 특징은 배열을 생성할 때 한번에 총 메모리를 확보하여 사용하기 때문에

    프로그램이 실행되는 중간에 배열의 크기를 바꾸는 것이 불가능

  - 이와 같은 문제점을 해결해주는 것이 Linked List

1. #####  Linked List의 삽입과 삭제 알고리즘

   1. ###### Linked List의 초기화

      ```python
      # 4개의 노드가 연결된 Linked List
      class Node:
          def __init__(self, data, next=None):
              self.data = data
              self.next = next
              
      def init_list():
          global node_A
          node_A = Node("A")
          node_B = Node("B")
          node_C = Node("C")
          node_D = Node("D")
          node_A.next = node_B
          node_B.next = node_C
          node_C.next = node_D
      
      def print_list():
          global node_A
          node = node_A
          while node:
              print(node.data)
              node = node.next
          print
          
      if __name__ =='__main__':
          init_list()
          print_list()
          
      ## A
      ## B
      ## C
      ## D
      ```

      