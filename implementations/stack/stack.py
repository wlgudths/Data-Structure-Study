from linked_lists.singly_linked_list import LinkedList

class Stack(LinkedList):
    def __init__(self):
        '''
        summary :
            스택을 초기화합니다. 연결 리스트를 상속받아 구현합니다.
        
        args :
            인자값이 없습니다.
        '''
        super().__init__()

    def is_empty(self):
        '''
        summary :
            스택이 비어있는지 확인합니다.
        
        args :
            인자값이 없습니다.
        
        return :
            스택이 비어있으면 True, 아니면 False 반환
        '''
        return self.head is None
    
    def push(self, data):
        '''
        summary :
            스택의 맨 위에 데이터를 추가합니다.
        
        args :
            data : 스택에 추가할 데이터
        '''
        self.insert(0, data)
    
    def pop(self):
        '''
        summary :
            스택의 맨 위 데이터를 제거하고 반환합니다.
        
        args :
            인자값이 없습니다.

        return :
            스택의 맨 위에 있는 데이터, 스택이 비어있으면 None 반환
        '''
        if self.is_empty():
            return None
        
        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return data
    
    def __str__(self):
        '''
        summary :
            스택을 문자열 형태로 반환합니다.
        
        args :
            인자값이 없습니다.
        
        return :
            스택 데이터를 순서대로 표현한 문자열
        '''
        if self.head is None:
            return "Linked list is empty"
        
        res = "Top"
        node = self.head

        while node is not None:
            res += " -> " + str(node.data)
            node = node.next
        
        return res


# 사용 예시
if __name__ == "__main__":
    stack = Stack()
    print(f"Is empty? : {stack.is_empty()}")
    stack.push(10)
    print(stack)
    print(f"Is empty ? : {stack.is_empty()}")
    stack.push(20)
    print(stack)
    print(f"Popped value : {stack.pop()}")
    print(stack)