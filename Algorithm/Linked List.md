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

   3. ###### Linked List의 삭제
   
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
          
      # 노드를 삭제하는 함수
      def delete_node(del_data):	# 인수로 del_data를 받음
          global node_A			# global로 node_A로 선언한 Linked List를 사용
          pre_node = node_A		# 이 Linked List를 가리키는 pre_node 선언
          next_node = pre_node.next 	# pre_node의 다음 노드에 해당하는 
          							# pre_node.next를 nexgt_node로 선언
          if pre_node.data == del_data:	# 현재 Linked List의 첫번쨰 노드인 pre_node.data가
              							# 삭제할 del_data라면 삭제할 노드가 가장 첫번째 노드
              node_A = next_node		# node_A에 next_node를 저장하고
              del pre_node			# 현재 노드인 pre_node를 삭제한 후에 
              return					# delete_node() 함수 리턴
          
          while next_node:		# 현재 Linked List를 가리키는 next_node가 존재할 동안
              if next_node.data == del_data:	# next_node의 data가 인수로 받은 삭제할 
                  							# 데이터인 del_data와 같다면
                      						# next_node의 다음 노드를 가리키는 링크를 
                  pre_node.next = next_node.next	# 이전 노드인 pre_node의 next에 자장
                  del next_node				# next_node를 삭제한 후에 리턴
                  break
              # 그러나 next_node.data가 인수로 받은 del_data와 같지 않다면
              pre_node = next_node	# 이전 노드인 pre_node는 현재 노드인 next_node를 가리킴
              next_node = next_node.next	# next_node는 next_node.next를 가리킴
      
      def insert_node(data):
          global node_A
          new_node = Node(data)
          node_P = node_A
          node_T = node_A
          while node_T.data <= data:
              node_P = node_T
              node_T = node_T.next
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
          print("노드 D를 삭제한 후")
          delete_node("D")
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
      # 노드 D를 삭제한 후
      # A
      # B
      # C
      # E
      ```
   
2. ##### 이중 연결 리스트

   1. ###### 이중 연결 리스트?

      - 연결 리스트는 배열과 달리 프로그램의 실행 중에도 새로운 노드를 삽입 또는 삭제하기가 간단하다.
      - 하지만, 무조건 한 방향으로만 링크를 따라가야 하기 때문에 다소 불편한 점이 존재한다.

      ```PYTHON
      class Node:
          def __init__(self, data, next=None, prev=None):
              self.data = data
              self.next = next
              self.prev = prev
          
      def init_list():
          global node_A
          node_A = Node('A')
          node_B = Node('B')
          node_D = Node('D')
          node_E = Node('E')
          node_A.next = node_B
          node_B.next = node_D
          node_B.prev = node_A
          node_D.next = node_E
          node_E.prev = node_D
      
      def print_list():
          global node_A
          node = node_A
          while node:
              print(node.data)
              node = node.next
          print
          
      if __name__ == '__main__':
          print('연결리스트 초기화 후')
          init_list()
          print_list()
      ```

      ```
      연결리스트 초기화 후
      A
      B
      D
      E
      ```

   2. ###### 삽입 알고리즘

      - 삽입할 때는 단일 연결 리스트의 삽입과 동일하다.

      ```python
      def print_list():
          global node_A
          node = node_A
          while node:
              print(node.data)
              node = node.next
          print
          
      def insert_node(data):
          global node_A
          new_node = Node(data)
          node_P = node_A
          node_T = node_A
          while node_T.data <= data:
              node_P = node_T
              node_T = node_T.next
          new_node.next = node_T
          node_P.next = new_node
          new_node.prev = node_P
          node_T.prev = new_node
      
      if __name__ == '__main__':
          print('연결리스트 초기화 후')
          init_list()
          print_list()
      
          print('노드 C 추가 후')
          insert_node('C')
          print_list()
      ```

      ```
      연결리스트 초기화 후
      A
      B
      D
      E
      노드 C 추가 후
      A
      B
      C
      D
      E
      ```

   3. ###### 삭제 알고리즘

      ```python
      def delete_node(del_data):
          global node_A
          pre_node = node_A
          next_node = pre_node.next
          next_next_node = next_node.next
      
          if pre_node.data == del_data:
              node_A = next_node
              del pre_node
              return
          
          while next_node:
              if next_node.data == del_data:
                  next_next_node = next_node.next
                  pre_node.next = next_node.next
                  next_next_node.prev = next_node.prev
                  del next_node
                  break
              pre_node = next_node
              next_node = next_node.next
              next_next_node = next_node.next
      
      if __name__ == '__main__':
          print('연결리스트 초기화 후')
          init_list()
          print_list()
      
          print('노드 C 추가 후')
          insert_node('C')
          print_list()
      
          print('노드 D의 삭제 후')
    delete_node('D')
          print_list()
      ```
      
      ```
      노드 D의 삭제 후
      A
      B
      C
      E
      ```
      
      

