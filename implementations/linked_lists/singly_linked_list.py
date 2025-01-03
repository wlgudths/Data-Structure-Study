class Node():
    def __init__(self, data):
        '''
        summary :
            연결 리스트의 각 노드를 초기화합니다.
        
        args :
            data : 노드에 저장할 데이터
        '''
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        '''
        summary :
            단순 연결 리스트를 초기화합니다.
        
        args :
            인자값이 없습니다.
        '''
        self.head = None
        self.length = 0

    def append(self, data):
        '''
        summary :
            연결 리스트 끝에 데이터를 추가합니다.
        
        args :
            data : 연결 리스트에 추가할 데이터
        '''
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        
        self.length += 1
    
    def pop(self):
        '''
        summary :
            연결 리스트의 마지막 노드를 제거하고 해당 데이터를 반환합니다.
        
        args :
            인자값이 없습니다.
        
        return :
            제거된 노드의 데이터. 리스트가 비어있으면 None 반환
        '''
        if self.head is None:
            return None
        
        node = self.head

        while node.next is not None:
            prev = node
            node = node.next
        
        if node == self.head:
            self.head = None
        else:
            prev.next = None
        
        self.length -= 1
        return node.data
    
    def remove(self, target):
        '''
        summary :
            연결 리스트에서 주어진 값을 가진 첫 번째 노드를 제거합니다.
        
        args :
            target : 제거할 값
        
        return :
            값이 제거되었으면 True, 값이 존재하지 않으면 False 반환
        '''
        node = self.head
        prev = None
        
        while node is not None and node.data != target:
            prev = node
            node = node.next
        
        if node is None:
            return False
        
        if node == self.head:
            self.head = self.head.next
        else:
            prev.next = node.next
        
        self.length -= 1
        return True
    
    def insert(self, idx, data):
        '''
        summary :
            연결 리스트의 특정 인덱스에 데이터를 삽입합니다.
        
        args :
            idx : 데이터를 삽입할 위치
            data : 삽입할 데이터
        '''
        if idx <= 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        elif idx >= self.length:
            self.append(data)
        else:
            node = self.head
            for _ in range(idx - 1):
                node = node.next
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
        
        self.length += 1
    
    def __len__(self):
        '''
        summary :
            연결 리스트의 길이를 반환합니다.
        
        args :
            인자값이 없습니다.
        
        return :
            연결 리스트에 포함된 노드의 개수
        '''
        return self.length

    def __str__(self):
        '''
        summary :
            연결 리스트를 문자열 형태로 반환합니다.
        
        args :
            인자값이 없습니다.
        
        return :
            연결 리스트의 데이터를 순서대로 표현한 문자열
        '''
        if self.head is None:
            return "Linked list is empty"
        
        res = "Head"
        node = self.head

        while node is not None:
            res += " -> " + str(node.data)
            node = node.next
        
        return res