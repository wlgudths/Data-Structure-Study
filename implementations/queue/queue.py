from linked_lists.singly_linked_list import LinkedList, Node

class Queue(LinkedList):
    def __init__(self):
        '''
        summary :
            큐를 초기화합니다. 연결 리스트를 상속받아 구현합니다.
            tail 포인터를 추가하여 큐의 맨 뒤를 
        
        args :
            인자값이 없습니다.
        '''
        super().__init__()
        self.tail = None

    def is_empty(self):
        '''
        summary :
            큐가 비어있는지 확인합니다.
        
        args :
            인자값이 없습니다.
        
        return :
            큐가 비어있으면 True, 아니면 False 반환
        '''
        return self.head is None
    
    def enqueue(self, data):
        '''
        summary :
            큐의 맨 뒤에 데이터를 추가합니다.
        
        args :
            data : 큐에 추가할 데이터
        '''
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    
    def dequeue(self):
        '''
        summary :
            큐의 맨 앞 데이터를 제거하고 반환합니다.
        
        args :
            인자값이 없습니다.
        
        return :
            큐의 맨 앞에 있는 데이터. 큐가 비어있으면 None 반환
        '''
        if self.is_empty():
            return None
        
        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        self.length -= 1
        return data
    
    def __str__(self):
        '''
        summary :
            큐를 문자열 형태로 반환합니다.
        
        args :
            인자값이 없습니다.
        
        return :
            큐의 데이터를 순서대로 표현한 문자열
        '''
        if self.is_empty():
            return "Queue is empty"
        
        res = "Front"
        node = self.head
        while node:
            res += f" -> {node.data}"
            node = node.next
        
        return res + "-> Rear"


# 사용 예시
if __name__ == "__main__":
    queue = Queue()
    print(queue)
    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)

    print(f"Dequeue : {queue.dequeue()}")
    print(queue)
    print(f"Dequeue : {queue.dequeue()}")
    print(queue)
    print(f"Dequeue : {queue.dequeue()}")
    print(queue)