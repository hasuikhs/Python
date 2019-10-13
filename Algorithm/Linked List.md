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

   2. ###### Linked List의 삽입

      ```python
      class Node:
          def __init__(self, data, next=None):
              self.data = data
              self.next = next
              
      def init_list():
          global node_A
          node_A = Node("A")
          node_B = Node("B")
          node_D = Node("D")
          node_E = Node("E")
          node_A.next = node_B
          node_B.next = node_D
          node_D.next = node_E
          
      # 노드를 삽입하는 함수
      def insert_node(data): 	# 인수로 data를 받음
          global node_A		# node_A를 global로 선언
          					# global인 node_A는 이미 init_list()함수에서 생성된 node_A 값
          new_node = Node(data) # data가 저장될 new_node를 선언
          node_P = node_A
          node_T = node_A
          while node_T.data <= data: 	# node_T의 data와 인수로 받은 data를 비교하여
              						# node_T의 data가 작으면 
              node_P = node_T
              node_T = node_T.next	# node_T는 다음 노드를 가리킴
          
          # node_T.data가 인수로 받은 data보다 크게 되면
          # 해당 위치가 인수로 받은 data를 사용하여 생성한 new_node가 삽입될 위치가 됨
          new_node.next = node_T		
          node_P.next = new_node
          
      def print_list():
          global node_A
          node = node_A
          while node:
              print(node.data)
              node = node.next
          print
          
      if __name__ == '__main__' :
          print("연결 리스트 초기화 후")
          init_list()
          print_list()
          print("노드 C를 추가한 후")
          insert_node("C")
          print_list()
          
      # 연결 리스트 초기화 후
      # A
      # B
      # D 
      # E
      # 노드 C를 추가한 후
      # A
      # B
      # C
      # D
      # E
      ```

      

