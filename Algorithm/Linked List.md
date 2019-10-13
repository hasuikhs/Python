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

1.  